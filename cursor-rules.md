# Cursor Harness — com.foodopenlab (Monorepo Root)

Top-level rules take precedence over all other guidance. Full specification: [`CLAUDE.md`](CLAUDE.md).

## Child harness (scope routing)

작업 범위에 맞는 **하위 `cursor-rules.md`를 반드시 함께 읽는다.**

| Scope | File | When |
|-------|------|------|
| **Monorepo (this file)** | `cursor-rules.md` | 우선순위·PKS·공통 에이전트 워크플로 |
| **Backend** | [`com.auditor/cursor-rules.md`](com.auditor/cursor-rules.md) | `com.auditor/` · FastAPI · DB · 도메인 앱 |
| **Frontend** | [`watcher.www/cursor-rules.md`](watcher.www/cursor-rules.md) | `watcher.www/` · Next.js · UI |
| **Flutter** | [`flutter/cursor-rules.md`](flutter/cursor-rules.md) | `flutter/` · Dart · 모바일 |
| **App (sibling)** | `com.auditor/apps/{domain}/_docs/cursor-rules.md` | 특정 백엔드 앱 — [`com.auditor/cursor-rules.md`](com.auditor/cursor-rules.md) 경유 (예: `titanic/_docs/cursor-rules.md`) |

**우선순위:** `CLAUDE.md` + **this file** > **child `cursor-rules.md`** (backend / frontend / flutter / app) > `_docs/{project}/` > `_docs/DevOps/*_RULES.md` > `FOUNDATIONS.md`

**문서 배치:** [`_docs/DOC_PLACEMENT.md`](_docs/DOC_PLACEMENT.md) — 공통 MD → `_docs/` · Backend → `com.auditor/_docs/` · Frontend → `watcher.www/_docs/` · Flutter → `flutter/_docs/` · 루트 harness = 공통만.

---

## 1. Harness Engineering (Karpathy)

- **Karpathy-style harness engineering:** the LLM is a component inside a reliable system, not a one-shot code generator.
- The harness provides structure, verification loops, and constraints so the agent iterates safely toward a defined success criterion.
- Implementation must be **goal-driven:** define verifiable success criteria before coding; validate after each step.

## 2. PKS — Project Knowledge System (Wiki + LLM)

- **PKS** is the SSOT bridge between **wiki/docs** and **LLM agents**.
- Before implementation, consult relevant `_docs/` material — not only harness summaries.
- Docs precede code: when docs and code disagree, treat docs as authoritative unless the user explicitly requests a doc update.
- After meaningful changes, update or propose wiki/docs updates when behavior, contracts, or env keys change.

**PKS workflow (mandatory order):**

1. Read [`CLAUDE.md`](CLAUDE.md) and **this file**
2. Read child harness for your scope ([`com.auditor/cursor-rules.md`](com.auditor/cursor-rules.md) / [`watcher.www/cursor-rules.md`](watcher.www/cursor-rules.md) / [`flutter/cursor-rules.md`](flutter/cursor-rules.md) / `apps/{domain}/_docs/cursor-rules.md`)
3. Read [`_docs/DevOps/FOUNDATIONS.md`](_docs/DevOps/FOUNDATIONS.md) + stack rules (`BACKEND_RULES.md` / `REACT_RULES.md`)
4. Read product-specific docs under `_docs/{project}/` when applicable
5. Plan with explicit success criteria
6. Implement
7. Verify (test, lint, build, or reproducible manual check)

## 3. Architecture — SOLID + Hexagonal + Clean + DDD

---> **이 절은 루트에 있던 백엔드 아키텍처 규칙입니다.** [`com.auditor/CLAUDE.md`](com.auditor/CLAUDE.md) § Architecture (요약: [`com.auditor/cursor-rules.md`](com.auditor/cursor-rules.md)).  
앱별 프랙탈: [`com.auditor/CLAUDE.md`](com.auditor/CLAUDE.md) § App-level specs → `apps/{domain}/_docs/CLAUDE.md` (예: titanic).

## 4. Path & Import Conventions

---> **이 절은 루트에 있던 백엔드 경로 규칙입니다.** [`com.auditor/CLAUDE.md`](com.auditor/CLAUDE.md) § Path & Import Conventions (요약: [`com.auditor/cursor-rules.md`](com.auditor/cursor-rules.md)).

## 5. Non-Negotiable Engineering Constraints

- Minimal diff: change only what the request requires.
- No secrets in code or commits.
- External/slow I/O: cache-first return, refresh in background when applicable.
- Existing naming and fractal layout take precedence over generic templates.

**Trade-off:** favor carefulness over speed; relax only for trivial, unambiguous tasks.

---

# Cursor Agent Workflow (Operational)

For full Karpathy agent-behavior guidelines, see [`CLAUDE.md`](CLAUDE.md) § LLM Coding Behavior.

## Harness file roles

| File | Role |
|------|------|
| `cursor-rules.md` | Monorepo root — priority & PKS (this file) — **공통만** |
| [`CLAUDE.md`](CLAUDE.md) | Monorepo full spec + Karpathy agent-behavior |
| [`_docs/DOC_PLACEMENT.md`](_docs/DOC_PLACEMENT.md) | 문서 배치 규칙 SSOT |
| [`_docs/`](_docs/) | 위키 · DevOps · 제품 (공통 MD) |
| [`com.auditor/CLAUDE.md`](com.auditor/CLAUDE.md) | Backend full spec |
| [`com.auditor/_docs/`](com.auditor/_docs/) | Backend PKS (app, db, auth, entity, scaffold, mfds-erd) |
| [`watcher.www/CLAUDE.md`](watcher.www/CLAUDE.md) | Frontend full spec |
| [`watcher.www/_docs/`](watcher.www/_docs/) | Frontend PKS (REACT_RULES, README) |
| [`flutter/CLAUDE.md`](flutter/CLAUDE.md) | Flutter full spec |
| [`flutter/_docs/`](flutter/_docs/) | Flutter harness |
| `com.auditor/apps/{domain}/_docs/CLAUDE.md` | Per-app backend full spec (sibling apps) |
| [`com.auditor/cursor-rules.md`](com.auditor/cursor-rules.md) | Backend harness (summary) |
| [`watcher.www/cursor-rules.md`](watcher.www/cursor-rules.md) | Frontend harness (summary) |
| [`flutter/cursor-rules.md`](flutter/cursor-rules.md) | Flutter harness (summary) |
| `com.auditor/apps/{domain}/_docs/cursor-rules.md` | Per-app backend harness (summary) |
| [`_docs/DevOps/FOUNDATIONS.md`](_docs/DevOps/FOUNDATIONS.md) | Cross-stack foundations |
| `_docs/DevOps/Backend/BACKEND_RULES.md` | Backend coding rules SSOT |
| [`_docs/DevOps/Frontend/REACT_RULES.md`](_docs/DevOps/Frontend/REACT_RULES.md) | Frontend coding rules SSOT |
| [`_docs/DevOps/Projects/README.md`](_docs/DevOps/Projects/README.md) | Product docs index |
| `_docs/{project}/` | Product-specific specs (e.g. `_docs/HACCP 개발/`) |
| [`.obsidian/`](.obsidian/) | Obsidian vault config at **monorepo root** (moved from `_docs/.obsidian/`); PKS notes live under `_docs/` |

Submodule-only clone: `_docs` may live at `../_docs/` relative to `com.auditor/` or `watcher.www/`.

## Stack summaries

---> **백엔드·프론트 스택 상세는 각각 분리했습니다.**

| Stack | Harness |
|-------|---------|
| Backend | [`com.auditor/cursor-rules.md`](com.auditor/cursor-rules.md) |
| Frontend | [`watcher.www/cursor-rules.md`](watcher.www/cursor-rules.md) |
| Flutter | [`flutter/cursor-rules.md`](flutter/cursor-rules.md) |

공통: minimal diff · verification method 명시 · env/비밀 커밋 금지.

## Operating Cursor with this harness

1. **Think before coding:** attach relevant files/rules with `@`; ask before coding when ambiguous.
2. **Simplicity:** do not add features, config, or abstractions not requested in the chat.
3. **Surgical changes:** keep diffs tied to the request; avoid adjacent "cleanup" refactors.
4. **Goal-driven:** prefer reproducible verification (test, build, lint) over "it seems to work."
5. **Context:** include files, folders, and rules matching the task scope; avoid large guesses from an empty context.
6. **Loop:** plan → change → verify → iterate only when needed; ask **before** implementation, not only after mistakes.

## User prompt template

```text
@cursor-rules.md @com.auditor/cursor-rules.md   # backend work
@cursor-rules.md @watcher.www/cursor-rules.md   # frontend work
@cursor-rules.md @flutter/cursor-rules.md       # flutter work
@com.auditor/apps/titanic/_docs/cursor-rules.md   # titanic app (example)

@_docs/DOC_PLACEMENT.md   # 문서를 어디에 쓸지
@_docs/DevOps/FOUNDATIONS.md @_docs/DevOps/[Backend|Frontend]/..._RULES.md

Acknowledge harness + DevOps rules, then [task].
Add @_docs/{project}/ when product specs are required.
```

## Acknowledgment (one line)

`_docs acknowledged: FOUNDATIONS + [Backend|Frontend]_RULES (+ project MD) · harness: root + [backend|frontend|app] cursor-rules.md`
