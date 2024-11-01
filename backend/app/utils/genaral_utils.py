import secrets


def create_tracking_number(length: int = 16) -> str:
    return secrets.token_urlsafe(length)
