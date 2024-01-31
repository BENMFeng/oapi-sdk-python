# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.add_custom_field_request import AddCustomFieldRequest
from ..model.add_custom_field_response import AddCustomFieldResponse
from ..model.create_custom_field_request import CreateCustomFieldRequest
from ..model.create_custom_field_response import CreateCustomFieldResponse
from ..model.get_custom_field_request import GetCustomFieldRequest
from ..model.get_custom_field_response import GetCustomFieldResponse
from ..model.list_custom_field_request import ListCustomFieldRequest
from ..model.list_custom_field_response import ListCustomFieldResponse
from ..model.patch_custom_field_request import PatchCustomFieldRequest
from ..model.patch_custom_field_response import PatchCustomFieldResponse
from ..model.remove_custom_field_request import RemoveCustomFieldRequest
from ..model.remove_custom_field_response import RemoveCustomFieldResponse


class CustomField(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def add(self, request: AddCustomFieldRequest, option: Optional[RequestOption] = None) -> AddCustomFieldResponse:
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
        response: AddCustomFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), AddCustomFieldResponse)
        response.raw = resp

        return response

    async def aadd(self, request: AddCustomFieldRequest,
                   option: Optional[RequestOption] = None) -> AddCustomFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: AddCustomFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), AddCustomFieldResponse)
        response.raw = resp

        return response

    def create(self, request: CreateCustomFieldRequest,
               option: Optional[RequestOption] = None) -> CreateCustomFieldResponse:
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
        response: CreateCustomFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateCustomFieldResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateCustomFieldRequest,
                      option: Optional[RequestOption] = None) -> CreateCustomFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateCustomFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateCustomFieldResponse)
        response.raw = resp

        return response

    def get(self, request: GetCustomFieldRequest, option: Optional[RequestOption] = None) -> GetCustomFieldResponse:
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
        response: GetCustomFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), GetCustomFieldResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetCustomFieldRequest,
                   option: Optional[RequestOption] = None) -> GetCustomFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetCustomFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), GetCustomFieldResponse)
        response.raw = resp

        return response

    def list(self, request: ListCustomFieldRequest, option: Optional[RequestOption] = None) -> ListCustomFieldResponse:
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
        response: ListCustomFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), ListCustomFieldResponse)
        response.raw = resp

        return response

    async def alist(self, request: ListCustomFieldRequest,
                    option: Optional[RequestOption] = None) -> ListCustomFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ListCustomFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), ListCustomFieldResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchCustomFieldRequest,
              option: Optional[RequestOption] = None) -> PatchCustomFieldResponse:
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
        response: PatchCustomFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchCustomFieldResponse)
        response.raw = resp

        return response

    async def apatch(self, request: PatchCustomFieldRequest,
                     option: Optional[RequestOption] = None) -> PatchCustomFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: PatchCustomFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchCustomFieldResponse)
        response.raw = resp

        return response

    def remove(self, request: RemoveCustomFieldRequest,
               option: Optional[RequestOption] = None) -> RemoveCustomFieldResponse:
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
        response: RemoveCustomFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), RemoveCustomFieldResponse)
        response.raw = resp

        return response

    async def aremove(self, request: RemoveCustomFieldRequest,
                      option: Optional[RequestOption] = None) -> RemoveCustomFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: RemoveCustomFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), RemoveCustomFieldResponse)
        response.raw = resp

        return response
