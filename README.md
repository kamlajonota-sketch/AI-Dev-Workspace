# AI-Dev-Workspace

A practical, reusable workspace for building software with AI coding assistants. It includes project rules, planning templates, testing checklists, and a full mirror of the official Everything Claude Code (ECC) toolkit for inspection and ChatGPT-assisted workflows.

## Start here

1. Read [AGENTS.md](AGENTS.md) before asking an AI assistant to change code.
2. Read the [ChatGPT ECC guide](docs/ECC_CHATGPT_GUIDE.md) for how to use ECC concepts through the ChatGPT GitHub connection.
3. Check [ECC_FILE_INDEX.md](ECC_FILE_INDEX.md) to locate agents, skills, commands, rules, hooks, scripts, tests, platform adapters, and documentation.
4. Use the [project brief template](templates/PROJECT_BRIEF.md) to define a new project.
5. Follow [the workflow guide](docs/WORKFLOW.md) and [testing checklist](docs/TESTING.md).
6. Read [security guidance](docs/SECURITY.md) before handling credentials, user data, or deployments.

## ECC source mirror

The official ECC repository is mirrored under [vendor/ecc/](vendor/ecc/). The sync workflow copies the complete upstream tree and generates a searchable file index. See [ECC mirror status](docs/ECC_MIRROR_STATUS.md) and [the sync workflow](.github/workflows/sync-ecc.yml).

**Important:** mirroring the files makes them available for review and reference; it does not install ECC runtime features into ChatGPT. Native hooks, slash commands, local scripts, memory automation, and MCP services require a compatible harness or separately configured integration. The ChatGPT guide explains the supported workflow and limitations.

## Repository map

- `AGENTS.md` — core instructions for AI coding agents.
- `vendor/ecc/` — full official ECC source snapshot, maintained by the sync workflow.
- `ECC_FILE_INDEX.md` — generated navigation index for the ECC source snapshot.
- `docs/ECC_CHATGPT_GUIDE.md` — ChatGPT workflow and plain-language ECC task prefixes.
- `docs/` — setup, workflow, architecture, testing, debugging, security, and ECC guidance.
- `templates/` — reusable project, task, and README templates.
- `.github/ISSUE_TEMPLATE/` — structured bug and feature reports.
- `.github/PULL_REQUEST_TEMPLATE.md` — review checklist.
- `scripts/validate_workspace.py` — lightweight checks for required workspace files.
- `scripts/build_ecc_index.py` — generates the ECC file index after a sync.
- `.github/workflows/validate.yml` — validates workspace files on pushes and pull requests.
- `.github/workflows/sync-ecc.yml` — imports the official ECC source snapshot.

## Works with

The Markdown instructions can be used as reference by ChatGPT and other assistants. ECC-specific executable features vary by harness; check the upstream support documentation rather than assuming that every runtime feature works in every tool.

## Principles

- Understand before editing.
- Make the smallest useful change.
- Preserve existing user work and public interfaces.
- Never expose secrets or disable security checks just to make a test pass.
- Verify changes and report what was and was not tested.
- Ask before destructive, costly, externally visible, or irreversible actions.

## Quick checklist

- [ ] Requirements and acceptance criteria are clear.
- [ ] The correct repository and files are targeted.
- [ ] No secrets or personal data are committed.
- [ ] Tests/checks have been run where possible.
- [ ] Documentation is updated when behavior changes.
- [ ] The final report lists changed files, checks, and known limitations.

## License

This workspace's original files and the mirrored upstream ECC files may have different license terms. See the license files in each location before redistributing or modifying content.
