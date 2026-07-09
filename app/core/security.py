"""Token and signature helpers used for the admin API and webhooks."""
import hashlib
import hmac
import secrets


def generate_api_token(length: int = 32) -> str:
    return secrets.token_urlsafe(length)


def verify_webhook_signature(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)
