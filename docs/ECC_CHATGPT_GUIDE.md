# Use the full ECC toolkit with ChatGPT

This workspace mirrors the official [affaan-m/ECC](https://github.com/affaan-m/ECC) repository into vendor/ecc/. The mirrored source is the complete upstream snapshot selected by the sync workflow, not a hand-picked subset. ECC_FILE_INDEX.md is generated to help locate its files.

## Start a ChatGPT coding task

When working through the ChatGPT GitHub connection, ask ChatGPT to:

1. Read the root AGENTS.md and this guide.
2. Read ECC_FILE_INDEX.md to discover the available components.
3. Inspect the relevant source files under vendor/ecc/ (agents, skills, commands, rules, hooks, scripts, tests, integrations, MCP configs, manifests, schemas, docs, and platform adapters).
4. Identify which ECC component applies to the task and state any components that cannot run in the current ChatGPT environment.
5. Plan, implement only the requested change, inspect the diff, run available checks through connected tools, and report checks honestly.

### Copy-and-use starter prompt

> Work in kamlajonota-sketch/AI-Dev-Workspace. First read AGENTS.md, docs/ECC_CHATGPT_GUIDE.md, and ECC_FILE_INDEX.md. Use the mirrored full ECC source in vendor/ecc/ as the reference toolkit. For this task, inspect the relevant ECC agents, skills, rules, commands, hooks, scripts, tests, and platform adapters before planning. Apply every compatible workflow directly, translate runtime-only features into an explicit ChatGPT workflow when needed, and clearly label anything that cannot execute in ChatGPT. Do not claim that a hook, test, command, or automation ran unless a connected tool actually ran it. Do not modify AI-Project-Hub.

## ChatGPT equivalents for native ECC commands

ChatGPT does not automatically interpret Claude Code slash commands from files in a repository. Use these plain-language task prefixes in your messages; they are workflow labels, not native slash commands.

- **ECC PLAN:** inspect the project and ECC guidance, then create a plan and acceptance criteria without editing.
- **ECC IMPLEMENT:** implement the approved task in small, reviewable changes.
- **ECC TDD:** define tests first, run the available tests, implement, and verify.
- **ECC REVIEW:** inspect the diff for bugs, regressions, security issues, and missing tests; do not edit unless asked.
- **ECC DEBUG:** reproduce or reason from the supplied error, inspect relevant code, find the root cause, then verify the fix.
- **ECC SECURITY:** review dependencies, secrets handling, permissions, injection risks, unsafe tool execution, and data exposure.
- **ECC RESEARCH:** read the relevant official docs and source first, compare options, and cite external sources when used.
- **ECC DOCUMENT:** update user-facing docs, setup instructions, and examples along with code changes.
- **ECC RELEASE:** follow the project's release checklist and produce a release-readiness report.
- **ECC LEARN:** summarize reusable lessons from the completed task and propose a small, explicit update to project guidance; do not silently rewrite global rules.

## What is mirrored versus executable

The complete ECC repository contains multiple harness-specific implementations. Keeping those files in this GitHub repository makes them inspectable and searchable; it does not install them into ChatGPT.

- **Usable as reference/instructions:** Markdown agents, skills, rules, prompt templates, guides, checklists, schemas, and many examples.
- **Requires a compatible local coding harness:** native slash commands, runtime hooks, shell scripts, package scripts, local memory/session automation, and some agent orchestration.
- **Requires a separately available integration or configuration:** MCP servers and external service connections. A config file alone does not connect or authorize a service in ChatGPT.
- **Must be checked per harness:** adapters for Claude Code, Codex, Cursor, OpenCode, Gemini, and other tools. Do not assume feature parity.

For native execution of ECC's local automation, use the supported target harness and follow the official setup instructions in vendor/ecc/README.md. Do not run installer scripts just because they are present in the mirror.

## Keeping the mirror current

The GitHub Actions workflow .github/workflows/sync-ecc.yml mirrors the official repository's main branch when first installed and can be run manually later. The manual workflow accepts a branch, tag, or commit in ecc_ref; using a release tag or commit makes a snapshot reproducible. Review the upstream changes before relying on new automation.

The workflow copies source files into vendor/ecc/ and regenerates ECC_FILE_INDEX.md. It does not execute ECC's installer or hook scripts. It commits the snapshot to this repository using the repository's GitHub Actions token; repository Actions must be enabled and the token must have permission to write contents.

## License and attribution

The upstream ECC repository states that it is MIT-licensed. The mirror retains upstream files, including its license and attribution notices, under vendor/ecc/. Review the upstream license and any file-specific notices before redistributing modified copies.
