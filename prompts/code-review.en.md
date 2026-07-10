# Prompt: Code review checklist

English | [繁體中文](code-review.md)

Purpose: review a PR or diff for conformance with this project's architecture conventions.

```
Please review this diff, checking for:

1. Correct layering: a cog should never touch the database or call a third-party SDK directly; a service should never handle a discord.Interaction directly.
2. Plan-gated commands use require_plan() rather than checking the plan ad hoc.
3. Database changes have a corresponding alembic migration.
4. Unnecessary new abstractions, over-engineering, or redundant error handling (trust internal guarantees).
5. Security concerns: webhook signature verification, SQL injection, secrets hardcoded in code.
6. Corresponding tests were added.

List specific issues with file names and line numbers, and flag their severity.
```
