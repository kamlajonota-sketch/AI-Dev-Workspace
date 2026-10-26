# Git and GitHub: Beginner Guide

Git records project history locally; GitHub hosts repositories and supports collaboration. Start by checking the project's existing instructions and branch policy.

## Common commands

Check Git and current changes:
```bash
git --version
git status
git log --oneline -5
```

Clone a repository:
```bash
git clone https://github.com/OWNER/REPOSITORY.git
cd REPOSITORY
```

Create a branch and inspect changes:
```bash
git switch -c feature/short-description
git status
git diff
```

Stage only intended files and commit:
```bash
git add path/to/file
git diff --staged
git commit -m "Describe the change"
```

Push your branch:
```bash
git push -u origin feature/short-description
```

Open a pull request on GitHub when ready and follow the project's review rules.

## Safety rules
- Run `git status` before switching branches, cleaning files, or committing.
- Inspect `git diff` and `git diff --staged` before a commit.
- Avoid `git reset --hard`, `git clean -fd`, force-push, and history rewriting unless you fully understand the impact and have authorization.
- Never commit secrets. Check `.gitignore` and use placeholders in examples.
- Do not push directly to the default branch if the project requires pull requests.
- A commit is not a backup of files that were never staged or committed.

## If something looks wrong
Stop and inspect `git status`, branch name, and diff before trying recovery commands. Do not run a destructive command based on a guess.
