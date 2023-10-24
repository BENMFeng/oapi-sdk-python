# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_tasklist_activity_subscription_request import CreateTasklistActivitySubscriptionRequest
from ..model.create_tasklist_activity_subscription_response import CreateTasklistActivitySubscriptionResponse
from ..model.delete_tasklist_activity_subscription_request import DeleteTasklistActivitySubscriptionRequest
from ..model.delete_tasklist_activity_subscription_response import DeleteTasklistActivitySubscriptionResponse
from ..model.get_tasklist_activity_subscription_request import GetTasklistActivitySubscriptionRequest
from ..model.get_tasklist_activity_subscription_response import GetTasklistActivitySubscriptionResponse
from ..model.list_tasklist_activity_subscription_request import ListTasklistActivitySubscriptionRequest
from ..model.list_tasklist_activity_subscription_response import ListTasklistActivitySubscriptionResponse
from ..model.patch_tasklist_activity_subscription_request import PatchTasklistActivitySubscriptionRequest
from ..model.patch_tasklist_activity_subscription_response import PatchTasklistActivitySubscriptionResponse


class TasklistActivitySubscription(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateTasklistActivitySubscriptionRequest,
               option: Optional[RequestOption] = None) -> CreateTasklistActivitySubscriptionResponse:
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
        response: CreateTasklistActivitySubscriptionResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                              CreateTasklistActivitySubscriptionResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteTasklistActivitySubscriptionRequest,
               option: Optional[RequestOption] = None) -> DeleteTasklistActivitySubscriptionResponse:
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
        response: DeleteTasklistActivitySubscriptionResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                              DeleteTasklistActivitySubscriptionResponse)
        response.raw = resp

        return response

    def get(self, request: GetTasklistActivitySubscriptionRequest,
            option: Optional[RequestOption] = None) -> GetTasklistActivitySubscriptionResponse:
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
        response: GetTasklistActivitySubscriptionResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                           GetTasklistActivitySubscriptionResponse)
        response.raw = resp

        return response

    def list(self, request: ListTasklistActivitySubscriptionRequest,
             option: Optional[RequestOption] = None) -> ListTasklistActivitySubscriptionResponse:
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
        response: ListTasklistActivitySubscriptionResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                            ListTasklistActivitySubscriptionResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchTasklistActivitySubscriptionRequest,
              option: Optional[RequestOption] = None) -> PatchTasklistActivitySubscriptionResponse:
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
        response: PatchTasklistActivitySubscriptionResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                             PatchTasklistActivitySubscriptionResponse)
        response.raw = resp

        return response
