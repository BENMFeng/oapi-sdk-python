# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .website_delivery import WebsiteDelivery


class CreateByResumeWebsiteDeliveryRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.website_id: Optional[str] = None
        self.request_body: Optional[WebsiteDelivery] = None

    @staticmethod
    def builder() -> "CreateByResumeWebsiteDeliveryRequestBuilder":
        return CreateByResumeWebsiteDeliveryRequestBuilder()


class CreateByResumeWebsiteDeliveryRequestBuilder(object):

    def __init__(self) -> None:
        create_by_resume_website_delivery_request = CreateByResumeWebsiteDeliveryRequest()
        create_by_resume_website_delivery_request.http_method = HttpMethod.POST
        create_by_resume_website_delivery_request.uri = "/open-apis/hire/v1/websites/:website_id/deliveries/create_by_resume"
        create_by_resume_website_delivery_request.token_types = {AccessTokenType.TENANT}
        self._create_by_resume_website_delivery_request: CreateByResumeWebsiteDeliveryRequest = create_by_resume_website_delivery_request

    def user_id_type(self, user_id_type: str) -> "CreateByResumeWebsiteDeliveryRequestBuilder":
        self._create_by_resume_website_delivery_request.user_id_type = user_id_type
        self._create_by_resume_website_delivery_request.add_query("user_id_type", user_id_type)
        return self

    def website_id(self, website_id: str) -> "CreateByResumeWebsiteDeliveryRequestBuilder":
        self._create_by_resume_website_delivery_request.website_id = website_id
        self._create_by_resume_website_delivery_request.paths["website_id"] = str(website_id)
        return self

    def request_body(self, request_body: WebsiteDelivery) -> "CreateByResumeWebsiteDeliveryRequestBuilder":
        self._create_by_resume_website_delivery_request.request_body = request_body
        self._create_by_resume_website_delivery_request.body = request_body
        return self

    def build(self) -> CreateByResumeWebsiteDeliveryRequest:
        return self._create_by_resume_website_delivery_request
