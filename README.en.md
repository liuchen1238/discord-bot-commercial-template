# Discord Bot Commercial Template

English | [繁體中文](README.md)

A ready-to-use project template for bootstrapping a **commercial Discord bot**, with:

- Discord.py Cog architecture + layered Service/Repository design
- Subscription billing (Stripe) with plans and feature flags
- FastAPI admin API (webhooks, guild/user management)
- Alembic database migrations, async SQLAlchemy ORM
- Scheduled jobs (subscription checks, cleanup, reports)
- A pluggable plugin system for extending commands
- Docker / Docker Compose / Kubernetes / systemd deployment examples
- GitHub Actions CI (test / lint / deploy)

> ⚠️ This is a **template skeleton**. Business logic (payment integration details, fraud prevention, real database migrations, etc.) needs to be filled in for your actual use case — don't ship it as-is.

## Quick start

```bash
cp .env.example .env
pip install -r requirements.txt
python -m app.main
```

## Project structure

See [docs/architecture.en.md](docs/architecture.en.md).

## License

MIT License, see [LICENSE](LICENSE).
