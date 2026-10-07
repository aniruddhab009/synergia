"""Independent review model, Python standard library only.

Source: Opus proposed baseline PDF, sections 8.4 and Appendix B, not its code.
Scope: R1-R7 control flow over immutable synthetic bid snapshots. No robot,
allocation, resources, physics, graph revision, or production correctness claim.
Run: python3 independent_round_review.py --output results.json
"""
import argparse
import heapq
import itertools
import json
import math
import random
from collections import Counter


def resolve(votes, n=3):
    vals = list(votes.values())
    if "ABORT" in vals:
        return "ABORT"
    if len(set(vals)) > 1:
        return "CONFLICT_ABORT"
    if len(vals) == n:
        return "COMMIT:" + vals[0]
    return None


def enumerate_vote_views():
    checked = 0
    # Every sender has at most one vote. Each recipient sees an arbitrary subset.
    for global_votes in itertools.product((None, "D", "E", "ABORT"), repeat=3):
        edges = [(s, d) for s in range(3) for d in range(3)
                 if s != d and global_votes[s] is not None]
        for mask in range(1 << len(edges)):
            views = [{i: v} if v is not None else {} for i, v in enumerate(global_votes)]
            for bit, (s, d) in enumerate(edges):
                if mask & (1 << bit):
                    views[d][s] = global_votes[s]
            decisions = [resolve(view) for view in views]
            commits = {d for d in decisions if d and d.startswith("COMMIT")}
            assert len(commits) <= 1
            assert not (commits and any(d in ("ABORT", "CONFLICT_ABORT") for d in decisions))
            checked += 1
    return checked


class Agent:
    def __init__(self):
        self.current = 0
        self.opened = {}
        self.own_bid = {}
        self.own_vote = {}
        self.bids = {}
        self.votes = {}
        self.outcomes = {0: "GENESIS"}
        self.aborts = 0
        self.streak = 0
        self.next_at = 0
        self.blocked = False


class Model:
    # 20 ms ticks; 100 ms push; 500 ms bid deadline; 1 s slow pull/backoff.
    def __init__(self, seed, profile, rounds=4, pull_limit=None):
        self.rng = random.Random(seed)
        self.profile = profile
        self.rounds = rounds
        self.pull_limit = pull_limit
        self.agents = [Agent() for _ in range(3)]
        self.queue = []
        self.serial = 0
        self.t = 0

    def alive(self, i):
        return not (self.profile == "crash" and i == 2 and self.t >= 1)

    def partition(self, s, d):
        end = 400 if self.profile == "healing_partition" else 10**9
        return self.profile in ("healing_partition", "permanent_partition") and 1 in (s, d) and 1 <= self.t < end

    def send(self, s, d, kind, r, payload):
        if s == d or not self.alive(s) or self.partition(s, d):
            return
        loss = {"loss10": .1, "loss40": .4}.get(self.profile, 0)
        if self.rng.random() < loss:
            return
        copies = 2 if self.profile in ("loss10", "loss40") and self.rng.random() < .1 else 1
        for _ in range(copies):
            self.serial += 1
            # 1-5 ticks avoids zero-delay event-loop ambiguity.
            heapq.heappush(self.queue, (self.t + self.rng.randint(1, 5), self.serial, s, d, kind, r, payload))

    def broadcast(self, i, kind, r, payload):
        for d in range(3):
            self.send(i, d, kind, r, payload)

    def open(self, i, r):
        a = self.agents[i]
        if a.blocked or r != a.current + 1 or a.current not in a.outcomes:
            return
        a.current = r
        a.opened[r] = self.t
        a.bids.setdefault(r, {})[i] = a.outcomes[r-1]
        a.own_bid[r] = a.outcomes[r-1]
        self.broadcast(i, "BID", r, a.own_bid[r])

    def vote(self, i, r, value):
        a = self.agents[i]
        assert r not in a.own_vote
        a.own_vote[r] = value
        a.votes.setdefault(r, {})[i] = value
        self.broadcast(i, "VOTE", r, value)

    def advance(self, i):
        a = self.agents[i]
        r = a.current
        if r == 0 or r in a.outcomes:
            return
        if len(a.bids.get(r, {})) == 3 and r not in a.own_vote:
            value = "D" + str(r) if len(set(a.bids[r].values())) == 1 else "ABORT"
            self.vote(i, r, value)
        result = resolve(a.votes.get(r, {}))
        if result:
            a.outcomes[r] = result
            if result.endswith("ABORT"):
                a.aborts += 1
                a.streak += 1
                a.next_at = self.t + (50 if a.streak >= 3 else 0)
                a.blocked = a.aborts >= 20 or result == "CONFLICT_ABORT"
            else:
                a.streak = 0

    def deliver(self, s, d, kind, r, payload):
        if not self.alive(d) or self.partition(s, d):
            return
        a = self.agents[d]
        if kind == "REQUEST":
            if r in a.own_bid:
                self.send(d, s, "BID", r, a.own_bid[r])
            if r in a.own_vote:
                self.send(d, s, "VOTE", r, a.own_vote[r])
            return
        if kind == "BID":
            a.bids.setdefault(r, {}).setdefault(s, payload)
            if r == a.current + 1 and a.current in a.outcomes:
                self.open(d, r)
        if kind == "VOTE":
            a.votes.setdefault(r, {}).setdefault(s, payload)
        self.advance(d)

    def run(self, horizon=1000):
        for i in range(3):
            self.open(i, 1)
        for self.t in range(horizon + 1):
            while self.queue and self.queue[0][0] <= self.t:
                _, _, s, d, kind, r, payload = heapq.heappop(self.queue)
                self.deliver(s, d, kind, r, payload)
            for i, a in enumerate(self.agents):
                if not self.alive(i):
                    continue
                r = a.current
                if r not in a.outcomes:
                    elapsed = self.t - a.opened[r]
                    if elapsed in (5, 10):
                        self.broadcast(i, "BID", r, a.own_bid[r])
                        if r in a.own_vote:
                            self.broadcast(i, "VOTE", r, a.own_vote[r])
                    if elapsed >= 25:
                        if r not in a.own_vote:
                            self.vote(i, r, "ABORT")
                        pull_number = (elapsed - 25) // 5
                        early = elapsed < 75 and (elapsed - 25) % 5 == 0
                        late = elapsed >= 75 and (elapsed - 75) % 50 == 0
                        if (early or late) and (self.pull_limit is None or pull_number < self.pull_limit):
                            self.broadcast(i, "REQUEST", r, None)
                    self.advance(i)
                elif sum(v.startswith("COMMIT") for v in a.outcomes.values()) < self.rounds and self.t >= a.next_at:
                    self.open(i, r + 1)
            for r in set().union(*(a.outcomes.keys() for a in self.agents)):
                seen = {a.outcomes[r] for a in self.agents if r in a.outcomes}
                assert len(seen) <= 1, (self.profile, self.t, r, seen)
        return all(sum(v.startswith("COMMIT") for v in a.outcomes.values()) >= self.rounds
                   for i, a in enumerate(self.agents) if self.alive(i))


def counterexamples():
    # A round opening travels for Delta; a peer's bid takes another Delta.
    delta, deadline = 300, 500
    assert 2 * delta > deadline
    # Gate asymmetry: both finish P1; only R receives partner progress.
    progress_received = {"L": False, "R": True}
    phase = {i: "P2" if received else "P1_wait" for i, received in progress_received.items()}
    assert phase == {"L": "P1_wait", "R": "P2"}
    # A lost COMPLETE leaves one replica's dependent task non-ready forever,
    # even though BID_SET and VOTE requests recover every round perfectly.
    ready_views = [{"dependent"}, {"dependent"}, set()]
    assert set.intersection(*ready_views) == set()
    # Quiescence predicate in section 6.6 fails to exclude an uncertain holder.
    states = {"UNCERTAIN"}
    old_quiescent = not states.intersection({"PREPARING", "RUNNING", "VERIFYING"})
    assert old_quiescent
    return {
        "join_deadline": {"first_bid_ms": 0, "peer_joins_ms": 300,
                          "originator_aborts_ms": 500, "peer_bid_arrives_ms": 600},
        "asymmetric_progress": phase,
        "lost_complete_effective_ready": [],
        "uncertain_holder_old_quiescence": old_quiescent,
        "geometric_tilt_degrees_only": {"5mm": math.degrees(math.asin(.005/.8)),
                                       "45mm": math.degrees(math.asin(.045/.8))},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()
    counts = {}
    for profile in ("delay", "loss10", "loss40", "crash", "permanent_partition", "healing_partition"):
        complete = sum(Model(seed, profile).run() for seed in range(100))
        counts[profile] = {"runs": 100, "all_live_agents_committed_four_rounds": complete}
    result = {
        "scope": "Synthetic round-control model; no task, resource or physics validation.",
        "enumerated_vote_visibility_states": enumerate_vote_views(),
        "round_profiles": counts,
        "counterexamples": counterexamples(),
        "limitations": ["Not a reproduction of unavailable Opus code or its 600 runs.",
                        "No exhaustive interleaving or crash-recovery proof.",
                        "R1-R7 simulated with synthetic snapshots; R6 tested only on reached schedules.",
                        "No assertions of physical excursion bounds."],
    }
    encoded = json.dumps(result, indent=2)
    if args.output:
        with open(args.output, "w") as f:
            f.write(encoded + "\n")
    print(encoded)


if __name__ == "__main__":
    main()
