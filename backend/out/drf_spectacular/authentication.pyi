from drf_spectacular.extensions import OpenApiAuthenticationExtension as OpenApiAuthenticationExtension
from typing import Any

class SessionScheme(OpenApiAuthenticationExtension):
    target_class: str = ...
    name: str = ...
    priority: int = ...
    def get_security_definition(self, auto_schema: Any): ...

class BasicScheme(OpenApiAuthenticationExtension):
    target_class: str = ...
    name: str = ...
    priority: int = ...
    def get_security_definition(self, auto_schema: Any): ...

class TokenScheme(OpenApiAuthenticationExtension):
    target_class: str = ...
    name: str = ...
    match_subclasses: bool = ...
    priority: int = ...
    def get_security_definition(self, auto_schema: Any): ...
