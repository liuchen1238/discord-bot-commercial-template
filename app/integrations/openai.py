"""Optional OpenAI integration used by AI-powered commands/plugins."""
from openai import AsyncOpenAI

from app.core.config import get_settings

settings = get_settings()
client = AsyncOpenAI(api_key=settings.openai_api_key)


async def complete(prompt: str, model: str = "gpt-4o-mini") -> str:
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content or ""
