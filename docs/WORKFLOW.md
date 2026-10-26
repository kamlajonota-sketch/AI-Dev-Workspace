# Development Workflow

Use this loop for new features, bug fixes, refactors, and documentation changes.

## Step 1 — Define the outcome
Describe the user problem, desired behavior, constraints, and acceptance criteria. Use `templates/PROJECT_BRIEF.md` for a new project and `templates/TASK_PLAN.md` for a specific change.

Good acceptance criteria are observable. Example: "Submitting an empty email shows a validation message and does not send a request."

## Step 2 — Inspect the project
Read the README, agent instructions, relevant source files, package/build configuration, tests, and git status. Identify what must remain unchanged.

## Step 3 — Plan the smallest safe change
List files likely to change, implementation steps, risks, and tests. Ask before proceeding if the task requires destructive migration, paid services, public deployment, or a decision that cannot be inferred safely.

## Step 4 — Implement incrementally
Make one logical change at a time. Keep interfaces consistent, avoid unrelated formatting, and add tests for behavior. Do not add a dependency just because it is convenient.

## Step 5 — Verify
Run the most relevant tests, lint/type checks, and build. For UI changes, inspect responsive layouts and empty/loading/error states where applicable. Record any command that could not run.

## Step 6 — Review
Inspect the diff and check for:
- unrelated or accidental changes
- exposed credentials or personal information
- unsafe input handling or missing authorization
- outdated docs, broken links, or missing tests
- inaccessible controls and unhandled error states

## Step 7 — Report
Summarize what changed, why, files affected, checks and results, known limitations, and manual follow-up. Never imply an unrun test passed.

## Suggested task prompt

> First inspect the repository and its instructions. Do not edit files yet. Summarize the current implementation, identify the likely cause or relevant files, and propose a minimal plan with acceptance criteria and tests. Preserve unrelated work. After the plan is clear, implement only the approved scope, run available checks, review the diff, and report exact results.
