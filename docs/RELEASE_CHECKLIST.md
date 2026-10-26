# Release Readiness Checklist

Adapt this checklist to the application's risk level and release process. Not every item applies to every project.

## Scope and quality
- [ ] Release scope and known limitations are documented.
- [ ] Acceptance criteria are met.
- [ ] Relevant automated tests pass.
- [ ] Lint, type checks, and production build pass where available.
- [ ] Important user journeys have been manually checked where appropriate.
- [ ] Dependency and platform compatibility has been reviewed.

## Security and privacy
- [ ] No secrets or private data are included in the release artifacts.
- [ ] Authentication and authorization are verified for protected operations.
- [ ] User input and error handling have been reviewed.
- [ ] Privacy notices and data retention behavior are appropriate.
- [ ] Required permissions are minimized.

## Operations
- [ ] Configuration for the target environment is documented.
- [ ] Backups and migration steps are ready where needed.
- [ ] Monitoring/logging avoids secrets and unnecessary personal data.
- [ ] Rollback or recovery plan is understood.
- [ ] Support/contact and incident handling are known.

## Release execution
- [ ] Version and changelog are updated if the project uses them.
- [ ] Release notes explain user-visible changes and breaking changes.
- [ ] Final artifacts are built from the intended commit.
- [ ] Publication/deployment has explicit approval.
- [ ] Post-release smoke checks are planned.

## Final decision
- [ ] Ready to release
- [ ] Blocked — list blockers:
- [ ] Not applicable items explained:
