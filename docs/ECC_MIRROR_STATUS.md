# ECC mirror status

- Upstream repository: https://github.com/affaan-m/ECC
- Local mirror destination: vendor/ecc/
- File inventory: ECC_FILE_INDEX.md
- Sync workflow: .github/workflows/sync-ecc.yml
- ChatGPT usage instructions: docs/ECC_CHATGPT_GUIDE.md

The mirror workflow is configured to copy the complete upstream repository tree, excluding only the upstream Git metadata directory. It retains upstream folders and files rather than selecting a small subset.

**Important:** a repository snapshot is not the same thing as a runtime installation. ChatGPT can inspect the mirrored source through the GitHub connection and apply compatible guidance, but local hooks, shell commands, background services, MCP servers, and harness-specific slash commands do not become native ChatGPT features just because their files exist here.

After adding or changing the sync workflow, verify the run under the GitHub repository's Actions tab. Do not mark the mirror complete until a successful run has created vendor/ecc/ and ECC_FILE_INDEX.md.
