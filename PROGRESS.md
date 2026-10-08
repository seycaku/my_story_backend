# Backend Learning Progress

**Last updated:** 2026-10-08  
**Goal:** Become a confident Junior Python Backend Developer.  
**Current stage:** Initial assessment completed; preparing for independent CRUD practice.

## Background
I have previously studied Python, FastAPI, PostgreSQL, and SQLAlchemy. My biggest challenge is retaining concepts and applying them independently instead of only following tutorials.

## Initial knowledge assessment
**Result: 7/10 correct multiple-choice answers.** This is an initial recall check, **not** a measure of job readiness or a coding assessment.

| # | Topic | Result | Observation |
|---|---|---|---|
| 1 | `list` vs `tuple` | Correct, with gaps | Mixed up tuple with set uniqueness. |
| 2 | References and mutation | Correct | Understands shared mutable objects. |
| 3 | Mutable default arguments | Incorrect | Did not recall that a default list persists across calls. |
| 4 | `is` vs `==` | Correct | Understands identity vs equality. |
| 5 | FastAPI missing task | Correct, uncertain | Recognized `200` + `null`; needs explicit 404 practice. |
| 6 | Pydantic coercion | Incorrect | Expected `422` instead of converting numeric string to int. |
| 7 | SQLAlchemy Session | Correct, partial | Knows `add`/`commit`; unclear on `refresh` and `flush`. |
| 8 | SQL JOIN | Incorrect / unsure | Needs `INNER` and `LEFT JOIN` practice. |
| 9 | Primary / Foreign Keys | Correct | Understands basic referential integrity. |
| 10 | PostgreSQL ROLLBACK | Correct, partial | Knows rollback; needs to explain atomicity and idempotency separately. |

## Strengths to build on
- Python object references, identity, and basic mutability.
- Basic FastAPI and HTTP reasoning.
- SQLAlchemy `add()` / `commit()` workflow.
- Primary keys, foreign keys, and basic rollback behavior.

## Topics to reinforce
- [ ] Mutable default arguments
- [ ] Tuple vs set and uniqueness
- [ ] Pydantic coercion vs strict validation
- [ ] FastAPI `HTTPException` and status codes
- [ ] `INNER JOIN` and `LEFT JOIN`
- [ ] SQLAlchemy `flush()`, `refresh()`, and `rollback()`
- [ ] Transaction atomicity and failure recovery
- [ ] HTTP idempotency and duplicate requests

## Practical ability
- **Understand:** some fundamentals demonstrated by explanations.
- **Apply:** not assessed yet with independent coding.
- **Independent:** not assessed yet with independent coding.

## Current milestone — First FastAPI CRUD
**Project:** Simple Task Manager API, initially without a database.

- [ ] Create a minimal FastAPI project and run it.
- [ ] Implement `GET /tasks`.
- [ ] Implement `GET /tasks/{task_id}` with a correct 404 response.
- [ ] Implement `POST /tasks` with Pydantic validation.
- [ ] Implement `PATCH /tasks/{task_id}`.
- [ ] Implement `DELETE /tasks/{task_id}`.
- [ ] Test success, malformed input, and missing task cases.
- [ ] Explain implementation decisions without reading a tutorial.

## Session workflow with ChatGPT
1. Read this file and [ROADMAP.md](ROADMAP.md) at the beginning of a new chat.
2. Give one small programming task at a time; don't supply full solutions unless requested.
3. Let me try independently, then give hints and code review.
4. Test my understanding with a small variant of the task.
5. Record mistakes, evidence, and next steps here after each session.

## Journal template
### YYYY-MM-DD — Topic
- **Built:**
- **What I can explain:**
- **Mistakes / surprises:**
- **Evidence (commit / test):**
- **Skill level:** Understand / Apply / Independent
- **Revisit date:**
- **Next task:**

## Latest session — 2026-10-08
Completed the 10-question foundation assessment. No independent project code has been reviewed yet. We will reinforce gaps during the CRUD project instead of restarting Python from zero.

**Course video to use as a reference:** https://youtu.be/v4YTsdDXBKM

**Next action:** Set up a minimal FastAPI app and implement the first GET endpoint independently.
