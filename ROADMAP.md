# Python Backend Developer Roadmap

## Goal
Become a confident Junior Python Backend Developer through independent projects, testing, and understanding the code I write.

**Core stack:** Python, FastAPI, Pydantic, PostgreSQL, SQLAlchemy, Alembic, pytest, Git, Docker.

## Learning rules
- Use tutorials as references, not code to copy blindly.
- Study a concept, implement it without copying, test it, explain it, and record mistakes.
- Ask ChatGPT for hints and code review before requesting full solutions.
- Tick a box only after verifying a working implementation.
- Review tricky topics after 2–3 days and again after 1–2 weeks.
- Keep secrets out of Git: use `.gitignore` and `.env.example`.
- Update [PROGRESS.md](PROGRESS.md) after each learning session.

## Phase 0 — Setup
- [x] Create the `my_story_backend` GitHub repository.
- [x] Complete an initial 10-question knowledge assessment (7/10 multiple-choice answers correct).
- [ ] Set up a Python virtual environment and dependency management.
- [ ] Create and run a minimal FastAPI application.
- [ ] Add a `.gitignore` and an `.env.example`.
- [ ] Document how to run the application locally.

**Done when:** I can clone and run the application using only the README instructions.

## Phase 1 — CRUD without a database
- [ ] Define a `Task` model and request/response schemas with Pydantic.
- [ ] Implement `GET /tasks`.
- [ ] Implement `GET /tasks/{task_id}` and return 404 when a task is missing.
- [ ] Implement `POST /tasks` with validation and HTTP 201.
- [ ] Implement `PATCH /tasks/{task_id}`.
- [ ] Implement `DELETE /tasks/{task_id}`.
- [ ] Handle malformed inputs and errors correctly.
- [ ] Compare Pydantic's normal type coercion with strict validation.
- [ ] Test endpoints through `/docs` and an HTTP client.
- [ ] Rebuild one endpoint independently, without copying a tutorial.

**Done when:** all endpoints work and I can explain the models, validation, and status codes.

## Phase 2 — PostgreSQL + SQLAlchemy
- [ ] Design tables, primary keys, foreign keys, and constraints.
- [ ] Connect PostgreSQL using environment-based configuration.
- [ ] Define SQLAlchemy models and a per-request Session dependency.
- [ ] Replace in-memory storage with database-backed CRUD.
- [ ] Set up Alembic and create an initial migration.
- [ ] Demonstrate `add()`, `flush()`, `commit()`, `refresh()`, and `rollback()`.
- [ ] Write `INNER JOIN` and `LEFT JOIN` queries in raw SQL.
- [ ] Model a one-to-many relationship and query related records.
- [ ] Demonstrate transaction rollback after a failure.
- [ ] Confirm data persists when the application restarts.

**Done when:** migrations work on a clean database and I can write and explain the SQL and ORM code.

## Phase 3 — Testing and maintainability
- [ ] Split the application into routers, schemas, models, dependencies, and business logic.
- [ ] Add filtering, sorting, and pagination.
- [ ] Write unit tests with pytest.
- [ ] Write integration tests for success and failure cases.
- [ ] Isolate test data using a test database or rolled-back transactions.
- [ ] Add logging and safe error handling.
- [ ] Write a project README with API examples and setup commands.
- [ ] Demonstrate mutable defaults, object identity, and copying in small Python tests.

**Done when:** another person can run the project and its tests reliably.

## Phase 4 — Real multi-user project
- [ ] Add registration and login.
- [ ] Hash passwords securely and verify credentials.
- [ ] Implement an authentication mechanism (e.g., JWT) and understand its trade-offs.
- [ ] Enforce ownership and access control for each user's tasks.
- [ ] Add relationships such as projects, assignments, and comments.
- [ ] Test authorization failures and invalid inputs.
- [ ] Explain HTTP idempotency and implement a suitable example.
- [ ] Document significant architecture decisions.

**Done when:** users can manage their own data without accessing other users' private resources.

## Phase 5 — Deployment and junior readiness
- [ ] Containerize API and PostgreSQL using Docker and Docker Compose.
- [ ] Set up basic health checks and environment configuration.
- [ ] Run automated tests through GitHub Actions.
- [ ] Deploy the API and document the process.
- [ ] Learn the basics of indexes, N+1 queries, and query performance.
- [ ] Build one timed feature without AI-generated code.
- [ ] Prepare a portfolio README with screenshots/examples and links.
- [ ] Practice Python, HTTP, SQL, and backend interview questions.

**Done when:** the deployed application works, the test suite passes, and I can defend my design choices.

## Topics from the diagnostic to revisit
- [ ] `list`, `tuple`, and `set` differences
- [ ] Mutable default arguments and the `None` pattern
- [ ] Pydantic type coercion and strict mode
- [ ] FastAPI `HTTPException` and HTTP status codes
- [ ] `INNER JOIN` vs `LEFT JOIN`
- [ ] SQLAlchemy `flush`, `refresh`, and `rollback`
- [ ] Database transaction atomicity
- [ ] HTTP idempotency vs database transactions

## Skill levels
- **Understand:** I can explain the concept.
- **Apply:** I can use it with documentation or small hints.
- **Independent:** I can implement, test, and explain it without AI-generated solutions.

**Note:** There is no fixed deadline. Progress is based on working code and demonstrated understanding, not on hours of video watched.
