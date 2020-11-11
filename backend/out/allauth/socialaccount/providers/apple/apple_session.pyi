from typing import Any

APPLE_SESSION_COOKIE_NAME: str
engine: Any
SessionStore: Any

def add_apple_session(request: Any) -> None: ...
def persist_apple_session(request: Any, response: Any) -> None: ...
