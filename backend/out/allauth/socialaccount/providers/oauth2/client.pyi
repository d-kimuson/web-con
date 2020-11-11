from typing import Any, Optional

class OAuth2Error(Exception): ...

class OAuth2Client:
    request: Any = ...
    access_token_method: Any = ...
    access_token_url: Any = ...
    callback_url: Any = ...
    consumer_key: Any = ...
    consumer_secret: Any = ...
    scope: Any = ...
    state: Any = ...
    headers: Any = ...
    basic_auth: Any = ...
    def __init__(self, request: Any, consumer_key: Any, consumer_secret: Any, access_token_method: Any, access_token_url: Any, callback_url: Any, scope: Any, scope_delimiter: str = ..., headers: Optional[Any] = ..., basic_auth: bool = ...) -> None: ...
    def get_redirect_url(self, authorization_url: Any, extra_params: Any): ...
    def get_access_token(self, code: Any): ...
