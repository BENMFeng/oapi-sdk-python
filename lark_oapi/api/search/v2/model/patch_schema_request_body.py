# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .patch_schema_property import PatchSchemaProperty
from .schema_display import SchemaDisplay


class PatchSchemaRequestBody(object):
    _types = {
        "display": SchemaDisplay,
        "properties": List[PatchSchemaProperty],
    }

    def __init__(self, d=None):
        self.display: Optional[SchemaDisplay] = None
        self.properties: Optional[List[PatchSchemaProperty]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchSchemaRequestBodyBuilder":
        return PatchSchemaRequestBodyBuilder()


class PatchSchemaRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_schema_request_body = PatchSchemaRequestBody()

    def display(self, display: SchemaDisplay) -> "PatchSchemaRequestBodyBuilder":
        self._patch_schema_request_body.display = display
        return self

    def properties(self, properties: List[PatchSchemaProperty]) -> "PatchSchemaRequestBodyBuilder":
        self._patch_schema_request_body.properties = properties
        return self

    def build(self) -> "PatchSchemaRequestBody":
        return self._patch_schema_request_body
