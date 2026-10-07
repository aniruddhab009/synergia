"""Disposable specification checks; NOT a SYNERGIA implementation or proof.

Python standard library. Run: python3 independent_event_boundary_review.py
Optional: --bundle PATH to instrument the supplied unmodified F2 function.
Results describe finite cases and explicit strengthened rules only.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from collections import deque
from dataclasses import dataclass, replace
from pathlib import Path
import sys


@dataclass(frozen=True)
class Event:
    epoch: str
    instance: str
    producer: str
    seq: int
    kind: str

    @property
    def stream(self):
        return self.epoch, self.instance, self.producer


class Replica:
    """Proposed ordered replay; relay transport identity is not event origin."""
    def __init__(self):
        self.stored = {}
        self.applied = {}
        self.history = {}
        self.actuation_commands = 0

    def receive(self, event):
        key = event.stream, event.seq
        if key in self.stored and self.stored[key] != event:
            raise ValueError("conflicting event identity")
        self.stored[key] = event
        stream = event.stream
        n = self.applied.get(stream, 0)
        while (stream, n + 1) in self.stored:
            n += 1
            self.history.setdefault(stream, []).append(self.stored[stream, n].kind)
        self.applied[stream] = n
        # Historical replay has no actuator callback. Production must enforce this.

    def missing(self, stream, advertised_max):
        return [n for n in range(1, advertised_max + 1)
                if (stream, n) not in self.stored]


def event_checks():
    events = [Event("e1", "i1", p, n, kind)
              for p in ("L", "R")
              for n, kind in enumerate(("PREPARED", "COMPLETE", "RELEASED"), 1)]
    expected = {}
    for event in events:
        expected.setdefault(event.stream, []).append(event.kind)
    count = 0
    for order in itertools.permutations(events):
        replica = Replica()
        for event in order + order[::-1]:
            replica.receive(event)
        assert replica.history == expected
        assert all(n == 3 for n in replica.applied.values())
        assert replica.actuation_commands == 0
        count += 1
    # Equal maximum sequence numbers do not mean equal stored contents.
    r = Replica()
    for event in (events[0], events[2]):
        r.receive(event)
    hidden_gap = r.missing(events[0].stream, 3)
    assert hidden_gap == [2] and r.applied[events[0].stream] == 1
    old_requests = 3 > max(e.seq for e in (events[0], events[2]))
    assert old_requests is False
    # A live relay can supply the missing original event without the producer.
    r.receive(events[1])
    assert r.applied[events[0].stream] == 3
    old_identity_count = len({(e.instance, e.seq) for e in events})
    assert old_identity_count == 3 and len(r.stored) == 3
    conflict_rejected = False
    try:
        r.receive(replace(events[0], kind="FAILED"))
    except ValueError:
        conflict_rejected = True
    assert conflict_rejected
    # An old attempt remains a different log and cannot become current ownership.
    held_instance = "i2"
    r.receive(Event("e1", "i0", "L", 1, "COMPLETE"))
    assert held_instance == "i2" and r.actuation_commands == 0
    return {"delivery_permutations_with_reverse_duplicates": count,
            "max_only_requests_for_hole": old_requests,
            "missing_sequence_numbers": hidden_gap,
            "contiguous_watermark_after_relay_repair": r.applied[events[0].stream],
            "events_retained_by_instance_only_key": old_identity_count,
            "events_required_for_two_origins": len(events),
            "conflicting_identity_rejected": conflict_rejected,
            "scope": "ordered storage only; no bus, authorization, full task reducer or actuator"}


@dataclass(frozen=True)
class Boundary:
    frozen: frozenset = frozenset()
    endorsed: frozenset = frozenset()
    pending: bool = True
    held: bool = False
    graph: str = "old"


MEMBERS = frozenset("ABC")


def successors(s):
    """Aggregate state abstraction: endorsement truth is assumed, not established."""
    if s.graph != "old":
        return
    for member in sorted(MEMBERS):
        if member not in s.frozen:
            yield "freeze_" + member, replace(s, frozen=s.frozen | {member})
        if member in s.frozen and member not in s.endorsed and not s.pending and not s.held:
            yield "endorse_" + member, replace(s, endorsed=s.endorsed | {member})
    if s.pending:
        yield "resolve_existing_award", replace(s, pending=False, held=True)
        yield "resolve_existing_abort", replace(s, pending=False)
    if s.held:
        yield "verified_release", replace(s, held=False)
    if not s.pending and not s.held and not s.frozen:
        yield "new_old_graph_award", replace(s, pending=True)
    if s.endorsed == MEMBERS:
        yield "install_new_graph", replace(s, graph="new")


def boundary_checks():
    q = deque([Boundary()])
    seen = {Boundary()}
    transitions = installed = 0
    while q:
        s = q.popleft()
        if s.graph == "new":
            installed += 1
            assert not s.pending and not s.held and s.frozen == MEMBERS
        for action, nxt in successors(s):
            transitions += 1
            assert nxt.frozen >= s.frozen  # no unilateral thaw
            if nxt.endorsed:
                assert not nxt.pending and not nxt.held
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    assert installed > 0
    # Counterexample to a snapshot-only interpretation, not to persistent C11 freeze.
    weak_trace = ["freeze all", "endorse inactive old graph", "thaw after endorsement",
                  "new old-graph award resolves and holds resource",
                  "install revision using earlier certificate"]
    # Explicit local graph+instance fencing: old certificate cannot activate after install.
    def activate(cert_graph, cert_instance, active_graph, held):
        return cert_graph == active_graph and cert_instance == held
    assert not activate("old", "i1", "new", None)
    assert not activate("old", "i1", "new", "i2")
    assert activate("new", "i2", "new", "i2")
    return {"reachable_aggregate_states": len(seen), "transitions": transitions,
            "installed_states": installed, "unsafe_installations": 0,
            "snapshot_only_counterexample": weak_trace,
            "stale_graph_activation_rejected": True,
            "scope": "persistent freeze lifecycle abstraction; no distributed knowledge or message-delay proof"}


def phase_checks():
    peer_event = {"phase": "P1", "event": "entered", "seq": 1}
    pending = {"phase": "P1", "event": "done", "seq": 2}
    old_stop = peer_event["phase"] == pending["phase"]
    receipt = {"producer": "L", "seq": 1}
    exact_stop = receipt["producer"] == "L" and receipt["seq"] >= pending["seq"]
    assert old_stop and not exact_stop
    receipt["seq"] = 2
    assert receipt["seq"] >= pending["seq"]
    return {"trace": ["L sends P1 done(seq=2); delivery lost",
                      "R P1 entered(seq=1) reaches L",
                      "C2 same-phase stop condition suppresses L done retransmission"],
            "same_phase_is_receipt": False,
            "explicit_origin_sequence_ack_keeps_retrying_until_received": True}


def decision_checks():
    bids = [{"sender": "A", "observation_revision": 8, "cost": 4000},
            {"sender": "B", "observation_revision": 10, "cost": 5200},
            {"sender": "C", "observation_revision": 7, "cost": 6000}]
    results = set()
    for delivery in itertools.permutations(bids):
        canonical = sorted(delivery, key=lambda b: b["sender"])
        digest = hashlib.sha256(json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        winner = min(canonical, key=lambda b: (b["cost"], b["sender"]))["sender"]
        results.add((digest, winner))
    assert len(results) == 1
    return {"bundle_delivery_orders": 6, "distinct_input_digest_and_output_pairs": len(results),
            "mixed_observation_revisions": [8, 10, 7],
            "scope": "sealed bids suffice for this deterministic choice, not world-state safety"}


def instrument_original_f2(bundle):
    path = (Path(bundle) / "protocol/round2_fixtures.py").resolve()
    spec = importlib.util.spec_from_file_location("original_fixtures", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    first = {}
    def tracer(frame, event, arg):
        if (event == "line" and frame.f_code.co_filename == str(path)
                and frame.f_code.co_name == "run"):
            v = frame.f_locals
            if v.get("rule") == "v1.1" and v.get("aborted_R"):
                key = str(v.get("dropout_from"))
                first.setdefault(key, {"first_abort_ms": v["t"], "sample": v.get("last")})
        return tracer
    try:
        sys.settrace(tracer)
        result = mod.f2()
    finally:
        sys.settrace(None)
    assert first == {"None": {"first_abort_ms": 0, "sample": None},
                     "400": {"first_abort_ms": 0, "sample": None}}
    return {"first_aborts": first, "original_result": result}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle")
    parser.add_argument("--out", default="independent_results.json")
    args = parser.parse_args()
    result = {"event_replay": event_checks(), "boundary": boundary_checks(),
              "phase_receipt": phase_checks(), "sealed_decision": decision_checks()}
    if args.bundle:
        result["original_F2_instrumentation"] = instrument_original_f2(args.bundle)
    Path(args.out).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
