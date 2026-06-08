# Contributing to FinShield AI

Thanks for your interest in improving FinShield AI! This document explains how to
set up the project, the standards we hold code to, and how to get a change merged.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Ways to Contribute](#ways-to-contribute)
3. [Local Development Setup](#local-development-setup)
4. [Branch & Commit Conventions](#branch--commit-conventions)
5. [Coding Standards](#coding-standards)
6. [Running Tests](#running-tests)
7. [Pull Request Process](#pull-request-process)
8. [Reporting Bugs & Requesting Features](#reporting-bugs--requesting-features)

---

## Code of Conduct

Be respectful, constructive, and inclusive. Harassment or abusive behavior of any
kind is not tolerated. By participating you agree to keep discussions focused on
the work and welcoming to newcomers.

## Ways to Contribute

- **Report bugs** — open an issue with clear reproduction steps.
- **Improve docs** — typo fixes, clearer explanations, and new guides are all welcome.
- **Add tests** — coverage for edge cases in the ML pipeline or API is highly valued.
- **Build features** — open an issue first so we can align on approach before you code.

## Local Development Setup

FinShield is a split backend (FastAPI + Python 3.12) / frontend (Next.js + TypeScript) app.
See the [README](README.md) for the full quick-start. The short version:

```bash
# Backend
cd backend
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp ../.env.example .env                              # fill in Supabase + secrets
uvicorn app.main:app --reload

# Frontend (separate terminal)
cd frontend
npm install
npm run dev
```

Common tasks are wrapped in the [`Makefile`](Makefile) — run `make help` to see them.

## Branch & Commit Conventions

- Branch from `main` using a descriptive name: `feat/...`, `fix/...`, `docs/...`, `test/...`, `chore/...`.
- Use [Conventional Commits](https://www.conventionalcommits.org/) for messages, e.g.:
  - `feat(backend): add velocity rule to fraud engine`
  - `fix(frontend): correct alert badge color for low-risk scores`
  - `docs: clarify Supabase setup steps`
- Keep commits **atomic** — one logical change per commit.

## Coding Standards

**Backend (Python)**
- Type hints on all function signatures; docstrings on non-trivial service methods.
- Keep routes thin — business logic lives in `services/`, data access in repositories.
- Run linting/formatting before pushing (`make lint` / `make format`).

**Frontend (TypeScript)**
- Prefer typed, small, reusable components; keep data-fetching out of presentational components.
- Handle loading, error, and empty states explicitly.
- Never hardcode API URLs — use the centralized API client.

**Both**
- Never commit secrets. Keep `.env` out of git; document new variables in `.env.example`.
- No mock data in production paths — show an empty state instead.

## Running Tests

```bash
# Backend
cd backend && pytest

# Frontend (unit + e2e)
cd frontend && npm test && npm run test:e2e
```

Please add or update tests for any non-trivial change. CI runs lint, tests, and a
security scan on every pull request — green checks are required before merge.

## Pull Request Process

1. Fork the repo and create your branch from `main`.
2. Make your change with accompanying tests and docs.
3. Ensure `make lint` and the test suite pass locally.
4. Open a PR with a clear description of **what** changed and **why**, linking any related issue.
5. Address review feedback; a maintainer will merge once CI is green and the change is approved.

## Reporting Bugs & Requesting Features

- **Bugs:** open an issue with steps to reproduce, expected vs. actual behavior, and your environment.
- **Features:** open an issue describing the problem you're solving before writing code.
- **Security vulnerabilities:** do **not** open a public issue — follow [SECURITY.md](SECURITY.md).

---

Thanks for helping make fraud detection better. 🛡️
