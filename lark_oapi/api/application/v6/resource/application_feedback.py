# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.list_application_feedback_request import ListApplicationFeedbackRequest
from ..model.list_application_feedback_response import ListApplicationFeedbackResponse
from ..model.patch_application_feedback_request import PatchApplicationFeedbackRequest
from ..model.patch_application_feedback_response import PatchApplicationFeedbackResponse


class ApplicationFeedback(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def list(self, request: ListApplicationFeedbackRequest,
             option: Optional[RequestOption] = None) -> ListApplicationFeedbackResponse:
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
        response: ListApplicationFeedbackResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   ListApplicationFeedbackResponse)
        response.raw = resp

        return response

    async def alist(self, request: ListApplicationFeedbackRequest,
                    option: Optional[RequestOption] = None) -> ListApplicationFeedbackResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ListApplicationFeedbackResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   ListApplicationFeedbackResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchApplicationFeedbackRequest,
              option: Optional[RequestOption] = None) -> PatchApplicationFeedbackResponse:
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
        response: PatchApplicationFeedbackResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                    PatchApplicationFeedbackResponse)
        response.raw = resp

        return response

    async def apatch(self, request: PatchApplicationFeedbackRequest,
                     option: Optional[RequestOption] = None) -> PatchApplicationFeedbackResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: PatchApplicationFeedbackResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                    PatchApplicationFeedbackResponse)
        response.raw = resp

        return response
