# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DownloadAsImageWhiteboardRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.whiteboard_id: Optional[str] = None

    @staticmethod
    def builder() -> "DownloadAsImageWhiteboardRequestBuilder":
        return DownloadAsImageWhiteboardRequestBuilder()


class DownloadAsImageWhiteboardRequestBuilder(object):

    def __init__(self) -> None:
        download_as_image_whiteboard_request = DownloadAsImageWhiteboardRequest()
        download_as_image_whiteboard_request.http_method = HttpMethod.GET
        download_as_image_whiteboard_request.uri = "/open-apis/board/v1/whiteboards/:whiteboard_id/download_as_image"
        download_as_image_whiteboard_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._download_as_image_whiteboard_request: DownloadAsImageWhiteboardRequest = download_as_image_whiteboard_request

    def whiteboard_id(self, whiteboard_id: str) -> "DownloadAsImageWhiteboardRequestBuilder":
        self._download_as_image_whiteboard_request.whiteboard_id = whiteboard_id
        self._download_as_image_whiteboard_request.paths["whiteboard_id"] = str(whiteboard_id)
        return self

    def build(self) -> DownloadAsImageWhiteboardRequest:
        return self._download_as_image_whiteboard_request
