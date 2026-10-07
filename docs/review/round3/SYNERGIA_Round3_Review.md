# SYNERGIA — Codex round 3

7 October 2026. Review of Opus round 2, the proposed v1.1 PDF, and the newly supplied `SYNERGIA_v1.1_probe_bundle.zip`. Starting review-branch head: `a934f409671269212a33e0e51281bf5f8d818851`. This review does not ratify the baseline or validate the project implementation.

## Decision

Keep the proposed architecture and UC1–UC3 scope. Accept the revised round deadline, conservative ownership/release policy, canonical decision bundle, and corrected claim labels. Withdraw Codex's earlier suggestion that all observation revisions must match: identical frozen decision inputs are sufficient for deterministic agreement.

Two specification repairs remain necessary: execution-event gap recovery and PHASE receipt/retry semantics. The inactive boundary needs a precise persistent-freeze lifecycle, which is consistent with C11 rather than a new architecture. Correct the governor evidence before using it to support controller claims. Then proceed to small implementation gates; another broad baseline rewrite is unnecessary.

| Round-2 item | Round-3 disposition | Remaining work |
|---|---|---|
| R2-01 cooperative phase safety | Partly resolved: old physical bound withdrawn; governor remains proposed | Repair PHASE acknowledgments; replace invalid F2 evidence; implement and test the stated controller |
| R2-02 execution-event retrieval | Not closed | Distinguish producer streams, received maximum, contiguous applied watermark and missing ranges |
| R2-03 two-leg round deadline | Specification accepted under stated bounded-loss assumptions | Run staggered joins in the actual implementation; 600-run bundle remains v1.0 |
| R2-04 inactive boundary/release | Accepted with persistent-freeze clarification | Bind boundary lifecycle and graph/epoch fencing; test real release evidence |
| R2-05 canonical inputs | Accepted, including unequal observation revisions | Correct the monotonicity explanation; implement sealed inputs and deterministic replay |
| R2-06 claims/validation/fencing | Direction accepted | Field-specific validation and actual adapter/invariant tests |

## 1. What was actually reproduced

All 36 entries in the bundle's `SHA256SUMS` match. Original files were preserved; runs used a separate copy. Host interpreter: Python 3.12.14; supplied environment records Python 3.12.3.

| Evidence | Result here | What it establishes |
|---|---|---|
| Original `protocol/round_model.py` | 600 runs; stdout byte-for-byte equal to supplied output | Reproduction of this v1.0 synthetic model and its assertions |
| Original `protocol/round2_fixtures.py` | All ten JSON fixture results exactly equal | Reproduction of these small fixtures, including their limitations |
| Independent event storage check | 720 permutations of six events, each followed by reverse duplicates | Ordered per-producer storage converges in this finite model |
| Independent boundary check | 44 reachable aggregate states, 104 transitions; no unsafe installation | Persistent-freeze lifecycle works under the abstraction's assumptions |
| Independent sealed-input check | Six delivery orders, one canonical digest/output pair despite unequal observation revisions | Determinism for the modeled choice |
| Original F2, instrumented without modifying source | Both v1.1 variants abort at t=0 with no pose sample | The 5 mm outcome is confounded by immediate startup abort |
| MuJoCo toys | Not run here | Reported numerical physics outputs remain Opus's results |
| Reference compiler/validator | Source inspected; not run here | No independent confirmation of its output or fixture counts |

Pinned `mujoco==3.15.0` and `jsonschema==4.26.0` could not be obtained in this runtime; both install attempts returned “No matching distribution found.” This does not establish that these versions are unavailable elsewhere. Do not silently substitute versions and call that exact reproduction.

The reproduced campaign reports 100/100 completion for nominal, lossy, heavy-loss and transient-partition profiles, and 0/100 for crash and permanent partition. These are six toy tasks and the script's own model definitions. Its I1/I2/I3 labels must not be read as verification of the baseline's complete implementation invariants. The bundle explicitly retains v1.0's 500 ms bid deadline. This campaign is distinct from Codex's earlier independently written 600-run round-control model.

Machine-readable details are in `reproduction_results.json` and `independent_results.json`. The independent script documents its abstractions. It does not model a real transport, production task reducer, authenticated provenance, controller, or physical release. Zero actuation during its replay is a property of a storage model with no actuator callback, not a tested production fence.

## 2. R3-01 — execution streams must detect holes and preserve origins

**Source:** v1.1 §2.3, C8–C10; bundle `protocol/round2_fixtures.py::f3`.

C9 requests events only when another replica advertises a higher received sequence. Consider a producer with PREPARED(1), COMPLETE(2), RELEASED(3). Replica A stores all three. B stores 1 and 3 but misses 2. Both advertise maximum 3, so the higher-mark trigger never fires. If B buffers 3 to enforce transitions, it stays stuck; if it discards 3, a contract that advertises highest *received* still hides the hole. Defining a different watermark could fix this, but the current rule does not do so.

Coalitions add a second issue: C8 lets each executor start its instance sequence at 1. C10's deduplication includes sender, but C9's watermark and request identify only the instance. A relay's transport sender is also different from the original producer. F3 uses `(instance, seq)` keys and one producer, so it cannot detect either ambiguity.

**Minimal replacement contract:**

1. Stream identity is `(run/epoch, instance, original_executor)`. Event identity adds `seq`; relay identity never replaces original executor identity.
2. Store validated out-of-order events. Track both the largest stored sequence and the highest contiguous applied sequence for each stream. Retain missing ranges above the contiguous prefix.
3. Advertise enough per-stream information to discover a missing tail. Request known holes even when local and remote maxima are equal. Specify `EVENT_REQUEST(stream, missing_ranges)` or a contiguous-prefix request with duplicates allowed.
4. Any holder returns the original envelope. Check that the producer is an authorized role holder for that instance. Conflicting content for one event identity is a protocol fault, not a harmless duplicate.
5. Apply events in per-producer order to a defined task/coalition reducer. COMPLETE and FAILED describe outcome; neither substitutes for every required RELEASED. Historical replay updates evidence only and never schedules old actuation. A delayed event from an earlier attempt cannot overwrite the current attempt's ownership.
6. Keep retry rate bounds and fail-closed termination if no holder can supply the gap. No repair rule may synthesize missing release evidence.

The independent check reproduces the hidden hole, repairs it from a holder, retains six events from two producers rather than three colliding keys, and enumerates all 720 delivery orders with duplicates. This supports the storage correction; a real reducer and fault-injected transport remain an implementation gate.

## 3. R3-02 — same phase does not acknowledge a particular PHASE event

**Source:** v1.1 §2.2, C1–C4; bundle F2 and `physics/beam_probe_v11.py::run`.

Concrete trace: L sends P1-done(seq=2), which is lost. R's P1-entered(seq=1) reaches L. C2 allows L to stop retries because R is in the same phase. This does not establish receipt of L's done event. A duplicate entered event can have the same effect. C1 also rejects non-current phases while C2 relies on observing later phases, leaving the acknowledgment path ambiguous. Phase deadlines may safely abort; reliable progress is not established by these rules.

**Correction:** acknowledge the particular `(instance, producer, phase_seq)` received, or use the repaired durable event stream to recover it. Retain/retry outstanding gate evidence until explicit receipt or the defined expiry/abort path; changing local phase must not silently lose evidence the peer still needs. Separate storing valid historical phase evidence from accepting a message as a current motion command. Validate the instance and deadline, prevent state regression and reactivation, and define what late done evidence may satisfy. Same-phase or later-phase observation alone is not a receipt acknowledgment.

This does not make cooperative start atomic under arbitrary loss. Keep the independent local guards and fail-closed deadlines. Test entered delivered/done lost, reversed deliveries, a phase transition before peer receipt, and expired evidence after abort.

### F2's 5 mm result is not evidence for C5

The executed F2 function initializes an empty observation queue with 20 ms latency. At t=0, `last is None`, so it sets `aborted_R=True` permanently. This happens both with and without the later 400 ms dropout. The right reference immediately lowers from h1; the result cannot demonstrate continuing P2 under the revised governor. An execution tracer confirmed both first aborts at t=0.

F2 also implements the discarded reference-cap rule, `min(target, partner_observation + lead)`, not C5's observed-separation feedback, and still uses a 300 ms gate. Keep its v1.0 counterexample. Withdraw the claimed v1.1 governor confirmation. Replace it with initialized valid observations, the actual C5/C6 rule, and logs confirming that motion and dropout occur in the intended phases.

### The MuJoCo toy is informative but does not implement C1–C7

Source inspection finds these material differences:

- PHASE transport/retries are absent; nominal peer gates are assumed delivered.
- P1 completion uses the reference reaching its target and elapsed time, not observed end height plus the specified 100 ms force-band dwell.
- The asymmetric wait uses 0.3 + 0.2 seconds since P1 entry, not the normative 400 ms after reaching h1.
- The separation governor runs in P1–P3, omitting P4. The early abort branch lowers and `continue`s before the governor and guards, contrary to governed P2–P4 abort lowering.
- No acceleration clamp or the stated phase deadlines are implemented.

The reported 3.078° → 0.318° comparison therefore remains a one-case toy result for the supplied controller, not verification of the normative controller. The phase-relative RMS calculation truncates to the shorter phase trace; it is not a full time-aligned trajectory comparison. Keep transition times, duration differences and omitted tails visible in refinement reports.

The 10.5 mm arithmetic is correct: `3 + 2*25*(40+100+10)/1000`. Its status should be **proposed envelope awaiting derivation and matching tests**, not an established general bound. Define initial separation, observation timestamp age, tracking assumptions, acceleration-limited reversals, stale-hold duration, saturation, and abort behavior. Neither F2 nor the toy demonstrates that envelope for C1–C7. No physical tilt bound is accepted.

## 4. R3-03 — preserve the inactive boundary until it is consumed

**Source:** v1.1 §2.5 C11–C13; F4/F5.

C11 already says to freeze new rounds and resolve started rounds. That addresses the earlier conceptual defect. F4 is a predicate test; it does not establish the lifecycle around endorsement. Spell out the existing intended freeze:

- Boundary rounds are a distinct control operation allowed while ordinary allocation is frozen. Drain every prior round; drain the work/reservations resulting from a late resolved award before endorsing inactivity.
- Each endorsement is tied to one boundary identifier, old graph, epoch/membership, prior closure and release evidence. Freeze persists after endorsement and after certificate formation while the proposed graph is generated/validated.
- Bind the eventual installation to that boundary and the agreed new graph hash. Release the freeze only through a mutually agreed installation or cancellation/closure. A missing member blocks; a local timeout does not thaw allocation.
- An old certificate or delayed activation cannot reopen a resolved instance. The adapter checks active graph/epoch and the exact current held instance; resource release remains evidence-based.

The independent aggregate-state model explores 44 states and 104 transitions with no unsafe installation under these rules. It assumes truthful quiescence and correctly shared state; it is not a distributed-knowledge proof. Its snapshot-only counterexample is a warning about prematurely thawing, not a claim that C11 explicitly permits thawing. Test delayed certificates and disagreement in the real replicas before treating the boundary as implemented.

C12's all-holder release plus stable-support condition is retained. C13's no timeout-based release is retained. A supervised reset ends the run; it is not an in-run ownership-transfer shortcut.

## 5. Observation revisions: accept Opus's conclusion, correct its reason

Equal observation revisions are not necessary for deterministic Decide when all agents use the same canonical bundle containing the same frozen per-sender bids. Codex retracts the stronger suggestion. Mixed observations affect the quality/freshness of a bid, not replica agreement when the complete inputs are identical.

However, “a lagging observation can only remove options” is too strong. Observation-derived travel duration can increase or decrease; geometry can change an eligibility or role decision; a stale ready/free view can still contain an option that has become invalid. Intersection is conservative relative to the supplied sets, not necessarily relative to the current world. Failure-history union has a different, append-only meaning.

Use this replacement rationale: costs, eligibility results, role choices and any decision-relevant geometry must be frozen into bid sets or other identified immutable bundle content; Decide may not reread mutable local observations. Hash equality identifies the same static belief/configuration content but is not itself a freshness test. Reservations, origin-valid release evidence, and fresh executor prechecks provide the separate safety controls. The six-order independent fixture confirms only the deterministic-choice part.

## 6. Other dispositions and next implementation gates

The deadline arithmetic is accepted under the declared delivery/computation bounds: two 320 ms legs plus two 20 ms computation allowances give 680 ms; 800 ms leaves 120 ms. Random loss gives no deadline guarantee. This must be exercised with v1.1 in the actual runtime.

Retain corridor resources, the same-scene serialized concurrency comparison, separated analytic/controller/pipeline labels, and repeated language grounding tests. Validate numeric ranges per field: negative bid durations are invalid; a blanket ban on every negative number would incorrectly reject signed poses. The F9 equality loop is a single function called repeatedly, not an independent implementation comparison. Keep validation and fencing claims at their actual scope.

The 592-hour arithmetic is accepted as an estimate, not evidence of feasibility: five people over twelve weeks with 25% reserve need about 13.2 gross hours/person/week. Availability, faculty acceptance of fail-closed behavior, title, hardware requirement and actual dates remain Ani-owned decisions. No new scope reduction is assumed.

Proceed in this order:

1. **Protocol slice:** three private replicas, actual serialized messages, sealed decision bundle, per-producer event repair, persistent boundary and adapter fencing. Inject interior holes, missing tails, reversed duplicates, silent producer with live relay, late old awards and phase receipt loss. Assert resource/instance invariants and no actuation from replay.
2. **UC1 vertical slice:** one live language goal through validation, allocation, physical action, observed completion/release and one safely released retry. This establishes integration, not decentralization.
3. **UC2 allocation/concurrency:** actual three-robot tasks, corridor contention, disjoint concurrency, failure/release recovery and the serialized baseline.
4. **UC3 physics gate before scoring:** implement the stated phase/guard/governor behavior and instrument every abort. Test initialized observations, asymmetric loss, active-phase dropout, noise, unequal pads and stalled actuators. Resolve P0/P5 timestep nonconvergence and model end-stop forces separately from actuator limits. Keep the admission/controller comparison fixed across alternatives.

The unavailable baseline source ZIP does not block these findings. It will help consolidate the final normative text, but the PDF and newly supplied probe source are sufficient for this review. Request one focused Opus patch and matching discriminating tests, then continue implementation. Keep PR #1 draft and unmerged.

## Evidence locations

All technical findings above derive from user-supplied v1.1 §2, Opus's round-2 reply, the checksummed probe bundle, and the accompanying executed checks. No new literature claim or external dependency-version claim is needed. Original uploaded documents and bundle source are not republished with this review.

Run independent checks with Python's standard library:

```sh
python3 independent_event_boundary_review.py --out independent_results.json
# Optionally instrument the supplied original F2:
python3 independent_event_boundary_review.py --bundle /path/to/SYNERGIA_v1.1_probe_bundle --out independent_results.json
```

Without `--bundle`, the original-F2 instrumentation section is intentionally absent. Reproduction records preserve the separate original campaign/fixture outputs and blocked dependencies.
