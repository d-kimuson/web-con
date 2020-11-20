from django_filters.rest_framework import DjangoFilterBackend as OriginalDjangoFilterBackend
from drf_spectacular.plumbing import build_parameter_type as build_parameter_type, follow_field_source as follow_field_source, get_view_model as get_view_model
from drf_spectacular.utils import OpenApiParameter as OpenApiParameter
from typing import Any

class OriginalDjangoFilterBackend: ...

class SpectacularDjangoFilterBackendMixin:
    def get_schema_operation_parameters(self, view: Any): ...

class DjangoFilterBackend(SpectacularDjangoFilterBackendMixin, OriginalDjangoFilterBackend): ...
