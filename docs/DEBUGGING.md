# Debugging Guide

Debug systematically instead of changing several unrelated things at once.

## 1. Reproduce
- Record the exact steps, expected result, actual result, and error text.
- Identify whether the issue happens every time or intermittently.
- Reduce it to the smallest reproducible case without exposing secrets.

## 2. Locate the failure
- Read the first meaningful error and its stack trace.
- Check recent changes and the relevant configuration.
- Separate frontend, API, database, network, and environment failures.
- Use logs that are safe to share; redact tokens, personal data, and secrets.

## 3. Form a hypothesis
Write down one likely cause and a test that can prove or disprove it. Avoid changing multiple variables at once.

## 4. Fix and verify
Make the smallest targeted change, add a regression test where practical, and rerun the failing test plus related checks.

## 5. Avoid these traps
- Do not randomly reinstall tools or delete lockfiles as a first step.
- Do not disable authentication, TLS, validation, or tests to hide the error.
- Do not claim a fix is verified if you cannot reproduce or test it.
- Do not paste credentials into public issue reports.

## Bug report template
- Environment and version:
- Steps to reproduce:
- Expected result:
- Actual result:
- Full error (redacted):
- What changed recently:
- Checks already tried:
