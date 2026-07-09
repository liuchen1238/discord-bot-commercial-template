"""Optional GitHub integration (e.g. issue creation from /feedback command)."""
import httpx

from app.core.config import get_settings

settings = get_settings()
API_BASE = "https://api.github.com"


async def create_issue(repo: str, title: str, body: str) -> dict:
    headers = {"Authorization": f"Bearer {settings.github_token}", "Accept": "application/vnd.github+json"}
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{API_BASE}/repos/{repo}/issues",
            json={"title": title, "body": body},
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
