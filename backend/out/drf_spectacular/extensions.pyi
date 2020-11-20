import abc
from abc import abstractmethod
from drf_spectacular.plumbing import OpenApiGeneratorExtension as OpenApiGeneratorExtension
from typing import Any, Optional

class OpenApiAuthenticationExtension(OpenApiGeneratorExtension['OpenApiAuthenticationExtension'], metaclass=abc.ABCMeta):
    name: str
    def get_security_requirement(self, auto_schema: Any): ...
    @abstractmethod
    def get_security_definition(self, auto_schema: Any) -> Any: ...

class OpenApiSerializerExtension(OpenApiGeneratorExtension['OpenApiSerializerExtension']):
    def get_name(self) -> Optional[str]: ...
    def map_serializer(self, auto_schema: Any, direction: Any): ...

class OpenApiSerializerFieldExtension(OpenApiGeneratorExtension['OpenApiSerializerFieldExtension'], metaclass=abc.ABCMeta):
    @abstractmethod
    def map_serializer_field(self, auto_schema: Any, direction: Any) -> Any: ...

class OpenApiViewExtension(OpenApiGeneratorExtension['OpenApiViewExtension'], metaclass=abc.ABCMeta):
    @abstractmethod
    def view_replacement(self) -> Any: ...
