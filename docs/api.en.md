# Admin API

English | [繁體中文](api.md)

Start it with:

```bash
uvicorn app.api.main:app --reload
```

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| GET | `/health` | Health check |
| GET | `/guilds/{guild_id}` | Fetch a single guild's data |
| GET | `/users/{discord_id}` | Fetch/create a user record |
| POST | `/billing/checkout` | Create a Stripe Checkout Session |
| POST | `/webhooks/stripe` | Stripe webhook receiver |

## Middleware

Applied in this order (see [app/api/main.py](../app/api/main.py)):

1. `ErrorHandlerMiddleware`: unifies error response format.
2. `MaintenanceMiddleware`: blocks non-`/health` requests during maintenance mode.
3. `RateLimitMiddleware`: per-IP request rate limiting.

Schemas are defined in [app/api/schemas/](../app/api/schemas/), all as Pydantic models.
