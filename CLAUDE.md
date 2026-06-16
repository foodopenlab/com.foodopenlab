# Project Harness & Architecture (Monorepo Root)

These rules take precedence over all other guidance in this repository. Cursor injection summary: [`cursor-rules.md`](cursor-rules.md).

## Child specifications (scope routing)

작업 범위에 맞는 **하위 `CLAUDE.md`를 반드시 함께 읽는다.**

| Scope | File | When |
|-------|------|------|
| **Monorepo (this file)** | `CLAUDE.md` | 우선순위·PKS·LLM 행동 가이드 |
| **Backend** | [`com.auditor/CLAUDE.md`](com.auditor/CLAUDE.md) | `com.auditor/` · FastAPI · DB · 도메인 앱 |
| **Frontend** | [`watcher.www/CLAUDE.md`](watcher.www/CLAUDE.md) | `watcher.www/` · Next.js · UI |
| **App (sibling)** | `com.auditor/apps/{domain}/_docs/CLAUDE.md` | 특정 백엔드 앱 — [`com.auditor/CLAUDE.md`](com.auditor/CLAUDE.md) § App-level specs 경유 (예: `titanic/_docs/CLAUDE.md`) |

**우선순위:** **this file** + [`cursor-rules.md`](cursor-rules.md) > **child `CLAUDE.md`** > `plan.docs/{project}/` > `plan.docs/DevOps/*_RULES.md` > `FOUNDATIONS.md`

---

## 1. Harness Engineering (Karpathy)

- This monorepo follows **Karpathy-style harness engineering**: the LLM is a component inside a reliable system, not a one-shot code generator.
- The harness provides structure, verification loops, and constraints so the agent can iterate safely toward a defined success criterion.
- Implementation work must be **goal-driven**: define verifiable success criteria before coding; validate after each step.

## 2. PKS — Project Knowledge System (Wiki + LLM)

- Implement and maintain **PKS (Project Knowledge System)** as the SSOT bridge between **wiki/docs** and **LLM agents**.
- Before implementation, consult the relevant `plan.docs/` material (DevOps foundations, stack rules, product docs) — not only harness summaries.
- Docs precede code: when docs and code disagree, treat docs as authoritative unless the user explicitly requests a doc update.
- After meaningful changes, update or propose updates to the wiki/docs when behavior, contracts, or env keys change.

**PKS workflow (mandatory order):**

1. Read **this file** and [`cursor-rules.md`](cursor-rules.md)
2. Read child spec for your scope ([`com.auditor/CLAUDE.md`](com.auditor/CLAUDE.md) / [`watcher.www/CLAUDE.md`](watcher.www/CLAUDE.md) / `apps/{domain}/_docs/CLAUDE.md`)
3. Read [`plan.docs/DevOps/FOUNDATIONS.md`](plan.docs/DevOps/FOUNDATIONS.md) + stack rules (`BACKEND_RULES.md` / `REACT_RULES.md`)
4. Read product-specific docs under `plan.docs/{project}/` when applicable
5. Plan with explicit success criteria
6. Implement
7. Verify (test, lint, build, or reproducible manual check)

## 3. Architecture — SOLID + Hexagonal + Clean + DDD

---> **이 절은 루트에 있던 백엔드 아키텍처 전체 명세입니다.** [`com.auditor/CLAUDE.md`](com.auditor/CLAUDE.md) § Architecture 로 분리했습니다.  
앱별 프랙탈 상세는 [`com.auditor/CLAUDE.md`](com.auditor/CLAUDE.md) § App-level specs → `apps/{domain}/_docs/CLAUDE.md` (예: titanic)를 따릅니다.

## 4. Path & Import Conventions

---> **이 절은 루트에 있던 백엔드 경로 규칙입니다.** [`com.auditor/CLAUDE.md`](com.auditor/CLAUDE.md) § Path & Import Conventions 로 분리했습니다.

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

---

## Harness file map

| File | Role |
|------|------|
| [`cursor-rules.md`](cursor-rules.md) | Cursor-injected summary (links to this tree) |
| `CLAUDE.md` | Monorepo full spec (this file) |
| [`com.auditor/CLAUDE.md`](com.auditor/CLAUDE.md) | Backend architecture & stack |
| [`watcher.www/CLAUDE.md`](watcher.www/CLAUDE.md) | Frontend architecture & stack |
| `com.auditor/apps/{domain}/_docs/CLAUDE.md` | Per-app backend spec (sibling apps) |
| [`plan.docs/DevOps/`](plan.docs/DevOps/) | Wiki SSOT (detail) |
