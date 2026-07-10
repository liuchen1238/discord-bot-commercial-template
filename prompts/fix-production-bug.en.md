# Prompt: Fix a production bug

English | [繁體中文](fix-production-bug.md)

Purpose: standardize the bug-fixing process, so an AI agent doesn't wander outside the scope of the fix.

```
The following issue is happening in production: <describe the symptom, logs, repro steps>

Please, in order:
1. Locate the root cause by reading code first — don't rush into changes. app/cogs -> app/services -> app/database/repositories is the main data flow.
2. Once you find the root cause, apply the smallest possible fix — don't refactor unrelated code along the way.
3. Add a test that reproduces the bug (under tests/), and confirm it passes after the fix.
4. If the issue is caused by inconsistent data, consider whether a one-off data-repair script (under scripts/) is needed, rather than rewriting migration history.
5. Explain the root cause and the fix — no need to add comments in the code explaining "what was done".
```
