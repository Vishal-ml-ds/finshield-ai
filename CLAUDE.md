# FinShield AI — Project Guide

ML-powered, real-time fraud detection platform for banks, fintechs, and insurance providers.
Multi-tenant, multi-layer ML detection (Rules → Isolation Forest → XGBoost → Neural Network → Ensemble),
with real-time scoring, multi-channel alerts, and a full analytics dashboard.

> **Full system design lives in [`docs/SYSTEM_DESIGN.md`](docs/SYSTEM_DESIGN.md)** — landing page, subscription
> tiers, database schema, ML strategy, connectors, fraud rules, API surface, and the implementation roadmap.
> Read it before making architectural decisions.

## Stack

- **Frontend:** Next.js (App Router) + TypeScript + Tailwind (dark theme) + Zustand + Recharts/D3
- **Backend:** FastAPI (Python 3.12, async) + SQLAlchemy 2.0 + Pydantic v2 + Alembic
- **ML:** scikit-learn, XGBoost, PyTorch → ONNX, SHAP for explainability
- **Data:** Supabase / PostgreSQL (SQLite for local dev) + Redis (cache/queue)
- **Infra:** Docker Compose, GitHub Actions CI, Terraform + AWS ECS

## Layout

```
backend/    FastAPI app — api/v1 routes, ml pipeline, rules engine, services, db (SQLAlchemy + Alembic)
frontend/   Next.js app — landing, auth, dashboard, test-me, settings
docs/        SYSTEM_DESIGN.md (full spec), API_SPEC, ARCHITECTURE, DB_SCHEMA, DEPLOYMENT
infrastructure/ + terraform/   AWS deployment
docker-compose.yml + Makefile  local orchestration
```

## Architecture rules

- Routes stay thin: **API routes → services → repositories → models**. No ORM/SQL in route files.
- Business logic in services; persistence in repositories; validation via Pydantic v2 schemas.
- Async I/O everywhere; type hints on all signatures; structured logging with correlation IDs.
- Multi-tenant: enforce tenant isolation (RLS) on every query. Never leak cross-tenant data.
- Never hardcode secrets — everything via env (`backend/.env`, `frontend/.env.local`). See `.env.example`.
- Dark theme first on the frontend (`#0A0A0F` background, `#111118` cards).

## Quick start

See [`README.md`](README.md). TL;DR: SQLite-based local dev — `cd backend && poetry install && uvicorn app.main:app --reload --port 8003`, then `cd frontend && npm install && npm run dev`.
