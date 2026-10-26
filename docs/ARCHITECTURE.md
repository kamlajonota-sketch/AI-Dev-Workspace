# Architecture Notes

Choose architecture based on requirements and constraints, not fashion.

## Describe the system
Document:
- purpose and user roles
- major components and their responsibilities
- data flow and external services
- trust boundaries and authorization rules
- persistence and backup approach
- deployment and operational dependencies

## Keep boundaries clear
- UI: presentation, interaction, client-side convenience validation.
- Application/domain logic: business rules and workflows.
- Data layer: persistence and queries.
- Integration layer: external APIs, queues, file storage, and identity providers.

Small projects may not need separate folders or services for every layer. Avoid needless abstraction.

## Decisions
For a meaningful long-term choice, record:
- Context/problem
- Decision
- Alternatives considered
- Consequences/trade-offs
- Date and owner (if useful)

## Data and migration changes
Plan schema changes before implementation. Consider existing data, migration order, backward compatibility, backup, rollback, and authorization. Never assume a destructive migration is safe because the app is new.
