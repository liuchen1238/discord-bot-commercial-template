# Prompt: Add a paid-plan feature

English | [繁體中文](add-commercial-feature.md)

Purpose: add a feature that's only usable by specific subscription plans (Pro/Enterprise).

```
I want to add a command /<command_name>, usable only by <plan> plan and above.

Requirements:
1. Add the command in app/cogs/<relevant cog>.py, wrapped with the app.core.permissions.require_plan("<plan>") decorator.
2. Put the business logic in the corresponding app/services/*.py — not in the cog.
3. If a new table/column is needed, update app/models/ and generate an alembic migration.
4. Add tests under tests/test_services/ or tests/test_commands/.
5. Update docs/billing.md if it affects the plan/feature description.
```
