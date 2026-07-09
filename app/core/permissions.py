"""Discord permission / plan-gating checks used as command decorators."""
from functools import wraps

import discord
from discord.ext import commands


def require_guild_admin():
    async def predicate(ctx: commands.Context) -> bool:
        return isinstance(ctx.author, discord.Member) and ctx.author.guild_permissions.administrator

    return commands.check(predicate)


def require_plan(min_plan: str):
    """Gate a command behind a subscription plan tier (checked via services.permission_service)."""

    def decorator(func):
        @wraps(func)
        async def wrapper(self, ctx: commands.Context, *args, **kwargs):
            from app.services.permission_service import PermissionService

            allowed = await PermissionService().has_plan(ctx.guild.id, min_plan)
            if not allowed:
                await ctx.send(f"此指令需要 `{min_plan}` 以上方案，請先升級訂閱。")
                return
            return await func(self, ctx, *args, **kwargs)

        return wrapper

    return decorator
