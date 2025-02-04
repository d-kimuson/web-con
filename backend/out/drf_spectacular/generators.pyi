from drf_spectacular.drainage import reset_generator_stats as reset_generator_stats
from drf_spectacular.extensions import OpenApiViewExtension as OpenApiViewExtension
from drf_spectacular.openapi import AutoSchema as AutoSchema
from drf_spectacular.plumbing import ComponentRegistry as ComponentRegistry, alpha_operation_sorter as alpha_operation_sorter, build_root_object as build_root_object, camelize_operation as camelize_operation, error as error, is_versioning_supported as is_versioning_supported, modify_for_versioning as modify_for_versioning, normalize_result_object as normalize_result_object, operation_matches_version as operation_matches_version, sanitize_result_object as sanitize_result_object, warn as warn
from drf_spectacular.settings import spectacular_settings as spectacular_settings
from rest_framework.schemas.generators import BaseSchemaGenerator, EndpointEnumerator as BaseEndpointEnumerator
from typing import Any, Optional

class EndpointEnumerator(BaseEndpointEnumerator):
    def get_api_endpoints(self, patterns: Optional[Any] = ..., prefix: str = ...): ...

class SchemaGenerator(BaseSchemaGenerator):
    endpoint_inspector_cls: Any = ...
    registry: Any = ...
    api_version: Any = ...
    inspector: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def create_view(self, callback: Any, method: Any, request: Optional[Any] = ...): ...
    def parse(self, request: Any, public: Any): ...
    def get_schema(self, request: Optional[Any] = ..., public: bool = ...): ...
