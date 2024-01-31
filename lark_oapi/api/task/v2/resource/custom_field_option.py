# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_custom_field_option_request import CreateCustomFieldOptionRequest
from ..model.create_custom_field_option_response import CreateCustomFieldOptionResponse
from ..model.patch_custom_field_option_request import PatchCustomFieldOptionRequest
from ..model.patch_custom_field_option_response import PatchCustomFieldOptionResponse


class CustomFieldOption(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateCustomFieldOptionRequest,
               option: Optional[RequestOption] = None) -> CreateCustomFieldOptionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateCustomFieldOptionResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   CreateCustomFieldOptionResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateCustomFieldOptionRequest,
                      option: Optional[RequestOption] = None) -> CreateCustomFieldOptionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateCustomFieldOptionResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   CreateCustomFieldOptionResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchCustomFieldOptionRequest,
              option: Optional[RequestOption] = None) -> PatchCustomFieldOptionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchCustomFieldOptionResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  PatchCustomFieldOptionResponse)
        response.raw = resp

        return response

    async def apatch(self, request: PatchCustomFieldOptionRequest,
                     option: Optional[RequestOption] = None) -> PatchCustomFieldOptionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: PatchCustomFieldOptionResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  PatchCustomFieldOptionResponse)
        response.raw = resp

        return response
