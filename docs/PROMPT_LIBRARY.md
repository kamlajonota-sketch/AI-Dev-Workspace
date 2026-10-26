# Reusable AI Coding Prompts

Adapt these prompts to your project. Give the assistant the relevant repository context and never include secrets or private customer data.

## 1. Repository orientation
> Read the repository README and all applicable agent instructions first. Do not edit files yet. Summarize the stack, architecture, main entry points, test commands, and important constraints. Clearly identify anything you could not inspect.

## 2. Plan a feature
> Inspect the existing implementation and identify the smallest safe approach to this feature: [describe feature]. Do not edit yet. Provide acceptance criteria, likely files, risks, alternatives, and tests. Preserve unrelated behavior and ask about material ambiguities.

## 3. Fix a bug
> Reproduce or reason from this report: [steps and redacted error]. Inspect relevant code before proposing a cause. Separate confirmed facts from hypotheses. Suggest a minimal fix and regression test. Do not disable security or tests to hide the failure.

## 4. Implement an approved plan
> Implement only this agreed scope: [plan]. Follow the repository instructions and existing conventions. Keep the change focused, add/update tests, and do not overwrite unrelated work. Run available checks and report exact commands and results. If a check cannot run, explain why.

## 5. Review changes
> Review the current diff as a careful maintainer. Look for correctness bugs, regressions, security/privacy risks, missing tests, accessibility issues, and unrelated changes. Report findings by severity with file/line references. Do not modify files during the review.

## 6. Improve documentation
> Update documentation only for behavior that is confirmed by the code or tests. Keep setup instructions beginner-friendly and copy-pasteable. Use placeholders for secrets. Do not invent commands, configuration options, or capabilities.

## 7. Prepare a release
> Use the release checklist in docs/RELEASE_CHECKLIST.md. Inspect actual project configuration and test commands. Report blockers and unverified items honestly; do not deploy, publish, tag, or change production systems without explicit authorization.

## 8. Final report
> Summarize the result, files changed, behavior affected, checks actually run and their results, known limitations, and manual steps remaining. Distinguish verified facts from assumptions. Do not claim success for work that was not performed.
