"""Shared input validation helpers."""
import re

DISCORD_SNOWFLAKE_RE = re.compile(r"^\d{17,20}$")


def is_valid_snowflake(value: str) -> bool:
    return bool(DISCORD_SNOWFLAKE_RE.match(value))
