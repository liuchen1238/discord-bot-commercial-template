# Architecture Overview

English | [繁體中文](architecture.md)

## Layered design

```
Cogs (Discord command layer)
   ↓
Services (business logic)
   ↓
Repositories (data access)
   ↓
Models (SQLAlchemy ORM)
```

- **app/cogs/**: The entry point for user interaction via Discord. Only responsible for parsing input, calling services, and replying.
- **app/services/**: Business logic (subscription checks, billing, notifications, etc.). Never touches the Discord API or SQL directly.
- **app/database/repositories/**: Wraps SQLAlchemy queries. The service layer accesses data through repositories.
- **app/models/**: ORM definitions, mapped to the database schema.
- **app/api/**: A FastAPI admin/webhook service independent of the bot process, sharing the services/database layer with the bot.
- **app/jobs/**: APScheduler scheduled jobs (subscription status checks, cleanup, reports).
- **app/plugins/**: Pluggable command extension modules, described via manifest.json and loaded dynamically by the loader.
- **app/middlewares/**: FastAPI middleware (rate limiting, audit logging, error handling, maintenance mode).
- **app/workers/**: Redis queue + background task consumer, used to offload slow work.

## Two processes

1. `python -m app.main`: starts the Discord bot (`app/bot.py`).
2. `uvicorn app.api.main:app`: starts the admin API, used by Stripe webhooks and any front-end dashboard.

Both share the same `app/database`, `app/models`, and `app/services`, connecting to the same database via `DATABASE_URL`.
