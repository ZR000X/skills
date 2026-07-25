# Code Standards Hardening Method

## Standard template

```markdown
# [Standard]

## Rule
[Imperative requirement]

## Applies to
[Repository, area, module, file types, or conditions]

## Rationale
[Concise link to design pressure or decision]

## Compliant
```language
...
```

## Prohibited
```language
...
```

## Enforcement
[Types, lint, tests, CI, review, generator, or manual check]

## Exceptions
[Explicit exception process or none]

## Related design
[Links]
```

## Scope test

Before creating a repository-wide rule, ask:

1. Does it recur across several modules?
2. Is consistency valuable enough to constrain future implementation?
3. Is it supported by approved design?
4. Can a developer determine compliance objectively?
5. Can it be enforced or reviewed sustainably?

If not, keep it module-local, scope-local, or record it only as a refactoring choice.

## Frontend examples

Component API and composition, state ownership, data fetching, forms, styling and tokens, accessibility, responsive behaviour, testing, error states, and file organisation.

## Backend examples

Module boundaries, services, validation, APIs, persistence, transactions, errors, logging, security, idempotency, testing, and integration adapters.

## Enforcement ladder

Prefer the strongest practical mechanism:

1. make invalid states impossible through types or APIs;
2. automated tests or architecture checks;
3. lint or static analysis;
4. generators and templates;
5. CI verification;
6. review checklist;
7. prose-only guidance as a last resort.

## Handoff to refactoring

Refactoring is ready when applicable standards are explicit, violations are locatable, exceptions are recorded, and verification mechanisms are known.
