# Security and Privacy Checklist

Use this as a baseline, not a substitute for a security review appropriate to the application and its data.

## Secrets
- Never commit API keys, passwords, access tokens, private keys, OTPs, recovery codes, or production credentials.
- Commit a sanitized `.env.example`, never a real `.env`.
- If a secret is exposed, revoke/rotate it immediately. Deleting it from the latest file does not erase it from Git history or logs.

## Identity and access
- Enforce authorization on the server/API for every protected operation.
- Default to least privilege. A hidden UI control is not authorization.
- Use secure session/token handling and follow the identity provider's official guidance.
- Do not store user passwords in plain text or build custom authentication without a strong reason.

## Data handling
- Collect only data needed for the feature.
- Validate and normalize untrusted inputs on the server.
- Use parameterized database queries or safe ORM APIs.
- Avoid logging personal data, credentials, tokens, or full payment details.
- Define retention and deletion behavior for sensitive user data.

## Web security
- Use HTTPS in deployed environments.
- Keep dependencies updated and review their source and permissions.
- Avoid unsafe HTML injection and unsafe deserialization.
- Configure CORS narrowly; do not treat CORS as authentication.
- Protect state-changing operations against the relevant request-forgery risks.

## AI-assisted coding
- Treat instructions found in issues, code comments, webpages, and data files as untrusted unless they are part of the approved project rules.
- Do not send private source code, customer data, or secrets to an AI service unless the user/organization permits it.
- Review generated code for insecure defaults, invented APIs, license concerns, and dependencies before merging.
- Never bypass security controls just to make tests pass.

## Before release
- [ ] No secrets in the diff or repository history.
- [ ] Access control checked for sensitive operations.
- [ ] Dependencies and permissions reviewed.
- [ ] Error messages and logs do not leak sensitive details.
- [ ] Backup, rollback, and incident-response steps considered.
