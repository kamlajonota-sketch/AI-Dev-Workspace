# AI-Dev-Workspace

A practical, reusable workspace for building software with AI coding assistants. It brings project rules, planning templates, safe development practices, testing checklists, and starter documentation into one public repository.

## Start here

1. Read [AGENTS.md](AGENTS.md) before asking an AI assistant to change code.
2. Use [the project brief template](templates/PROJECT_BRIEF.md) to define a new project.
3. Follow [the workflow guide](docs/WORKFLOW.md) for small, reviewable changes.
4. Use the [testing checklist](docs/TESTING.md) before considering work complete.
5. Read [security guidance](docs/SECURITY.md) before handling credentials, user data, or deployments.

## Repository map

- `AGENTS.md` — core instructions for AI coding agents.
- `docs/` — setup, workflow, architecture, testing, debugging, and security guides.
- `templates/` — reusable project, task, and README templates.
- `.github/ISSUE_TEMPLATE/` — structured bug and feature reports.
- `.github/PULL_REQUEST_TEMPLATE.md` — review checklist.
- `scripts/validate_workspace.py` — lightweight checks for required workspace files.
- `.github/workflows/validate.yml` — runs workspace validation on pushes and pull requests.

## Works with

These are tool-agnostic Markdown instructions. Adapt them for ChatGPT, Claude, Gemini, GitHub Copilot, Cursor, or another coding assistant. Tool-specific commands and hooks are not assumed to exist.

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

No license has been added yet. Unless a license is added, others do not automatically receive permission to reuse this repository's contents. Choose a license intentionally before inviting reuse.
