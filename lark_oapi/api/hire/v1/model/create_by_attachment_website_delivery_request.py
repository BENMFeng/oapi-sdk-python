# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .website_delivery_attachment import WebsiteDeliveryAttachment


class CreateByAttachmentWebsiteDeliveryRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.website_id: Optional[str] = None
        self.request_body: Optional[WebsiteDeliveryAttachment] = None

    @staticmethod
    def builder() -> "CreateByAttachmentWebsiteDeliveryRequestBuilder":
        return CreateByAttachmentWebsiteDeliveryRequestBuilder()


class CreateByAttachmentWebsiteDeliveryRequestBuilder(object):

    def __init__(self) -> None:
        create_by_attachment_website_delivery_request = CreateByAttachmentWebsiteDeliveryRequest()
        create_by_attachment_website_delivery_request.http_method = HttpMethod.POST
        create_by_attachment_website_delivery_request.uri = "/open-apis/hire/v1/websites/:website_id/deliveries/create_by_attachment"
        create_by_attachment_website_delivery_request.token_types = {AccessTokenType.TENANT}
        self._create_by_attachment_website_delivery_request: CreateByAttachmentWebsiteDeliveryRequest = create_by_attachment_website_delivery_request

    def website_id(self, website_id: str) -> "CreateByAttachmentWebsiteDeliveryRequestBuilder":
        self._create_by_attachment_website_delivery_request.website_id = website_id
        self._create_by_attachment_website_delivery_request.paths["website_id"] = str(website_id)
        return self

    def request_body(self,
                     request_body: WebsiteDeliveryAttachment) -> "CreateByAttachmentWebsiteDeliveryRequestBuilder":
        self._create_by_attachment_website_delivery_request.request_body = request_body
        self._create_by_attachment_website_delivery_request.body = request_body
        return self

    def build(self) -> CreateByAttachmentWebsiteDeliveryRequest:
        return self._create_by_attachment_website_delivery_request
