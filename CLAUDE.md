# Project Harness & Architecture (Top-Level Rules)

These rules take precedence over all other guidance in this repository. Product-specific docs (`plan.docs/{project}/`) and stack rules (`plan.docs/DevOps/`) refine but do not override them.

## 1. Harness Engineering (Karpathy)

- This monorepo follows **Karpathy-style harness engineering**: the LLM is a component inside a reliable system, not a one-shot code generator.
- The harness provides structure, verification loops, and constraints so the agent can iterate safely toward a defined success criterion.
- Implementation work must be **goal-driven**: define verifiable success criteria before coding; validate after each step.

## 2. PKS — Project Knowledge System (Wiki + LLM)

- Implement and maintain **PKS (Project Knowledge System)** as the SSOT bridge between **wiki/docs** and **LLM agents**.
- Before implementation, consult the relevant `plan.docs/` material (DevOps foundations, stack rules, product docs) — not only `.cursorrules` summaries.
- Docs precede code: when docs and code disagree, treat docs as authoritative unless the user explicitly requests a doc update.
- After meaningful changes, update or propose updates to the wiki/docs when behavior, contracts, or env keys change.

**PKS workflow (mandatory order):**

1. Read top-level rules in `CLAUDE.md`
2. Read `plan.docs/DevOps/FOUNDATIONS.md` + stack rules (`BACKEND_RULES.md` / `REACT_RULES.md`)
3. Read product-specific docs under `plan.docs/{project}/` when applicable
4. Plan with explicit success criteria
5. Implement
6. Verify (test, lint, build, or reproducible manual check)

## 3. Architecture — SOLID + Hexagonal + Clean + DDD

All backend feature work **must** comply with:

- **SOLID** (especially DIP: depend on ports/abstractions, not concrete adapters)
- **Hexagonal Architecture** (ports & adapters; inbound vs outbound separation)
- **Clean Architecture** (dependency rule: outer layers depend inward; domain has no framework imports)
- **DDD** (domain language in entities/value objects; application layer orchestrates use cases)

| Layer | Responsibility | Must NOT |
|-------|----------------|----------|
| **Inbound adapter** (API router, schema) | HTTP validation, request/response mapping | SQL, ORM, external API details, business rules |
| **Application** (use case / interactor, port interfaces) | Use-case orchestration, transaction boundaries | HTTP objects, direct DB driver usage |
| **Domain** (entity, value object) | Business rules & domain types | FastAPI, SQLAlchemy, HTTP, env access |
| **Outbound adapter** (pg/memory/orm repository) | Persistence & external I/O | HTTP status decisions, UI concerns |
| **Dependencies / composition root** | Wire ports to adapters (DI factories only) | Business logic |

**Fractal naming:** mirror the same capability name across layers with a consistent prefix + suffix (e.g. `crew_walter_roaster_schema`, `crew_walter_roaster_dto`, `crew_walter_roaster_interactor`).

Entry points (`main.py`) remain thin: route registration and DI only.

## 4. Path & Import Conventions

When describing backend locations in plans, comments, PR text, and agent responses, use these **canonical path prefixes**:

- **App/domain modules** — write paths as `com.auditor/{domain}/...`
  - Omit the `apps/` segment even though the physical path is `com.auditor/apps/{domain}/...`
  - Example: physical `com.auditor/apps/titanic/app/use_cases/...` → document as `com.auditor/titanic/app/use_cases/...`
- **Core/shared modules** — prefix with `com.auditor.core.`
  - Example: physical `com.auditor/core/matrix/grid_oracle_database_manager.py` → `com.auditor.core.matrix.grid_oracle_database_manager`

**Imports in Python code** remain as the repository actually uses them today (e.g. `titanic.*`, `matrix.*`). The convention above is for **documentation and harness communication**, not forced import rewrites unless explicitly requested.

## 5. Non-Negotiable Engineering Constraints

- Minimal diff: change only what the request requires.
- No secrets in code or commits.
- External/slow I/O: cache-first return, refresh in background when applicable.
- Existing naming and fractal layout in the repo take precedence over generic templates.

**Trade-off:** favor carefulness over speed; relax only for trivial, unambiguous tasks.

---

# LLM Coding Behavior (Karpathy Guidelines)

**Agent behavior** guidelines to reduce common LLM coding mistakes. When these conflict with the top-level architecture and PKS rules above, follow the top-level rules.

## 1. Think Before Coding

**Do not assume. Do not hide confusion. Surface trade-offs.**

Before implementing:

- State assumptions explicitly. Ask when uncertain.
- When multiple interpretations exist, present alternatives — do not silently pick one.
- Suggest simpler approaches when they exist. Push back on the user's request when warranted.
- Stop when unclear. Name what is confusing and ask.

## 2. Simplicity First

**Only the minimum code needed to solve the problem. No speculative code.**

- Do not add features beyond the requested scope.
- Do not build abstractions for one-off code.
- Do not add unrequested "flexibility" or configurability.
- Do not handle edge cases that are impossible or extremely unlikely.
- If you can write it in 50 lines instead of 200, rewrite it.

Ask yourself: "Would a senior engineer call this over-engineered?" If yes, simplify.

## 3. Surgical Changes

**Touch only what is necessary. Clean up only what your change leaves behind.**

When editing existing code:

- Do not "improve" adjacent code, comments, or formatting.
- Do not refactor code that is not broken.
- Match existing style even if you dislike it.
- If you find dead code unrelated to the task, **mention it only** — do not delete it without being asked.

If your change makes something unused:

- Remove imports, variables, and functions made obsolete **by your change**.
- Leave pre-existing dead code in place unless explicitly requested to remove it.

## 4. Goal-Driven Execution

Turn vague requests into verifiable goals:

- "Add validation" → "Write tests for invalid input and make them pass"
- "Fix bug" → "Write a reproduction test and make it pass"
- "Refactor X" → "Confirm tests pass before and after"

For multi-step work, state a short plan:

```
1. [step] → verify: [check]
2. [step] → verify: [check]
3. [step] → verify: [check]
```

Weak success criteria like "make it work for now" invite endless back-and-forth.

---

**Signals this is working:** unnecessary diff noise decreases, rewrites from over-complexity decrease, and **clear questions happen before implementation** — not after mistakes.
