# Testing and Definition of Done

## Choose checks based on the project
Use commands documented by the repository. Common check categories are:
- Unit tests for small functions and business rules.
- Integration tests for communication between components/services.
- End-to-end tests for important user journeys.
- Lint and formatting checks.
- Static type checks.
- Production build/package checks.
- Manual accessibility, responsiveness, and usability review.

Do not assume every project supports every category.

## Test changed behavior
For each change, ask:
1. What should happen in the normal case?
2. What should happen with missing, invalid, or boundary input?
3. What happens when a network, file, permission, or service operation fails?
4. Is access restricted to the right user/role?
5. Does the change preserve existing behavior?

## UI checklist
- [ ] Loading, empty, success, and error states are understandable.
- [ ] Forms validate input and explain errors.
- [ ] Keyboard focus and labels are usable.
- [ ] Layout works at narrow and wide widths.
- [ ] Buttons have meaningful disabled/loading states.
- [ ] No sensitive information is displayed or logged unnecessarily.

## API/data checklist
- [ ] Inputs are validated at the trusted boundary.
- [ ] Authorization is enforced server-side.
- [ ] Errors do not reveal secrets or internal stack traces.
- [ ] Database changes have a safe migration/rollback strategy.
- [ ] Duplicate submissions and retries are considered where relevant.

## Report results honestly
Write down the command and whether it passed, failed, or could not run. If tests were not run, explain the reason. A code review is not a substitute for running tests when they are available.
