# ChatGPT/Codex and Opus: shared review workflow

7 October 2026 · Proposed workflow, with the ChatGPT-side repository connection verified

## Recommendation

Use this GitHub repository as the shared record now. Use a draft pull request for each proposed baseline, comments for disagreements and responses, and versioned Markdown/source documents for decisions. Ani approves the baseline. This gives both assistants the same inspectable text and keeps reasoning tied to revisions.

GitHub's official MCP server supports repository, issue and pull-request operations [C1]. GitHub Free includes collaboration on public repositories [C2]. The server code is MIT licensed. The coordination layer can therefore avoid a new paid collaboration service; each assistant still consumes its own subscription/API allowance. No promise of unlimited free model calls is implied.

**Observed here:** GitHub repository access works from this ChatGPT session. Ani approved publication of the three review files on 7 October 2026. They form the first review handoff. **Not verified here:** Opus's access, its connector's write scope, installation on Ani's computer, or a complete cross-assistant round trip. No Opus response has been received in this session.

## Practical choices

| Route | What it does | Fit and verification status |
|---|---|---|
| GitHub repository + official GitHub MCP / existing connector | Shared files, issues, PRs and review comments | Recommended for this task. ChatGPT-side access verified. Opus-side read/write requires a smoke test. GitHub is persistent shared state; it does not automatically invoke either model. |
| PAL MCP Server, `clink` | Launches installed Claude Code/Codex/Gemini CLI agents and returns their results | Best candidate for later direct local delegation. Author documentation and Apache-2.0 license checked [C4–C6]; not installed or executed here. Requires local CLI setup and valid model access. |
| MCP Agent Mail | Agent identities, inboxes, threads and advisory file reservations | Technically relevant, but current license contains an OpenAI/Anthropic-specific rider [C7]. Excluded from this recommendation; no installation or legal compatibility claim made. |

The PAL documentation explicitly describes permissive CLI presets, including bypass flags for some agents. For a supervised review, configure normal permission checks/read-only review behavior rather than accepting the shipped permissive preset. This is a documented implementation characteristic, not a hypothetical concern. Do not treat an orchestration server as providing model access for free. PAL's API-backed tools and its CLI bridge are different access paths.

## Claude surface matters

For **Claude Code**, GitHub and Anthropic document connecting the official remote server with a GitHub personal access token [C3, C8]. Use a token limited to the intended repository and needed contents/PR/issue operations. Configure it in the local client environment; do not paste credentials into this repository or the handoff prompt. Run `/mcp` to check the actual connection; merely adding a configuration does not validate authentication.

For **Claude Desktop**, the official GitHub installation guide currently describes a local-server route and warns that remote custom-connector OAuth compatibility differs [C3]. Do not promise that pasting the remote URL into a web/desktop connector works identically to Claude Code. Claude Chat's native GitHub integration syncs files on a selected branch; the official help page explicitly excludes PRs and commit history [C9]. Do not rely on it to read the review thread. Use repository files as the shared context, and return a reply for Ani to relay when no separate write-capable MCP tools are present.

For **Claude in the browser**, use available repository access for reading, or attach the review files. If it cannot write PR comments, Ani relays the exact response. That is a functional monitored workflow with no extra collaboration service, although it requires an explicit handoff. This Work session has no callable Opus runtime, so it cannot independently start an Opus conversation.

## One-time round-trip test

1. Give Opus the design-review PR URL and paste the contents of `Opus_Handoff_Prompt.txt`. Attach the audit if its GitHub integration cannot read the review branch.
2. Ask Opus to read `Faculty_Action_Audit.md` from the PR head and report the head commit SHA and D06 summary. This detects stale/default-branch reads.
3. If write tools are available, Opus adds a comment prefixed `Opus — round 1`, containing one concrete D06 objection and the cited file/section. Otherwise it returns exactly that text for Ani to relay.
4. In the next ChatGPT turn, provide the PR URL or ask ChatGPT to read the latest Opus comment. ChatGPT identifies that comment, evaluates the objection and adds a response on the same PR.
5. The bridge is verified only after both sides read the other side's actual message. Success means the same revision is read, the comment is persisted, and the reply references the correct objection. Until then, call it a prepared workflow, not completed inter-model collaboration.

## Review rules

- Each proposal names decision ID, evidence, assumptions, strongest objection, chosen correction, implementation cost and closure test.
- Disagreement is useful only when tied to a requirement, counterexample, calculation, source or measured result. Agreement between models is not verification.
- One assistant authors a change; the other reviews it. Avoid simultaneous edits to the same file. Separate branches isolate implementation work when needed.
- Preserve draft status until Ani accepts the decisions. Do not infer consent from a model's approval comment.
- Limit a round to the unresolved technical questions; do not repeatedly recreate the whole research survey. After two unresolved exchanges, produce the smallest discriminating test or present the tradeoff to Ani.
- Never claim a response was sent or received without a tool result or supplied transcript. Tooling cannot guarantee higher quality; track concrete contradictions closed and tests added.
- Keep raw uploaded project documents outside the public repository unless Ani explicitly chooses to publish them. This review records necessary technical findings and source locators.

## Fast handoff now

1. Open the existing SYNERGIA project in Claude Chat so its original documents are available.
2. Add from GitHub: `aniruddhab009/synergia`, branch `review/faculty-baseline-2026-10-07`, folder `docs/review`. If branch selection is unavailable, download/attach the audit instead.
3. Paste the current `Opus_Handoff_Prompt.txt` contents. Add the next-review date, final deadline, hours per member per week, and faculty hardware requirement if known; otherwise mark each unknown.
4. Let Opus finish the review and document. Bring its answer/files back to ChatGPT. With write-capable Claude Code/MCP tools it can instead post to the draft PR; tell ChatGPT when posted.
5. ChatGPT reviews the actual response, records changes, and Ani approves the baseline. Neither GitHub nor this chat automatically starts the other model.

## First message for Opus

> ChatGPT/Codex has prepared the first review in this PR. Please challenge D06's round closure and cooperative start assumptions, D09's failure/reassignment boundary, and D12's independent admission labels. For each, give a concrete failing trace or justify retaining the proposal. Then create the full baseline requested by Ani using the attached handoff prompt. No Opus-side review is recorded yet.

## Sources checked on 7 October 2026

- C1: [GitHub official MCP server](https://github.com/github/github-mcp-server): maintainer, repository/issue/PR tools and MIT license.
- C2: [GitHub plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans): free public repository collaboration.
- C3: [Official GitHub MCP installation for Claude](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-claude.md): Code/Desktop setup differences.
- C4: [PAL MCP Server](https://github.com/BeehiveInnovations/pal-mcp-server): project and provider setup.
- C5: [PAL clink documentation](https://github.com/BeehiveInnovations/pal-mcp-server/blob/main/docs/tools/clink.md): CLI delegation, isolated contexts and documented permission presets.
- C6: [PAL license](https://github.com/BeehiveInnovations/pal-mcp-server/blob/main/LICENSE): Apache 2.0.
- C7: [MCP Agent Mail current license](https://github.com/Dicklesworthstone/mcp_agent_mail/blob/main/LICENSE): named restrictive rider. No legal conclusion about Ani's particular use is asserted.
- C8: [Claude Code MCP documentation](https://code.claude.com/docs/en/mcp): GitHub connection and actual connection verification.

Sources document capabilities and constraints. They do not establish successful installation in Ani's environment.

- C9: [Claude native GitHub integration](https://support.claude.com/en/articles/10167454-use-the-github-integration): selected-branch file sync; PRs and history are not retrieved.
