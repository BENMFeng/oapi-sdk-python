# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.add_to_folder_talent_request import AddToFolderTalentRequest
from ..model.add_to_folder_talent_response import AddToFolderTalentResponse
from ..model.batch_get_id_talent_request import BatchGetIdTalentRequest
from ..model.batch_get_id_talent_response import BatchGetIdTalentResponse
from ..model.get_talent_request import GetTalentRequest
from ..model.get_talent_response import GetTalentResponse


class Talent(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def add_to_folder(self, request: AddToFolderTalentRequest,
                      option: Optional[RequestOption] = None) -> AddToFolderTalentResponse:
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
        response: AddToFolderTalentResponse = JSON.unmarshal(str(resp.content, UTF_8), AddToFolderTalentResponse)
        response.raw = resp

        return response

    async def aadd_to_folder(self, request: AddToFolderTalentRequest,
                             option: Optional[RequestOption] = None) -> AddToFolderTalentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: AddToFolderTalentResponse = JSON.unmarshal(str(resp.content, UTF_8), AddToFolderTalentResponse)
        response.raw = resp

        return response

    def batch_get_id(self, request: BatchGetIdTalentRequest,
                     option: Optional[RequestOption] = None) -> BatchGetIdTalentResponse:
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
        response: BatchGetIdTalentResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchGetIdTalentResponse)
        response.raw = resp

        return response

    async def abatch_get_id(self, request: BatchGetIdTalentRequest,
                            option: Optional[RequestOption] = None) -> BatchGetIdTalentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: BatchGetIdTalentResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchGetIdTalentResponse)
        response.raw = resp

        return response

    def get(self, request: GetTalentRequest, option: Optional[RequestOption] = None) -> GetTalentResponse:
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
        response: GetTalentResponse = JSON.unmarshal(str(resp.content, UTF_8), GetTalentResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetTalentRequest, option: Optional[RequestOption] = None) -> GetTalentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetTalentResponse = JSON.unmarshal(str(resp.content, UTF_8), GetTalentResponse)
        response.raw = resp

        return response
