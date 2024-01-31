# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_calendar_event_meeting_chat_request import CreateCalendarEventMeetingChatRequest
from ..model.create_calendar_event_meeting_chat_response import CreateCalendarEventMeetingChatResponse
from ..model.delete_calendar_event_meeting_chat_request import DeleteCalendarEventMeetingChatRequest
from ..model.delete_calendar_event_meeting_chat_response import DeleteCalendarEventMeetingChatResponse


class CalendarEventMeetingChat(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateCalendarEventMeetingChatRequest,
               option: Optional[RequestOption] = None) -> CreateCalendarEventMeetingChatResponse:
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
        response: CreateCalendarEventMeetingChatResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          CreateCalendarEventMeetingChatResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateCalendarEventMeetingChatRequest,
                      option: Optional[RequestOption] = None) -> CreateCalendarEventMeetingChatResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateCalendarEventMeetingChatResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          CreateCalendarEventMeetingChatResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteCalendarEventMeetingChatRequest,
               option: Optional[RequestOption] = None) -> DeleteCalendarEventMeetingChatResponse:
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
        response: DeleteCalendarEventMeetingChatResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          DeleteCalendarEventMeetingChatResponse)
        response.raw = resp

        return response

    async def adelete(self, request: DeleteCalendarEventMeetingChatRequest,
                      option: Optional[RequestOption] = None) -> DeleteCalendarEventMeetingChatResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: DeleteCalendarEventMeetingChatResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          DeleteCalendarEventMeetingChatResponse)
        response.raw = resp

        return response
