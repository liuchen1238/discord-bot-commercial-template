# AI-Assisted Development Guide

English | [繁體中文](ai-development-guide.md)

This project is designed to be easy for AI coding agents (like Claude Code) to collaborate on. The `prompts/` directory has prompt templates for a few common tasks:

- [prompts/add-commercial-feature.en.md](../prompts/add-commercial-feature.en.md): add a feature gated behind a paid plan.
- [prompts/add-plugin.en.md](../prompts/add-plugin.en.md): add a plugin.
- [prompts/fix-production-bug.en.md](../prompts/fix-production-bug.en.md): the standard process for fixing a production bug.
- [prompts/code-review.en.md](../prompts/code-review.en.md): a code review checklist.

## Project conventions for AI agents

- Command logic lives only in `app/cogs/`; business logic always goes down into `app/services/`; database access always goes through `app/database/repositories/`.
- To add a database column/table: change `app/models/` first, then generate a migration with `alembic revision --autogenerate` — don't hand-write SQL.
- Commands gated by plan should use the `require_plan()` decorator from `app/core/permissions.py`, not ad-hoc plan checks inside the cog.
- New external service integrations belong in `app/integrations/`; the service layer calls the integration — don't let a cog call a third-party SDK directly.
- After making changes, run `pytest` and `ruff check .`.
