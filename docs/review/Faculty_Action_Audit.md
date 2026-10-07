# SYNERGIA: faculty action audit and proposed decision baseline

7 October 2026 · ChatGPT/Codex review round 1 · Prepared for Ani and Opus

## 1. Verdict and evidence boundary

**Our extrapolation:** The project is ready to freeze a bounded design, but it is not yet ready to claim implementation feasibility or completed use cases. Adopt the lean direction in the new engineering review. Replace the old centralized SRS sections. Define the distributed protocol, execution boundary, failure semantics, and acceptance tests before expanding the software.

**Documented facts:** The corrected project definition fixes the three-stage progression and requires runtime coalition formation plus force-coupled execution in UC3. The new working reference explicitly describes release criteria, not completed work. The new engineering review explicitly labels its changes as untested recommendations. A live GitHub inspection on 7 October found `aniruddhab009/synergia` accessible, public, and empty before this review was added. That establishes the state of this repository, not the absence of code elsewhere.

**Status vocabulary:** `Retain` means consistent with the current scope; `Replace` means contradicted or defective; `Proposed lock` means a concrete engineering choice offered for the next baseline; `Verify` means implementation evidence is required; `External` means only the team or faculty can supply the fact. None means implemented. Established principles, documented facts, and our extrapolations are distinguished below. No issue is labeled actively contested research merely because two project documents disagree.

### Source precedence and reading scope

1. Current faculty action points and the user's current instructions.
2. `FINAL_SYNERGIA_PROJECT_DOCUMENT_CORRECTED(2).pdf`, especially §§3–7: current research boundary.
3. `Synergia_Blueprint_Engineering_Review_STE.pdf`, §§2–8: latest simplification proposal, subject to this audit.
4. `Synergia_Workbench_Working_Reference_STE.pdf`, §§3–10, and `Synergia_Final_Product_Blueprint(1).pdf`, §§4–13: product and evidence requirements.
5. Older SRS, synopsis, project-state, work-distribution, implementation design, architecture and WBS: historical designs and reusable detail, subordinate where they conflict.

The corrected definition, blueprint, and both new STE documents were read in full. Relevant older requirements, schedule, conflict registers and architecture headings were inspected to trace disagreements; the entire historical literature corpus was not independently re-audited. New external checks cover collaboration tooling and the proposed simulator's documented capabilities. This is an engineering audit, not a new systematic literature review. The earlier standalone mission/interfaces packet cited by the blueprint was not supplied; its algorithms and 36 analytical labels cannot be treated as verified artifacts here.

### Consequential contradictions

| Source | Conflict | Disposition |
|---|---|---|
| Old SRS §2.5 C3, C4; §4.6 REQ-46–50 | Excludes coalitions; uses a permanent central auctioneer | Replace for the current UC1–UC3 scope. Retain only as historical design or an explicitly labeled centralized comparison. |
| Old SRS C2 | LLM may run only before execution | Replace with bounded, event-triggered task-graph revision at a quiescent boundary; ordinary reassignment stays deterministic. |
| Old work distribution §0.1 K7–K8 | Removes dependency graph and coalition fields | Superseded by corrected definition §§4.2, 6.2–6.3. Restore both. |
| Old scope and stack | Scout survey, probe lift, ROS/Gazebo, navigation and perception dominate the build | These are not prerequisites of the refined project. Supplied world facts are permitted. |
| Working reference §8 and blueprint §8 | UC3 described as mandatory | Keep as the full-project target; distinguish faculty's guaranteed UC1 floor from full-project completion. |
| Synopsis §4 | 26-week schedule, probable completion 31 March 2027 | Historical planning evidence; current review date and available weekly effort remain unconfirmed. |
| Work distribution §E | Relative 30-week plan | Do not combine with the synopsis as though the schedules agree. Rebaseline. |

## 2. Every faculty action point

All recommendations in the last column are **our extrapolation**, not faculty-approved decisions.

| # | Faculty point | What exists / status | Required closure and evidence |
|---|---|---|---|
| F01 | Clear title | Several competing titles; suggested title is suitable | Use **SYNERGIA: Decentralized Task Allocation for Cooperative Multi-Robot Systems**. Describe language and simulation in the abstract. |
| F02 | Precise problem, boundary, assumptions, outcomes, exclusions | Corrected definition describes integration, but its technical statement is a topic list | Adopt the problem statement in §3 and its bounded model. |
| F03 | Lock UC1, UC2, UC3 | Stage identities are fixed in corrected §6 | Freeze scale, required behavior, and exit tests in §4. |
| F04 | Functional requirements | Corrected §7 lists functions; old SRS has detailed but conflicting requirements | Replace with atomic, testable FRs in §10. Map each to owner, stage, interface and test. |
| F05 | Non-functional requirements | Old SRS has numeric targets for a different stack; latest review has few numbers | Use candidate targets in §11, benchmark on the actual host, and freeze before scored trials. |
| F06 | End users / stakeholders | New documents identify students/researchers and reviewer | Primary operator: a robotics student/lab researcher. Testable initial user: a non-author teammate. Faculty are acceptance stakeholders; industry deployment is unvalidated. |
| F07 | Feasibility; essential vs stretch; UC1 floor | Lean design helps; no working implementation supplied | Deliver UC1 first while prototyping fixed-coalition control in parallel. UC2 is necessary to substantiate multi-robot decentralization. UC3 completes the cooperative target. |
| F08 | Timeline, milestones, risks, backup, dependencies | Several incompatible relative plans | Use §13 as a conditional calendar plan. Actual deadline, effort and hardware acceptance remain external facts. |
| F09 | Definition of decentralization | Agent-only award authority is stated | Add formal information/authority boundaries, fixed membership, replicated decisions, and fail-closed behavior in §§5–7. |
| F10 | Robot vs agent | Used inconsistently across generations | Robot = modeled physical mechanism. Robot agent = software decision-maker associated one-to-one with a robot. LLM = task compiler, not a robot agent. |
| F11 | Messages, transport, rate, delay/loss | Earlier ROS contracts exist for another architecture | Select local serialized message queues with fault injection; define envelopes, message families and timing in §7. Do not claim deployed network robustness. |
| F12 | Prompt pipeline and ambiguity | General pipeline fixed | Validate both structure and meaning; clarification creates no executable tasks; bounded repair and explicit offline fallback in §8. |
| F13 | LLM output fields | Historical schemas disagree | Versioned JSON graph, closed skill catalogue, role requirements, dependencies, resources, concurrency and named completion predicates. No invented capabilities or actuator code. |
| F14 | Bidding rule and exceptional cases | Hard filtering and costs are agreed; algorithm unselected | Use bounded, all-peer deterministic greedy allocation as a baseline; §6 specifies cost, ties, commitment, and unresolved activation proof obligation. |
| F15 | Task board authority and failure | Shared representation stated; old central board conflicts with peer authority | One logical board replicated inside agents; display is a derived view. No database/launcher winner selection. |
| F16 | All failure types | Broad failure lists exist; guarantees overreach | Adopt §9 matrix with detection, response, termination and test for every case. |
| F17 | Decentralized decision loop | Described at architectural level | Implement observe → validate local state → eligible set → bids → peer agreement → prepare → execute → verify → update → bounded recovery. |
| F18 | End-to-end implementation | No runnable evidence in supplied repository | One command, live goal, validated graph, one-agent bid/commit, physics execution, observed completion, saved report, then one recovery injection. |
| F19 | Immediate pre-review priorities | All can be drafted now; some cannot be confirmed by reasoning | Freeze title/problem/scope/protocol contracts; build UC1; run UC3 control spike; obtain review date and explicit faculty hardware criterion. |

## 3. Proposed project statement and boundary

**Proposed lock — title:** SYNERGIA: Decentralized Task Allocation for Cooperative Multi-Robot Systems.

**Proposed problem statement:** A heterogeneous robot team must convert a supported human goal into executable work and decide which robot, or robot pair, should perform each subtask while respecting capability, dependency and shared-resource constraints. SYNERGIA will implement a local experimental system that converts natural-language goals into validated task graphs, lets robot agents determine assignments through message-based bidding without a permanent central allocator, and monitors execution in a physics simulator. Its final stage selects a two-robot coalition at runtime for a shared-object manipulation task and evaluates the resulting motion and forces. The system assumes a known, bounded workcell, supplied object properties, a finite skill catalogue and configured robot models. It produces inspectable assignment traces, execution outcomes, bounded recovery behavior and reproducible comparisons. Autonomous environment discovery, arbitrary robot support, unrestricted language instructions, loaded coalition replacement, production fleet operation and guaranteed recovery from arbitrary failures are outside the first release.

**Proposed lock — concrete physical family:** A modeled tabletop/planar workcell, with force-limited robot mechanisms and short, predefined transfer/lift motions. Use the same model family for individual light-object moves and a two-contact cooperative beam/tray lift and short transfer. A minimum UC3 task may lift, hold and lower a supported shared object; explain the narrower motion envelope. A rigid body must respond dynamically to robot forces. Do not prescribe object motion kinematically. Robot capabilities differ through actuator limits, reachable contacts and supported skills; arbitrary commercial robot models are unnecessary.

**Proposed lock — operating envelope:** UC1: one robot and one mission. UC2: three robots and four to six allocatable subtasks, each requiring one robot. UC3: three candidate robots, exactly two distinct role holders for one shared-object task, with at least two physically possible candidate role mappings before capability/admission filtering. One mission and one cooperative object at a time. A protocol-only scaling test may use six agents and twenty tasks. These are design bounds chosen to exercise the required decisions, not measured limits.

**Proposed lock — software:** Python, one CPU physics backend, YAML scenarios, JSON contracts, per-producer JSONL events, numerical signal files, and generated HTML reports. Use a single simulation worker with isolated agent objects and serialized inboxes. A small external launcher supervises worker exit and wall-clock stalls. Prefer MuJoCo for a greenfield force-coupled prototype because its documented API supports articulated/contact dynamics, actuation and Python access [W1]; this is a fit judgment, not proof that a controller will work. If a working compatible scene exists elsewhere, run it on day 1 before replacing it. Do not introduce ROS, a second simulator or a web API without a demonstrated interface need. Pin actual dependency versions after a clean installation test; do not fabricate a lockfile in the specification.

**Assumptions:** Fixed known membership during a run; non-malicious agents; explicit message fault injection; common simulation clock; model-linked capability limits; supplied object identities, mass and geometry; local observations exposed through a declared interface. Shared clocks and a common simulator limit the claim to simulated decentralized decision-making. Real hardware behavior is not established.

**Outcomes:** An installable coordination package; UC1–UC3 scenarios; schema and protocol definitions; traceable bids/commitments; physics and protocol tests; independent evaluation; all-run comparison report. Novel algorithmic superiority remains a hypothesis. Integrating and evaluating existing methods is an acceptable engineering contribution when accurately described.

## 4. Locked stages and their acceptance evidence

| Stage | Required completion | Exit evidence | What it does not establish |
|---|---|---|---|
| UC1 — guaranteed delivery floor | Live language input; graph validation; local board; capability gate; one bidder using the shared protocol; execution; observed completion; report; one bounded recoverable failure | Fresh checkout run; malformed/ambiguous goal rejection; a mission with dependent subtasks; failed attempt followed by valid retry; traces with graph source | Competitive allocation, multi-robot decentralization, coalitions |
| UC2 — core allocation milestone | Three agents; multiple ready single-robot tasks; hard filters; different bids; deterministic agreement; concurrent execution where resources permit; resource exclusion; one reassignment | Two eligible bidders for at least one task; one cheaper but incapable robot rejected; two tasks overlap in time; no duplicate ownership; changing cost/availability changes assignment; failed but communicating robot releases safely before reassignment | General optimal scheduling; network fault tolerance; cooperative load sharing |
| UC3 — full cooperative target | Two-agent team selected from three candidates at runtime; role-aware admission; preparation and start contract; shared dynamic object; local force feedback; completion and abort evidence | Different scenario facts change selected pair/roles; contact forces and object trajectory recorded; static equilibrium and timestep checks; analytical reject case and feasible alternative; same controller under both admission policies | Loaded partner replacement, arbitrary 3-D manipulation, real-world validation |

**Our extrapolation:** UC1 is the guaranteed minimum working system because faculty requested that floor. It is not a complete validation of the proposed title. If only UC1 is delivered, report an incomplete multi-robot target and obtain an explicit scope decision. UC2 should be the next non-negotiable demonstration of the title's allocation claim. UC3 remains in the full final scope; dropping it changes the project claim and must be visible.

Fixed-coalition UC3 control is a development gate. It is not a substitute for runtime coalition selection. A coalition fixed in YAML, a video, a scalar payload sum, or two independent trajectories does not meet UC3.

## 5. Decentralization, task board and authority

**Proposed formal definition:** For run epoch e and allocation round r, each robot agent i computes its bid and endorses an assignment set using only its local state, the frozen mission/model contract, and messages delivered to i. An executable assignment requires the protocol's peer endorsement certificate. No launcher, UI, persistence layer, simulator or external LLM computes or chooses the live winner. All agents run the same decision rule; no permanent auctioneer exists.

| Component | Authorized work | Prohibited authority |
|---|---|---|
| Task compiler + validator | Propose and validate mission structure; distribute a versioned graph | Choose binding robot identities, invent executable code, bypass eligibility |
| Robot agent | Observe local state; filter; bid; validate candidates; endorse allocation; own execution status and recovery proposals | Read another agent's private memory or hidden evaluator truth |
| Delivery bus | Copy, route, delay, duplicate, reorder or drop messages under a recorded fault profile | Compare bids, select winners, remove members, resolve resource conflicts |
| Simulator + controller | Advance dynamics; provide declared observations; execute certificate-bound skills | Select coalitions or silently expand capabilities |
| Launcher | Freeze configuration; start/stop worker; supervise timeouts; record infrastructure outcomes | Reassign a task after a timeout |
| Evaluator/report | Score recorded ground truth; display trace, comparison and uncertainty | Send decisions to agents during a run |

**Task board:** A replicated logical structure inside every agent. Static fields: mission ID, graph version/hash, task/skill IDs, parameters, dependencies, capability predicates, role count and resource sets. Dynamic fields: task state, task version, current round, candidate records, endorsement certificate, role mapping, reservation set, execution instance ID, progress, evidence reference and reason code. The report is an observational projection of those replicas.

**Proposed lifecycle:** PENDING → READY → NEGOTIATING → COMMITTED → PREPARING → RUNNING → SUCCEEDED. Exceptional transitions go to BLOCKED, FAILED or CANCELLED; a retry creates a new attempt and preserves the old one. Dependency release requires an observed completion event satisfying the declared predicate, not merely an executor's unsupported DONE flag. Task/world/graph versions prevent late completion from an earlier attempt overwriting current state.

**Ownership:** Graph changes come through the validated revision path. Agents jointly endorse assignments. Only the current executor/coalition can publish execution evidence for its attempt; peers verify envelope and state transitions. World facts are versioned separately from graph and allocation revisions. Resource reservations are part of the endorsed assignment set. UI failure does not affect awards. Replica disagreement blocks new awards; the single-process runtime dying is an infrastructure failure, not a successfully tolerated robot crash.

**Established reasoning:** Private state plus messaging is a useful software boundary; process count alone proves neither decentralized decisions nor fault tolerance. A delivery bus must implement event order, but ordering transport events is different from deciding ownership. Test that shuffling delivery order within the same complete round leaves the assignment unchanged.

## 6. Bidding and commitment: concrete baseline for Opus to challenge

**Proposed lock D06:** Use a small-fleet, all-peer, deterministic greedy auction. Avoid claiming CBBA guarantees for a new custom implementation. This is deliberately conservative: unanimous agreement preserves a simple ownership invariant while a missing peer blocks progress. Do not label it partition-tolerant or globally optimal.

### Candidate and objective

Each available agent advertises an immutable bid set for one frozen round, including an explicit NO_BID where it cannot participate. Hard requirements precede scoring: supported skill/tool, reach/contact role, actuator/model limit, current availability, state freshness and resource compatibility. Unknown capability fails admission with an explicit reason; it is not guessed by the LLM.

For a feasible agent i and task t, use an estimated duration cost in seconds:

`c(i,t) = estimated approach time + estimated skill time + estimated waiting time`.

For the initial baseline, a busy robot does not bid, so queue waiting is zero; blocked resources prevent immediate admission. Estimates come from configured paths/skill durations and later measured traces. No mixed-unit weighted sum and no largest-payload bonus. Lower cost wins. Quantize the cost to integer milliseconds, then tie-break by ascending robot ID. Log raw components, units and estimate source. This is local greedy minimization of predicted task completion time, not a proof of minimum fleet makespan.

UC2: sort ready tasks by `(ready_since_tick, task_id)` so older work is considered first. For each task choose the lowest-cost eligible candidate whose robot and resources remain unused in that round. Remove those robots/resources before considering the next task. Commit one nonconflicting assignment set; its tasks can execute concurrently. Repeatedly failed tasks stop after the declared attempt limit, preventing an infinite monopolizing retry.

UC3: enumerate ordered pairs for the two named roles from the received manifests/bids. Reject identical robot IDs, missing skills, unreachable contacts and unavailable resources. Each agent independently evaluates the same candidate pair using the selected admission policy. Rank admissible pairs by `max(approach_time_left, approach_time_right) + cooperative_skill_time`, then ordered role-holder IDs. With three candidates there are at most six role mappings, making exhaustive candidate enumeration reasonable. Pair enumeration here is bounded; it is not a general exponential coalition solver.

### Round and message procedure

1. Freeze the run membership, graph/world versions, prior commitment digest and allocation round. Every peer publishes its snapshot and immutable bid set.
2. Require one valid bid-set response from every configured peer, including NO_BID. A closed local timer is not proof that a missing bidder has ceased acting.
3. Each peer canonicalizes the complete received set, calculates the same candidate decisions, and broadcasts ENDORSE with the input digest and assignment-set digest. It endorses at most one digest per round.
4. A complete, matching endorsement certificate establishes the logical award. Different digests, malformed values or missing peers prevent commitment. The executor validates the certificate and current attempt/version before preparing.
5. Each selected agent reserves its role/resources and emits PREPARED/READY for the execution instance. A local precondition change causes rejection before motion and a recorded abort path.
6. Execute only under the separate start contract below. Publish progress and completion/failure evidence. Close the round through an agreed state boundary before starting another round from its resulting state.
7. Duplicate messages are idempotent. Late old-epoch messages cannot reopen closed decisions. A timeout after any endorsement does not authorize a contradictory award in a new round. Freeze and abort the run if a consistent closure cannot be established; restart only after old executors are stopped/fenced and the world is reset or reconciled.

**Ownership proof obligation:** If every honest peer endorses only one assignment digest per round, and every executable award requires all peers, two distinct certificates cannot exist in that round. Extending this invariant across rounds requires version fencing and explicit closure; unanimous acknowledgement alone does not solve stale execution. Write tests for both, rather than asserting that deterministic sorting proves the whole protocol correct.

**Cooperative start limitation — established reasoning:** Unique ownership and simultaneous physical activation are different properties. An arbitrary message loss can leave one coalition member holding a readiness certificate that another member has not received. More acknowledgements alone do not establish a general atomic physical start under unbounded partition. For the first UC3 release, require a declared bounded-delivery, connected preparation/start interval in the simulated transport model, use a future common activation tick after the configured delivery guard, and pre-test contact readiness. Inject losses outside that supported interval and report aborted/unsupported starts separately. If Opus proposes robustness during the start interval, it must provide the actual protocol, assumptions and adversarial traces. Do not quietly let the launcher choose or force an award.

**Decisions left for explicit adversarial review:** Exact end-of-round closure messages and start-certificate propagation deserve a second review before coding. The design choice is fixed-membership, unanimous, fail-closed allocation; the pending item is verification of a finite-state implementation, not a menu of unrelated algorithms. Crash-stop membership changes during a run are excluded from the first protocol. A robot can become execution-unavailable while its software agent remains responsive and sends NO_BID.

## 7. Communication contract and clocks

**Proposed lock:** Typed, serialized JSON-like message envelopes routed through local per-agent queues. No shared mutable dictionaries between agents. This is an in-process simulation transport, not a deployed wire protocol. A ROS 2/DDS or TCP adapter is future work unless existing tested code justifies it.

Envelope: `schema_version, run_id, epoch, sender_id, sender_seq, message_id, round_id, graph_version, world_version, task_id/attempt_id when applicable, created_tick, expires_tick, kind, payload`. Validate sender membership, finite numeric values, units, required fields and applicable versions. An unknown sender is rejected. Non-malicious origin identity is an assumption of this simulator; cryptographic Byzantine tolerance is outside scope.

| Message family | Purpose and cadence | Failure behavior |
|---|---|---|
| GRAPH / GRAPH_REVISION | Initial accepted graph; later only at a quiescent revision boundary | Reject unsupported versions or inconsistent predecessor state |
| SNAPSHOT / BID_SET / NO_BID | Once per allocation round per peer; retransmit identical payload if needed | Missing response blocks the round; do not reinterpret silence as NO_BID |
| ENDORSE / certificate dissemination | Once per digest; idempotent retransmission | Digest conflict aborts negotiation; late endorsement never overrides another digest |
| PREPARED / READY / REJECT / ABORT | At state transitions before execution | No start before required evidence; no unilateral release of uncertain committed work |
| PROGRESS / COMPLETE / FAILED / RELEASED | Event-driven; progress optionally 5 Hz | Validate execution instance; duplicate completion has no effect; release requires observed stop/reconciliation |
| HEARTBEAT / STATE_DIGEST | Candidate 5 Hz during active runs | After 1 s simulation-time silence mark SUSPECT; suspend new allocation |

**Candidate timing constants:** 20 ms coordination tick; 500 ms bid-set phase deadline; 500 ms endorsement phase deadline; 100 ms retransmission spacing, at most two resends of an unchanged message. These are configuration defaults for testing, not achieved latency results. A deadline miss produces blocked/timeout status; it does not unlock an uncertain award. Evaluate zero loss, duplicate/reordered messages, delays 0–100 ms and isolated losses; test persistent partition as a fail-closed case. A 500 ms phase budget is plausible only within the selected bounded-delay/retry model and must be measured.

Protocol timers, injected delays and modeled execution use simulation time. The event loop must advance virtual time while agents wait, even when robots are idle. Wall-clock time measures LLM/CPU latency. A separate launcher watchdog detects a worker that stops advancing simulation time; candidate threshold 15 s of no progress outside an intentional pause or declared LLM wait. A simulation-clock timer cannot diagnose a stopped simulation clock. Pause state and LLM wait state are explicit, bounded lifecycle states.

## 8. Language interface and graph schema

**Proposed lock:** Natural language → compiler proposal → structural validation → catalogue/world semantic validation → operator clarification if needed → immutable graph version → peer distribution. The LLM chooses supported skills and references; the validator fills/validates capability and completion contracts from one catalogue. Never accept a model's weaker capability requirement as overriding the catalogue.

Top-level fields: `schema_version, mission_id, world_revision, status, clarification_questions, tasks`. Status is one of `proposed`, `needs_clarification`, `unsupported`. Non-proposed responses produce no executable tasks.

Task fields: `task_id, skill_id, arguments with object/location references and units, depends_on, required_capabilities, roles, min_robots, max_robots, resources, concurrency_constraints, preconditions, completion_criteria, timeout_s`. Role entries use symbolic roles such as `left_support` and `right_support`; they never preselect robot IDs. Catalogue checks enforce exactly two distinct holders for the cooperative skill. Resources identify objects, contact sites, destination slots and workspace zones. Dependency edges alone cannot express mutual exclusion; the resource/concurrency fields must do that explicitly.

Example, illustrative contract rather than an implemented schema:

```json
{
  "schema_version": "1.0",
  "mission_id": "M1",
  "world_revision": 1,
  "status": "proposed",
  "clarification_questions": [],
  "tasks": [{
    "task_id": "T1",
    "skill_id": "cooperative_lift_hold_lower",
    "arguments": {"object_id": "beam_1", "lift_height_m": 0.05, "hold_s": 2.0},
    "depends_on": [],
    "required_capabilities": ["support_contact", "local_force_feedback"],
    "roles": [{"role_id": "left_support"}, {"role_id": "right_support"}],
    "min_robots": 2,
    "max_robots": 2,
    "resources": ["beam_1", "lift_zone"],
    "concurrency_constraints": {"distinct_role_holders": true, "exclusive_resources": true},
    "preconditions": [{"predicate": "object_on_supported_surface", "object_id": "beam_1"}],
    "completion_criteria": [{"predicate": "lift_hold_lower_complete", "object_id": "beam_1"}],
    "timeout_s": 30.0
  }]
}
```

The catalogue defines the measurable predicate, permitted argument range, phases and tolerance configuration. LLM text is never evaluated as code. Checks include duplicate task IDs, unknown references, cycles, unavailable skills, illegal role counts, impossible parameter ranges, unsatisfied capability coverage, and incompatible resources. A necessary-condition feasibility precheck is not proof of complete plan feasibility.

**Ambiguity:** Unknown object, multiple matching objects, unspecified destination or unsupported action returns a specific question/error before execution. Syntax/schema errors permit one constrained repair attempt using validator feedback. If that fails, save LLM failure and stop compilation. Candidate total wall-time budget: 30 s across calls; this is a client cutoff, not a provider response guarantee. Save provider/model identifier, prompt version, parameters and raw output without credentials. Live and cached graphs are distinctly labeled.

**Replanning:** First retry/reassign an unchanged valid task deterministically when stopped/released state is confirmed. If a supported world change invalidates the remaining graph, pause at a quiescent boundary, preserve completed tasks, ask the LLM once for a replacement remainder, validate it, and distribute a new version. No LLM call during force-control ticks and no graph mutation under a loaded object. A rejected revision yields a blocked mission with evidence. The old SRS's one-call-only rule must be explicitly superseded.

## 9. Failure model and recovery

All rows are **proposed requirements**. The test column defines the evidence needed before claiming support.

| Failure | Detection | Required response | Acceptance test |
|---|---|---|---|
| Robot execution failure, agent alive | Skill failure event / no progress / actuator-state flag | Stop supported motion, confirm object/resource state, release certificate-bound task, rebid with failed executor excluded; maximum two retries | Inject failure before contact; surviving eligible robot completes; no duplicate execution |
| Robot-agent crash or persistent silence | Heartbeat timeout or worker fault | Mark SUSPECT; stop new awards; abort if membership cannot agree. Restart with new epoch only after old actions are fenced and world reconciled | Stop one agent after endorsement; no replacement award in old epoch |
| Temporary message loss / delay | Deadline and sequence/digest checks | Retransmit same message; retain ownership locks; recover only when complete consistent evidence arrives | Drop/duplicate/delay each protocol phase; eventual delivery either completes consistently or terminates explicitly |
| Persistent partition / bus failure | Missing peer evidence | Fail closed on new work; record communication failure. Do not promise continuing fleet availability | Partition peers; verify no conflicting certificates or new unilateral awards |
| Task precondition / execution failure | Predicate check or skill result | Preserve failed attempt; bounded retry/reassignment if state is known; otherwise block | Inject unreachable/occupied target and failed skill |
| Invalid bid | Schema, finite-value, identity, capability and version checks | Reject with reason; peer can supply explicit valid NO_BID, otherwise round blocks | NaN, negative time, absent role, false eligibility, wrong epoch, duplicate sender |
| Stale state / late completion | Version/attempt mismatch | Ignore for current state; keep audit record; reconcile at boundary | Replay old bid, old READY and old COMPLETE after retry |
| Unavailable capability | No admissible candidates after all peer responses | BLOCKED with requirements and rejection reasons; no relaxation of hard gates | Unsupported tool and insufficient contact force |
| LLM failure / invalid prompt | Timeout, parse error, ambiguous references, catalogue violation | Bounded repair/clarification, then explicit stop; optional disclosed cached graph | Offline API, malformed JSON, invented skill, cyclic graph |
| Incomplete execution | Task/mission horizon; missing postcondition evidence | Report timeout/unknown evidence separately; never mark success from elapsed time alone | Suppress completion evidence and let horizon expire |
| UC3 partner/actuator failure while loaded | Force/pose/contact limits or lost partner state | Attempt only a prevalidated supported hold/lower action if feasible; otherwise terminate simulated trial as failure | Inject partner loss; record resulting forces/motion and limits. No automatic replacement under load |
| Simulator stall/crash | Launcher wall watchdog / exit status | Infrastructure error with partial logs; incomplete bundles remain readable | Kill worker; freeze time progression; verify no false terminal success |
| Evidence write failure | I/O error / missing final manifest | Stop scored run and mark incomplete evidence; no silently successful result | Inject write failure; evaluator refuses a complete-result claim |

**Established reasoning:** A missing heartbeat indicates suspicion, not proof that a robot stopped. A replacement can conflict with a delayed original executor. Reassignment therefore needs a release/stop acknowledgement or a verified fencing/reset boundary. An arbitrary actuator failure also cannot guarantee safe lowering; a controller may lack the remaining force authority.

**Outcome correction to Opus:** Keep at least `planner_verdict`, `execution_status` and `evaluation_status`. Suggested values: verdict accepted/rejected/not_evaluated; execution not_started/running/success/failure/cancelled/infrastructure_error; evaluation complete/partial/unknown, with reason codes. A rejected coalition has `execution_status=not_started`, not an invented observed failure. A horizon timeout is recorded explicitly; label the physical success predicate unknown if available evidence cannot resolve it.

## 10. Functional requirements for the next SRS

All are proposed, testable “shall” requirements. Stage notation specifies first required use.

| ID | Requirement | Stage / pass criterion |
|---|---|---|
| FR01 | Load and validate a scenario with separate truth, planner belief, faults and perturbations | UC1; wrong units/reference rejected before worker launch |
| FR02 | Compile a supported natural-language mission into versioned JSON using a closed catalogue | UC1; live request/response and graph source recorded |
| FR03 | Validate structure, dependencies, references, role constraints and catalogue predicates | UC1; all deliberately malformed fixtures rejected |
| FR04 | Maintain per-agent task-board replicas through validated versioned events | UC1/2; replicas agree at completed round boundaries |
| FR05 | Apply hard capability filters before ranking bids | UC1/2; no accepted bid violates declared hard gates |
| FR06 | Compute and publish auditable bid components and rejection reasons | UC2; two valid bidders and one rejected bidder visible |
| FR07 | Establish assignments only from the peer protocol | UC2; launcher/LLM cannot issue an executable award |
| FR08 | Prevent duplicate robot/object/zone use and enforce dependency release | UC2; conflict and concurrency tests pass |
| FR09 | Exchange versioned messages and handle duplicates, stale messages and missing peers | UC2; each fault has a deterministic recorded disposition |
| FR10 | Execute supported skills in physics with progress, result and cancellation | UC1; postconditions measured independently |
| FR11 | Reassign recoverable released work and bound retries | UC2; one failure-and-reassignment trace, maximum two retries |
| FR12 | Accept an event-triggered validated graph revision at a quiescent boundary | UC2; completed tasks preserved and stale revision rejected |
| FR13 | Select a role-mapped two-robot coalition at runtime | UC3; input change changes coalition or rejection |
| FR14 | Execute shared-object manipulation using declared local feedback | UC3; measured simulated contact/effort and object traces |
| FR15 | Persist all attempts and produce independent reports/recomputation | UC1 onward; failed and partial runs retained |
| FR16 | Compare two admission policies under a compatibility-checked trial manifest | UC3; unapproved configuration difference rejected |
| FR17 | Provide CLI validate/run/report/compare commands and a reproducible environment | UC1 onward; a non-author runs without editing Python |

## 11. Non-functional requirements and provisional numbers

**Our extrapolation:** These are acceptance targets to test, not achieved capabilities. Hard logical invariants are fixed now. Physics and performance defaults receive a measured pilot review before the experiment configuration is frozen. Opus must not convert candidate numbers into measured results.

| ID | Attribute / target | Measurement and baseline |
|---|---|---|
| NF01 | Zero conflicting committed owners, duplicate skill starts or hard-gate violations in the declared test suite | Named adversarial protocol fixtures plus 100 seeded delivery schedules; report count and coverage, not a universal proof |
| NF02 | 10/10 nominal UC1 runs and 9/10 nominal UC2/UC3 runs at engineering gate; 3 full clean demo rehearsals | Frozen cases, all failures included; small sample is readiness evidence only |
| NF03 | p95 local allocation computation under 100 ms for six agents/twenty ready tasks, excluding simulated waiting | Monotonic wall clock, at least 100 rounds on named host; compare one-agent and six-agent cases; report phase/transport time separately |
| NF04 | Detect configured silence within 1.02 s simulation time after last heartbeat, given a 1 s threshold and 20 ms check tick | Inject silence; separately measure wall latency and watchdog behavior; this is suspicion detection |
| NF05 | Live compiler terminates or returns error within 30 s wall-time budget | Timeout/repair fixtures; do not promise external API success |
| NF06 | Two admission policies replaceable without controller/runtime changes | Same interface, different policy ID; matched-run test |
| NF07 | Reference simulation fits under 6 GB peak resident memory and runs headlessly on the selected 16 GB host | Proposed resource target; measure actual host, elapsed time and real-time factor; no GPU requirement inferred |
| NF08 | Metric recomputation on the same complete bundle agrees exactly for counts, and within 1e-6 absolute/relative tolerance for deterministic numeric summaries | Fixed evaluator/dependency version; separately document physics rerun tolerances |
| NF09 | A non-author validates, runs and opens a report within 15 minutes after environment installation | Written instructions, no source edits; one-user usability evidence only |
| NF10 | Every run has versions, resolved configuration, graph provenance, event sequences, units and terminal/incomplete status | Manifest checker; kill worker and verify partial-artifact treatment |
| NF11 | Forces respect configured actuator limits; candidate pose target within 2 cm and 5 degrees for a 2 s hold; no dropped shared object in nominal gate | Chosen scene; compare quasi-static equilibrium and halved timestep; tune before held-out runs, record revisions |
| NF12 | No credentials in tracked files or run exports; LLM cannot execute arbitrary generated code | Export inspection and malicious/invalid skill fixtures |

Physics timestep/control rate are engineering settings, not generic guarantees. Start the pilot with a 2 ms physics step and 10 ms controller update, record actual rates, and check sensitivity at half the physics step. The force/pose thresholds require the concrete model and contact assumptions. Do not inherit the old 500 ms announce-to-award target, 32 GB/GPU host, room survey deadline, or hardware emergency-stop number without matching the new architecture and tests.

## 12. Research experiment and corrections to the new Opus review

**Proposed lock D12:** Compare trait-only coalition admission with geometry/force-aware coalition admission. Keep the bid objective, peer protocol and controller fixed. Treat the experiment as testing whether the richer screen improves selection within the supported model and at what rejection/compute cost. There is no presumption that it wins.

For a quasi-static beam with vertical point supports at xL and xR and center of mass xC strictly between them:

`FR = m*g*(xC-xL)/(xR-xL)` and `FL = m*g - FR`.

For a centered 3 kg beam with g=9.81 m/s², FL=FR=14.715 N. A 20 N/12 N pair passes an aggregate 29.43 N weight check but cannot meet the right-contact requirement under those assumptions. A 20 N/16 N pair can meet the static vertical shares. Dynamic acceleration, friction, actuator geometry and contact loss add constraints; passing this check is only admission under the bounded model. Never generalize scalar force ratings to arbitrary arm poses.

**Critical evaluation correction:** Admission verdict versus execution outcome does not by itself yield admission accuracy. Rejected candidates never execute in the normal policy, and a bad controller can fail a physically feasible candidate. For tiny candidate sets, run a separate evaluation-only campaign on each candidate role mapping under identical controller/initial conditions, including policy-rejected candidates where meaningful in simulation. Define labels as “successful under this tested controller and scenario,” not absolute physical feasibility. Keep the analytic static reference as a separate unit-test oracle. Report false acceptance/rejection only where independent labels exist; retain unknown cases explicitly. The evaluator must not call the admission policy's own predicate implementation as its oracle.

**Trial design:** Begin with a small grid over mass, center-of-mass offset and actuator-limit configurations covering both sides of the analytic boundary. Use paired perturbation realizations for both policies. A seed must change declared values such as initial pose or observation error; repeated identical deterministic inputs are repetitions, not a meaningful seed distribution. Separate pilot/tuning cases from scored cases. Proposed initial budget: 12 scenario configurations × 5 perturbation seeds × 2 policies = 120 pipeline runs; this is an operational starting point, not a statistically powered sample-size claim. Report success/rejection/unknown counts, paired outcomes, force/pose violations, messages, compute time and successful-run makespan with its denominator. Choose final count using pilot variance and runtime; reduce breadth before dropping essential failure categories.

**UC2 baseline:** Use nearest-feasible as a simple behavioral baseline and a centralized deterministic replay of the identical greedy rule to check distributed agreement, without letting it control live runs. An exact assignment solver is optional for small static snapshots with an explicitly matched objective and information set. Do not call a snapshot optimum a bound on a dynamic dependency-constrained mission makespan.

**LLM evaluation:** Freeze a 30-goal set: 20 supported variants across the three use cases, 5 ambiguous goals, 5 unsupported/invalid goals. Score schema validity, required action/dependency/resource semantics, correct clarification and correct refusal. Allow semantically equivalent graphs; literal JSON equality is too strict. Record actual counts, test-set provenance and prompt/model versions. Candidate engineering target: at least 18/20 supported goals semantically correct after the permitted repair, and all 10 ambiguity/unsupported cases blocked from execution. This does not establish general natural-language competence.

### Keep, amend and reject in the new engineering review

| Opus recommendation | Verdict | Reason / required refinement |
|---|---|---|
| CLI + report first, UI after core | Keep | Same run/evaluation functions, much smaller critical path; verify non-author use |
| Single-process private agents | Keep with boundary | Simulated decentralized decisions only; one crash can still stop the whole runtime |
| Run directory instead of database/writer | Keep with amendment | Atomic manifest replacement, one owner per file, flush policy and partial-run recovery remain necessary |
| “CLI passes duplicate-start and UI-restart gates by construction” | Reject as stated | CLI can be launched twice, collide on output paths or leave partial writes. Use unique run IDs/exclusive directory creation; no UI makes UI-restart test inapplicable, not passed |
| Simulation-time protocol clocks | Keep with amendment | Wall watchdog must still detect nonadvancing simulation/blocked worker |
| Merge task/skill catalogue | Keep with boundary | Share semantic definitions, but keep evaluation implementation and observations independent |
| Derive all capabilities from robot model | Amend | Geometric/actuator limits may be derived; tool semantics and empirically supported capacities may require explicit declarations with provenance |
| Admission ownership belongs to agents | Keep and specify | Every peer evaluates the same bounded role-mapped candidates, then endorses the same decision |
| Select admission research question now | Keep as hypothesis | Pilot may expose no useful effect; report a negative result rather than engineer an unfair baseline |
| Planner verdict and run outcome separated | Keep and extend | Add not-started and evaluation completeness; avoid invented labels for rejected candidates |
| Compare only one differing field | Amend | Compare semantic intervention plus allowlisted derived metadata; policy changes legitimately alter trace/output hashes. Worlds/controllers must remain paired |
| Start fixed-coalition control on day 1 | Keep | Highest-risk dependency; early stop/go gate prevents late discovery |
| Remove “health” as a concept | Narrow | Remove a redundant service; retain essential progress/liveness monitoring requested by faculty |
| Member 4 owns physics; Member 3 helps | Amend for actual team | Assign both E&TC members substantive control/model/sensing work and keep three AI&DS owners for compiler, coordination and harness/evaluation |

## 13. Feasibility, calendar, responsibilities and backup

**Documented fact:** The older synopsis names 31 March 2027 as probable completion. **External unknowns:** current next-review date, confirmed final deadline, actual weekly availability, relevant working code elsewhere, faculty hardware criterion, and department-specific acceptance. A model cannot lock these by choosing plausible values.

**Our extrapolation:** A narrow single-host implementation is a credible candidate for a five-person project if fixed-coalition physics works early. Feasibility remains conditional. Use a 12-week engineering plan beginning 8 October 2026 as a planning scenario, not a promise or replacement for the academic deadline. At 10–12 hours/person/week, five people supply 600–720 gross hours. Reserve 25% for integration, exams and rework, leaving 450–540 planned build/test hours. This arithmetic does not establish that the team has that availability or that the work fits it; day-1 inventory and week-2 spike determine whether to revise it.

| Dates | Milestone and dependency | Exit / stop-go condition |
|---|---|---|
| 8–14 Oct | Freeze scope/contracts; inventory any external code; pin host; begin UC1 skeleton and fixed-coalition physics in parallel | One scenario loads, one actuator responds; schema/event fixture; actual review date and hardware question sent to guide by team |
| 15–21 Oct | UC1 fixed graph through physics/report; two-contact control prototype | Clean run; static force shares roughly consistent; if no stable coupled motion, reduce model/motion complexity immediately |
| 22 Oct–4 Nov | UC1 live language, validation and bounded retry; UC2 protocol on mock transport | UC1 complete; adversarial message fixtures preserve ownership; Opus protocol objections resolved with tests |
| 5–18 Nov | UC2 physics/concurrency/resources and recoverable reassignment; fixed-coalition UC3 stabilization | UC2 gate; physics/contact/timestep evidence before attaching runtime selection |
| 19 Nov–2 Dec | Runtime two-role coalition selection; both admission policies; bounded graph revision | Full UC3 trace with changed coalition; all authority checks pass |
| 3–16 Dec | Pilot then freeze scored configuration; paired experiments; separate LLM evaluation | Reports reproducible from complete and failed run records; unknowns preserved |
| 17–30 Dec | Clean install, independent user test, final report, demo rehearsals; thin UI only if core gates passed | Three clean rehearsals; traceability closed; no unsupported claims |

If the next review is within two weeks, promise the frozen design, UC1 slice and UC3 control evidence only. If fewer than six working weeks remain, prioritize UC1/UC2 and one narrow UC3 scenario; explicitly seek faculty scope adjustment rather than silently dropping UC3. A new physical platform has no credible schedule without equipment, budget and access information. Do not add a procurement dependency to this conditional software plan.

| Owner slot | Primary responsibility | First concrete deliverable / cross-check |
|---|---|---|
| AI&DS-1 | Catalogue/schema, language compiler, validated graph revision | Reference graph + goal set; AI&DS-2 verifies execution meaning |
| AI&DS-2 | Agent state, messages, bids, certificates, board and recovery | Mock multi-agent trace; AI&DS-3 audits invariants |
| AI&DS-3 | Launcher, run records, evaluator framework, reports and comparison | Recomputable UC1 bundle; E&TC-2 checks physical scoring |
| E&TC-1 | Physics scene, actuation and cooperative controller | Fixed-coalition coupled motion; E&TC-2 verifies forces |
| E&TC-2 | Model/limit provenance, contact/force observations, geometry admission and model validation | Static force reference and admission implementation; AI&DS-2 integrates it inside peer logic |

Role slots are assignments to ratify by demonstrated ability; actual names are not invented. Each owner writes tests and documentation for their module. Keep admission decision authority inside the robot-agent runtime even if an E&TC member implements the mathematics.

### Risks, triggers and backups

| Risk / owner | Early trigger | Backup and claim limit |
|---|---|---|
| Unstable contact/controller / E&TC pair | No stable fixed-coalition hold by 21 Oct | Reduce to constrained planar/vertical short motion with real coupled dynamics; do not substitute animation |
| Protocol conflict or deadlock / AI&DS-2 | Any duplicate owner or unresolved closure fixture | Freeze membership, serialize negotiation rounds, abort uncertain rounds; drop dynamic join/leave |
| Too much product work / AI&DS-3 | Core gate slips one week | Remove thin UI and live plots first; retain CLI, report and raw evidence |
| LLM unreliable or unavailable / AI&DS-1 | Goal-set failure or API outage | One repair attempt, clarification, disclosed cached graph; cached demo does not satisfy live-language test |
| Weak research effect / E&TC-2 + AI&DS-3 | Both policies identical on honest held-out cases | Report bounded negative result/integration contribution; do not tune scored set for victory |
| Slow simulation / E&TC-1 | Demo exceeds time budget or memory target | Sequential short runs, existing native viewer, labeled recorded batches; reduce scene complexity |
| Faculty requires hardware / team lead | Explicit requirement received | Agree on a relevant available fixture or physical task and replan. Passive load fixture validates only static load model |
| Member bottleneck / team | One owner unavailable or >1-week dependency block | Paired ownership on protocol/physics; shared executable fixtures; keep integration weekly |
| Deadline mismatch / team lead | Confirmed date precedes planned gate | Rebaseline immediately; distinguish delivery floor from full claim |

## 14. Decision ledger and next handoff

| ID | Proposed decision | What remains |
|---|---|---|
| D01 | Faculty-aligned title and bounded statement | Team adopts wording |
| D02 | Three UCs; UC1 floor, UC2 allocation evidence, UC3 final target | Faculty confirms acceptance consequences if a stage slips |
| D03 | Supplied world information; fixed skill catalogue; no scout prerequisite | Concrete model/skill assets implemented |
| D04 | CLI-first package, one physics backend, private simulated agents | Day-1 environment/asset test |
| D05 | Replicated agent board; no central award authority | Source-boundary and delivery-order tests |
| D06 | Fixed-member unanimous greedy allocation | Adversarial review of closure, stale awards and UC3 start; then protocol tests |
| D07 | Duration-based bid objective with deterministic ties | Calibrate estimates; no unsupported optimality claim |
| D08 | Runtime two-role pair selection; one cooperative object | Fixed-coalition controller gate |
| D09 | Fail closed on uncertain ownership; no loaded replacement | Fault injection and supported abort validation |
| D10 | Deterministic reassignment + bounded quiescent LLM graph revision | One example of each, separately logged |
| D11 | Immutable run evidence, independent evaluation, explicit not-started outcomes | Schema and recomputation implementation |
| D12 | Trait-only vs geometry/force-aware admission | Independent labels, pilot, paired scored study |
| D13 | Conditional 12-week plan and 3 AI&DS/2 E&TC roles | Actual deadline, availability and skills confirmed |
| D14 | GitHub as shared review record; Ani approves baseline | Opus connector read/write smoke test; no direct Opus exchange has occurred yet |

**Ready to decide now:** D01–D12 architecture and bounded policy choices can be stated without waiting for another broad survey. The unproven behavior remains marked as such. **Implementation evidence needed:** actual installability, execution/control, commit uniqueness across failure traces, message timings, resource budget, logging integrity. **Controlled experiments needed:** admission benefit/cost, sensitivity to modeled uncertainty, comparative allocation/LLM performance. **External facts needed:** deadline, available effort/assets and faculty hardware acceptance.

Opus should challenge D06/D08/D09/D12 most strongly. For each disagreement supply a concrete failing trace, conflicting requirement or source; propose one correction; state the extra cost and required test. Preserve unresolved external facts as named assumptions with owners and deadlines. Do not call all decisions verified merely because both assistants agree.

## 15. Sources and traceability

User-supplied source locators refer to the original documents in the project, which are not copied into this public repository.

- P1: `FINAL_SYNERGIA_PROJECT_DOCUMENT_CORRECTED(2).pdf`, §§3–7, pp. 2–5: pipeline, decentralization and UC definitions.
- P2: `Synergia_Final_Product_Blueprint(1).pdf`, §§4–8, 10–13: authority, evidence, release gates and product alternatives.
- P3: `Synergia_Workbench_Working_Reference_STE.pdf`, §§1, 3, 6–10: evidence boundary, retained criteria and unresolved items.
- P4: `Synergia_Blueprint_Engineering_Review_STE.pdf`, §§2–8: simplification recommendations and research corrections.
- P5: `SRS_Synergia_v1.0_final.pdf`, §2.5 C1–C8; §4.6 REQ-46–53; §5.1 REQ-85–94; Appendix C: superseded central design, performance assumptions and unresolved requirements.
- P6: `Project_Synopsis_Synergia_G15_final.pdf`, §4, pp. 13–14: old milestones and probable completion date.
- P7: `Synergia_Work_Distribution.md`, introduction and §0: no-code status at authorship and old conflict register; role/schedule headings inspected.
- P8: `Project-State-Synergia(2).md`, §§1–3: historical authority and scope; explicitly superseded here where current instructions differ.
- P9: `Implementation_Design_Tray_Transfer.md`, architecture headings including §5.1: central auctioneer lineage; historical reference only.
- W1: [MuJoCo official overview](https://mujoco.readthedocs.io/en/stable/overview.html), accessed 7 Oct 2026: contact dynamics, actuation, model and Python interfaces. This supports engine capabilities, not Synergia controller performance.
- W2: [MuJoCo computation](https://mujoco.readthedocs.io/en/stable/computation/index.html), accessed 7 Oct 2026: physical modeling context; no version-specific performance claim is inferred.

No implementation test or physics experiment was performed during this document audit. Numeric thresholds, schedules and trial counts in this proposal are labeled design targets and require the stated verification.

## Delivery status

Ani approved publication of these three review files on 7 October 2026. They are the first ChatGPT/Codex proposal for an Opus review, not a ratified technical baseline. No response from Opus has yet been received. Original uploaded project documents are not included.
