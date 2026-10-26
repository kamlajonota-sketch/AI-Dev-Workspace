# Windows Setup Guide

This is a general checklist, not a one-size-fits-all installation script. Use the instructions in the specific project's README first.

## 1. Install only what the project needs
Common tools include:
- Git for version control.
- The runtime required by the project (for example, Node.js, Python, Java/JDK, or .NET).
- A code editor such as Visual Studio Code.
- The platform SDK if building for Android or another device platform.

Download tools from their official websites. Avoid random executable download sites.

## 2. Open a terminal
In Windows 10/11, open PowerShell or Windows Terminal. Navigate to the project folder with `cd`.

Examples:
```powershell
Get-Location
Get-ChildItem
git --version
```

Check a runtime only if the project needs it:
```powershell
node --version
npm --version
python --version
```

A command not being recognized often means the tool is not installed or its folder is missing from PATH. Do not overwrite the entire PATH variable. Use the Windows Environment Variables settings and edit the existing value carefully.

## 3. Install project dependencies
Read the project README and identify its package manager and lockfile. Prefer the lockfile-based command recommended by the project. Do not install all possible runtimes or globally install packages without a reason.

## 4. Configure environment
- Copy the provided example configuration if one exists.
- Add real secrets only to a local ignored environment file or a secret manager.
- Never paste secrets into source files, screenshots, public issues, or Git commits.

## 5. Run and verify
Use the exact documented development, test, lint, and build commands. Read the complete error message before changing configuration.

## 6. Common troubleshooting
- **Command not found:** verify installation and PATH; restart the terminal after PATH changes.
- **Dependency error:** check runtime version and the project's package manager/lockfile.
- **Port already in use:** identify the process before stopping anything.
- **Permission denied:** understand the specific path/permission before running as Administrator.
- **Build fails:** capture the first meaningful error and inspect the relevant configuration; avoid deleting lockfiles or caches as a first step.
