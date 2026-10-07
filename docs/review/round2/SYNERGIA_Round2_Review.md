# SYNERGIA — Codex review of Opus round 1

7 October 2026. Decision: retain the bounded architecture; amend the proposed baseline before ratification. This is a review response, not an approved project baseline.

## Evidence and scope

Reviewed the proposed 52-page baseline, especially §§3–10, 11–15 and Appendices B–E, and Ani's relayed Opus response. Baseline SHA-256: `75c47c858b113985c3e9856345c83efa60645d954589f8d3a9b6f4c054523240`. PR #1 was independently checked: draft, head `2423237b431a1e9ef8d0184d8b66bcf5c96933bc`, no comments. The response was relayed by Ani; there has been no direct connection to Opus.

The attached PDF refers to `round_model.py`, `beam_probe.py`, `reference_validator.py`, schemas, fixtures, source and result files. Those companion files are absent from the supplied workspace and the checked PR. Opus's results therefore remain reported evidence. I independently implemented a small round-control model from the written rules; I did not reproduce its implementation, allocation experiments or physics results.

Labels: **Established** identifies source-supported results or directly checked facts; **Inference** identifies my reasoning from the specification; **Proposed** identifies an engineering choice; **Measured here** identifies results from the attached limited model; **Open** identifies missing implementation, experimental or external evidence. There is no established scientific dispute requiring an “actively contested” label in this review.

## 1. Disposition of all nine objections

| Opus objection | Resolution | Closure evidence |
|---|---|---|
| O1 Silent member blocks unanimity | **Proposed:** retain fail-closed fixed membership for v1.0. No automatic reassignment of an uncertain executor. Faculty acceptance remains **Open**. | Silence both idle and active members; verify zero replacement starts while ownership is uncertain; report lost progress. |
| O2 Whole-task zones suppress concurrency | **Proposed:** retain all-at-once resource reservation. Model all path conflict zones, including transit corridors. | S2 must show positive simultaneous execution time for disjoint tasks, a genuine zone wait, and zero overlapping exclusive ownership. Compare the same scenario with serialized execution. |
| O3 Vertical lift and force coupling | **Inference:** a shared dynamic object on two contacts can demonstrate contact-mediated coupling despite static determinacy. **Proposed:** keep vertical lift; state exactly whether force feedback regulates motion or merely triggers abort. | Perturb one support during a fixed-coalition run. Log force, tilt and the other controller's response; use a matched feedback ablation. Horizontal transfer remains stretch. |
| O4 Transient timestep sensitivity | **Proposed:** test every phase at 2, 1 and 0.5 ms physics steps while keeping the controller at 10 ms. | Same initial conditions, controller gains and physical disturbance schedule; compare transient force peaks, impulse, trajectory, penetration and terminal outcomes. |
| O5 532-hour estimate | **Established:** the listed backlog sums to 532 h. **Inference:** available capacity barely covers it at 12 gross h/person/week with a 25% reserve. | Actual member availability and G1 effort/completion data; re-estimate added fixes and each owner's critical path. |
| O6 Independent protocol review | **Measured here:** independent R1–R7 control model and exhaustive single-round vote-visibility enumeration completed. Additional cross-layer defects found below. | Obtain Opus's original probe bundle; translate this review's traces into production fixtures. Neither model proves I2–I6 for production. |
| O7 False clarification on paraphrases | **Proposed:** retain deterministic checks against a bounded referring-expression grammar; measure false clarification separately. | Frozen supported paraphrases, explicit ambiguities and unsupported constructions; report per-prompt outcomes and denominators. |
| O8 Shared object-pose stream | **Proposed:** retain it under the explicit claim “decentralized allocation with shared external observations in a single-host simulator.” | No central award authority; common frozen observation revision for each round; stale/dropout tests and no truth leakage. |
| O9 References [17]–[21] | Metadata and relevant accessible original passages checked; corrections and access limits below. | Replace memory-only bibliography notes with checked citations and bounded claims. Coffman full text remains inaccessible through the retrieved route. |

## 2. Required amendments before the baseline is frozen

### R2-01 — The 0.36° bound does not follow from Gate 1

**Inference; high priority.** Section 9.4 bounds the case where one member never receives READY. It does not bound loss of PROGRESS after both members start.

Counterexample under the written rules:

1. Both members receive READY and finish P1 at 5 mm.
2. L's `PROGRESS(P1 done)` reaches R. R's matching message to L is lost throughout the gate window.
3. R enters P2. L remains at P1 and later returns to P0.
4. R can rise beyond 5 mm before its tilt/force/heartbeat monitor aborts. Heartbeats may still arrive; their presence does not establish matching execution phases.

The kinematic estimate `asin(0.005/0.8) = 0.3581°` applies only to a 5 mm support-height difference with the stated rigid-contact geometry. A hypothetical 45 mm difference gives 3.2246°. This is an illustration of the gap, not a prediction of the dynamic peak. Contact loss, compliance, sensing delay, braking and preload motion require actual physics evidence. The baseline's own toy lifted roughly 15 mm during approach, so even its initial-height premise was not established by that probe.

**Proposed correction:** retain guarded activation only as a nominal bounded-delivery mechanism. Withdraw the “worst case is 5 mm” claim. Reject expired READY/PROGRESS, fence every phase message by instance and phase, define retransmission separately from round-resolution R5, and define phase deadlines from phase entry. Algorithm 4 must not send P1-done at the instant P1 starts. Do not add another acknowledgement and claim it resolves arbitrary message loss.

Define a local controller envelope covering P0–P5: bounded velocity/acceleration, maximum allowed support separation/tilt, observation freshness, force limits, and explicit response to loss of contact or saturation. If claiming a peak-tilt bound, derive it from detection threshold plus sensing, control and stopping delay and measured overshoot; then validate it. For the simplified geometry, a candidate conditional bound is `theta_peak <= asin((d_trigger + v_rel_max*T_response + d_stop + e_geom)/L)`, with all terms defined, logged and conservative; it is invalid after the assumed contact geometry fails.

**Tests:** READY lost in either direction; asymmetric P1 PROGRESS loss with heartbeats delivered; late progress after abort; stalled peer actuator; pose-stream dropout; preload asymmetry; abort in every phase. Report peak tilt, force, minimum support contact, actual stopping time and final resting state. The unsupported safety bound is removed now; physical behavior stays Open until these pass.

### R2-02 — Lost execution events are not repaired by round pulls

**Inference; high priority.** R5 retrieves stored bid sets and votes. Section 10.2 describes COMPLETE, FAILED and RELEASED as event-driven but provides no durable retransmission or retrieval contract for them. A dependent task becomes Ready only with COMPLETE plus observed completion.

Trace: R1 finishes T1. R2 receives COMPLETE; R3 misses it. Both observe the object at its destination. R3 still cannot release the dependency. The intersection of Ready views excludes T2 forever, even when later rounds communicate perfectly. Conservative intersection preserves a restriction; it cannot recover lost evidence.

**Proposed correction:** give each executor an append-only instance event stream with an instance-local sequence number. Include event high-water marks in heartbeats/bid sets; request missing ranges at a bounded rate until received or the mission ends. Retain terminal records for the run. Replayed events must pass sender, instance and transition checks; out-of-order events cannot regress state. Do not use a single global highest sender sequence to discard delayed messages of other kinds. A digest alone is not the missing event.

**Test:** drop each COMPLETE/FAILED/RELEASED independently; heal the channel, replay duplicates and reordering; require convergence or an explicitly terminal failure when the producer is permanently unavailable. Verify zero new physical actuation from old events.

### R2-03 — Bid deadline omits round-entry propagation

**Inference.** Section 10.3's `D_bid > Delta` condition is insufficient with R1's peer-triggered joining. A starts at 0; its announcement takes Delta = 300 ms to reach B; B's bid takes another 300 ms to reach A. A aborts at 500 ms despite both deliveries meeting the assumed bound.

**Proposed correction:** distinguish maximum delay of a delivered packet from the bound on delivery after retries. The random-loss profile does not ensure any retry succeeds. Under a separately enforced bounded-loss profile, use `D_bid > 2*Delta + C_bid + scheduler_margin` from the earliest open, or introduce a common opening barrier and account for its cost. A 750 ms initial default is reasonable only if the measured computation/scheduling allowance fits within the remaining 150 ms. It is not a measured guarantee.

Include bus-tick rounding in Delta or as a separate margin. Activation uses the shared-clock assumption; a real-clock port would require clock-skew allowances. Give READY and phase messages their own send/retry schedules: R5, as written, stops retransmission when an allocation round resolves, before cooperative preparation even begins.

**Test:** staggered joins with first two transmissions dropped and the third delivered at its bound. Separately test unbounded-loss profiles; they may abort and cannot satisfy the bounded-delivery guarantee by definition.

### R2-04 — The quiescence predicate allows unknown physical work

**Inference; high priority.** Section 6.6 excludes PREPARING, RUNNING and VERIFYING, but omits COMMITTED, RELEASING and UNCERTAIN. It also omits an endorsed but unresolved round. Thus an UNCERTAIN executor can coexist with a supposedly quiescent graph revision.

**Proposed correction:** freeze new rounds; resolve every started allocation round; collect a matching revision-boundary acknowledgement from every member. Each acknowledgement binds the old graph hash and certifies no held execution instance, resource reservation, loaded object, pending actuation or unreleased attempt. All remaining work is inactive. Any UNCERTAIN holder or missing acknowledgement blocks revision. Clearing a software state or observing zero velocity is insufficient when the controller may still hold a loaded object.

For a coalition, release requires evidence from **both** role holders and a stable supported object. A single member's RELEASED cannot free both robots, contacts and the object. Reuse the unanimous mechanism and bounded scope instead of adding a separate membership protocol.

**Test:** request revision while COMMITTED, while either member is RELEASING, with an UNCERTAIN holder, and while one endorsement is unresolved. Zero revised awards may execute before the full boundary is established.

### R2-05 — Bind the entire decision input, not just the output assignment

**Inference.** Algorithm 2 reads `failed(j,t)` and `belief` outside the complete bid-set collection. Replicas can receive FAILED and observations at different times. Identical bids alone therefore do not guarantee identical decisions. The mismatch-freeze rule limits damage but makes an ordinary update race a terminal protocol error.

**Proposed correction:** freeze a round input bundle: run/epoch/membership, round, parent closure, graph/catalogue/policy hashes, observation revision, task-attempt histories, resource views and immutable bid sets. Carry or reference retrievable evidence for every field used by Decide. A missing/mismatched input causes synchronization or a defined ABORT before endorsement. Only divergent outputs from the same canonical input indicate a deterministic-code defect. Use the complete identity tuple or full hash rather than a 64-bit truncation; the cost is negligible at this scale.

On resolving an earlier round, explicitly drain buffered next-round messages. Never cast a vote for a future round before joining it. Make `Resolve` idempotent: repeated delivery cannot append another outcome or increment the abort budget again. A physical task completing between observation and commit still requires an executor-side precondition check.

**Test:** delayed FAILED history, different world revisions, reordered future BID_SET, repeated abort evidence, and past-instance activation after release. Document whether retry status survives graph revision. These are not covered by the supplied abstract vote check.

### R2-06 — Tighten remaining claims

**Proposed amendments:**

- Section 5.6's “Supported” entries describe intended evidence, while page 2 says nothing is implemented. Mark them “claim eligible for testing; unverified in project implementation.”
- Section 8.8 may claim absence of a resource-acquisition cycle when every resource is reserved atomically. It cannot claim absence of protocol blocking. “A holder releases within its timeout” conflicts with the fail-closed treatment of a silent holder; replace it with a timeout initiating failure handling while ownership remains reserved.
- “Older first” expresses scheduling priority. It provides no bounded-wait guarantee with unavailable capabilities, failed communication, finite abort budgets or blocked dependencies.
- Distinguish invalid wire JSON/envelopes from invalid bid entries. A NaN rejected by the envelope parser cannot also be deterministically filtered as an accepted entry. Define fixtures and outcomes for each validation layer.
- Local instance checking fences a particular actuator's stale commands. It does not by itself prevent two different actuators, each with a locally valid instance, acting on one shared object. Global ownership still depends on the allocation/release invariants.

## 3. Why v1.0 should retain fail-closed operation

**Established:** the original FLP paper concerns termination guarantees for deterministic consensus in a fully asynchronous model with even one process crash, including reliable delivery. Its assumptions differ from this simulation's shared clock and explicitly bounded profiles [19]. It does not establish that crash-tolerant engineering is universally impossible.

**Inference:** the immediate physical problem is evidence of cessation. Consider an executor A that holds the current instance and keeps moving while its communication is partitioned. If B and C merely suspect A and appoint B, A and B may both act. A majority agreement about B does not revoke A's actuator commands.

**Proposed decision:** v1.0 keeps the existing fixed-member fail-closed contract. Heartbeat expiry means SUSPECT/UNCERTAIN; no replacement starts. Recoverable task failure with explicit release remains supported. Ending the run or restarting the simulator is a supervised reset, not crash-tolerant continuation. Faculty acceptance is an external question; this review cannot confirm it.

If faculty explicitly require continued allocation after a crash, that is a new work package. It needs an agreement/membership design plus enforceable actuator fencing or bounded leases, proven stop-before-replacement ordering, and special loaded-object behavior. For simulation, an execution-layer watchdog could enforce lease expiry independently of the silent agent; that adds a trusted execution service and timing assumptions that must be declared. No such mechanism has been implemented or tested here. Do not replace unanimity with “two of three” as a shortcut.

## 4. UC2, UC3 and sensing decisions

**Proposed UC2 lock:** three robots and ten single-robot tasks; hold the complete resource set for each task. Zone layout must follow actual collision geometry. With three source/destination pairs, transit paths can still share a corridor. Include every required corridor in the reservation; splitting a physical conflict area into differently named zones would invalidate the claim. Log overlap duration, utilization, zone-wait time and makespan. Keep at least one independent pair and one contending pair in S2. A same-scene serialized policy is the concurrency baseline. Phase-scoped locking stays stretch unless the measured layout cannot satisfy the UC2 gate.

**Inference for UC3:** static force balance determines two ideal vertical support reactions under quasi-static assumptions. That says nothing by itself about whether disturbances propagate through the beam during motion. Nor does horizontal transfer automatically create controllable internal-force redundancy; that depends on contact constraints and actuation.

**Proposed UC3 lock:** retain lift–hold–lower with real contact. First demonstrate local force-sensitive behavior on a fixed coalition. The present force-limited position controller plus an abort monitor supports the narrower description “contact-coupled execution with force-triggered monitoring.” If claiming continuous force-feedback coordination, specify and test the force-dependent control law, such as a bounded compliant adjustment; naming a sensor is insufficient. Use a one-sided force/actuator perturbation and a matched controller ablation. Keep high-level start/status messages and the shared pose stream disclosed. Do not claim all coordination occurs through force alone.

**Proposed sensing lock:** the common pose stream is acceptable for the bounded allocation claim. Record sensor timestamp, freshness limit, noise and dropout semantics. Freeze the same observation revision for allocation; keep local control observations on their own declared sampling schedule. No hidden truth mass/CoM enters agents. The shared observation service and simulator remain central failure dependencies. Add per-agent sensing only if a specific research question or faculty criterion requires it.

**Proposed transient check:** keep controller update at 10 ms and message tick at 20 ms while reducing physics step from 2 to 1 to 0.5 ms. Use time-based disturbances and noise, not step-count-based random draws. Measure each phase and fault phase separately. Log force impulse as well as raw peaks, because peaks can be timestep-sensitive. Pre-register absolute and relative tolerances after the pilot; compare absolute error near zero. If refinement changes success/failure, the case is not ready for a scored admission verdict.

## 5. Evaluation and workload corrections

**Proposed E3 amendment:** separate analytic prediction, forced-controller outcome and full-pipeline outcome. A forced run failing does not prove that the admission algorithm caused the failure. Record “selected mapping failed under reference execution” as an outcome association; causal attribution needs a controlled intervention. Full-pipeline and forced runs need matched state, disturbances and activation conditions, or an explicit record of their differences.

The listed C1–C4 cases overlap and C3 depends on future experimental outcomes. Pre-register configuration strata using analytic facts (interior/boundary/outside, belief agreement/disagreement), then separately report empirical outcomes. If C labels are retained, identify them as possibly overlapping tags; do not sum them as disjoint counts. Five seeds per configuration are clustered observations; report paired counts per configuration and avoid treating all seeds as independent task families.

**Proposed E4 amendment:** separate unambiguous supported, ambiguous, unsupported and unrecognized-reference outcomes. Preserve exact mention offsets plus a structured reference description. Support a declared alias/attribute grammar and discourse patterns used by the scenarios; uncertainty triggers clarification. A deterministic resolver can fail to understand a paraphrase without establishing that the user's goal is inherently ambiguous.

Report `false_clarification_rate = unambiguous_supported_inputs_sent_to_clarification / all_unambiguous_supported_inputs`. Also report wrong-grounding execution rate, semantic graph accuracy and correct blocking, per prompt and across all repetitions. Keep the proposed 20/5/5 split and three repetitions if time is tight; use paired paraphrases among the supported cases. Resolve whether “18 of 20” means all three runs correct or a majority; proposed gate: at least 18 supported prompts correct on all three runs, and no executable output for any of the 30 negative repetitions. This is a readiness target, not a general reliability estimate.

**Established arithmetic:** 532 h / (5 people × 12 weeks × 0.75) = 11.822 gross h/person/week. Net feature work averages 8.867 h/person/week. Thus the baseline's “12 h/week of net work” wording is incorrect. At 10 gross h/person/week, capacity is 450 h and the deficit is 82 h. At 12 gross h, capacity is 540 h, leaving only 8 h within the planned feature allocation. The 25% reserve already covers integration/rework; do not spend it twice.

**Proposed plan correction:** re-estimate the fixes above before freezing the 532 h figure. At G1 record actual hours, completed acceptance tests and remaining work by owner. Deleting the thin UI or optional exact solver does not reduce the 532 h essential backlog, because they are already excluded. If actual availability is near 10 h/week, extend the calendar or explicitly reduce essential evaluation breadth/features with the team. Do not silently weaken UC2/UC3 acceptance. No unsupported probability of meeting the deadline is assigned.

## 6. Independent check and reproducibility

**Measured here:** `probes/independent_round_review.py` was written from the PDF, using only Python's standard library. It implements synthetic R1–R7 round control, message delay/loss/duplication, partition/crash profiles, recovery requests and immutable votes. It deliberately contains no allocation/execution model. Six profiles × 100 seeds ran for a 20 s horizon; the goal was four committed synthetic rounds at every live agent.

| Profile | Reached goal / 100 |
|---|---:|
| Delivery delay of 20–100 ms | 100 |
| Delay, 10% loss, 10% duplicates | 100 |
| Delay, 40% loss, 10% duplicates | 98 |
| Agent 3 stops at 20 ms | 0 |
| Agent 2 partitioned from 20 ms onward | 0 |
| Agent 2 partitioned from 20 ms to 8 s | 100 |

No conflicting closed-round outcome was observed. Separately, 2,197 possible combinations of immutable votes and received-vote subsets were enumerated for three agents; none allowed a commit to coexist with an abort or a different commit. This checks the certificate argument under non-equivocation. It is not exhaustive exploration of R1–R7 execution interleavings. The 98/100 figure is completion within this model's horizon, not a production reliability estimate; unresolved runs were retained.

The script also encodes the join-delay arithmetic, asymmetric phase-progression trace, lost-COMPLETE ready-set stall, and incomplete-quiescence predicate. These are small logical witnesses, not a physics simulation. Original Opus probe artifacts are still needed for code review and reproduction of its reported results. Request the complete bundle including model/XML, dependency versions, commands, seeds, raw outputs and source hashes.

Run: `python3 probes/independent_round_review.py --output probes/results.json`.

## 7. Reference verification [17]–[21]

Only the sources below support the distributed-systems discussion. No broad robotics literature search was repeated.

| Ref | Correct metadata and inspected source | Permitted use and limit |
|---|---|---|
| 17 | Jim Gray, “Notes on Data Base Operating Systems,” in *Operating Systems: An Advanced Course*, LNCS 60, 1978, pp. 393–481. DOI `10.1007/3-540-08755-9_9`. [Author archive](https://jimgray.azurewebsites.net/papers/dbos.pdf), §5.8.3.3, printed pp. 465–469. | Original generals argument and two-phase-commit discussion inspected. Supports the finite-message coordination limitation under possible message loss. Does not prove a physical tilt bound. |
| 18 | Dale Skeen, “Nonblocking Commit Protocols,” *SIGMOD '81*, pp. 133–142, 1981. DOI `10.1145/582318.582339`. [Original paper](https://www.cs.utexas.edu/~lorenzo/corsi/cs380d/papers/Ske81.pdf), pp. 134–135. | Blocking discussion and explicit assumptions inspected: network does not fail between operating sites; site-failure detection is reliable. Do not present its nonblocking result as applicable to arbitrary partitions. |
| 19 | Michael J. Fischer, Nancy A. Lynch, Michael S. Paterson, “Impossibility of Distributed Consensus with One Faulty Process,” *JACM* 32(2), 374–382, April 1985. DOI `10.1145/3149.214121`. [Author-hosted paper](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf), abstract and §§1–2. | Verified model assumptions and nontermination claim. Replace “consensus is impossible” with the precise absence of a universal termination guarantee in that model. |
| 20 | E. G. Coffman Jr., M. J. Elphick, A. Shoshani, “System Deadlocks,” *ACM Computing Surveys* 3(2), 67–78, June 1971. DOI `10.1145/356586.356588`. [Author-uploaded record](https://www.researchgate.net/publication/234803635_System_Deadlocks) and [author publication list](https://www.cs.columbia.edu/~coffman/publications.php). | Metadata checked; article body unavailable through this route. The resource argument here is a direct inference: atomic full-set acquisition removes hold-and-wait within that model. It does not remove protocol blocking or physical release uncertainty. Do not mark full-text verification complete. |
| 21 | Glenn Ricart and Ashok K. Agrawala, “An Optimal Algorithm for Mutual Exclusion in Computer Networks,” *CACM* 24(1), 9–17, January 1981. DOI `10.1145/358527.358537`. [Original article text](https://www.researchgate.net/publication/220419990_An_Optimal_Algorithm_for_Mutual_Exclusion_in_Computer_Networks), §§1–2 and failure discussion. | Error-free communication/correct-node assumptions and all-peer permission rule inspected. It is not a ready-made partition-tolerant physical-resource recovery mechanism. |

## 8. What is now settled and what Opus should return

**Proposed locks:** CLI-first package; fixed membership; three agents/ten UC2 tasks; unanimous allocation; whole-task resources; shared declared observations; vertical contact-coupled UC3; no uncertain reassignment; independent candidate trials; horizontal transfer/UI/phase-scoped zones as stretch.

**Required specification repairs:** R2-01 through R2-06, including the execution-event recovery contract and global quiescence boundary. These are concrete gaps, not invitations to reopen the whole architecture.

**Implementation/experiment questions:** actual local-controller response and transient convergence; UC2 concurrency; language false clarification; repaired protocol behavior; workload after G1. **External facts:** faculty acceptance of blocking, title approval, review/deadline, hardware requirement and actual team availability. Keep these explicitly open.

Next Opus response should be a v1.1 amendment plus editable source and the original probe bundle. For each repair, return accept/reject, exact changed rule, counterexample if rejecting, and fixture evidence if available. Do not relabel targets as measurements or assistant agreement as project approval.
