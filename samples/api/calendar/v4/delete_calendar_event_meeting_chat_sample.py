# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.calendar.v4 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: DeleteCalendarEventMeetingChatRequest = DeleteCalendarEventMeetingChatRequest.builder() \
        .calendar_id("feishu.cn_HF9U2MbibE8PPpjro6xjqa@group.calendar.feishu.cn") \
        .event_id("75d28f9b-e35c-4230-8a83-4a661497db54_0") \
        .meeting_chat_id("oc_a0553eda9014c201e6969b478895c230") \
        .build()

    # 发起请求
    response: DeleteCalendarEventMeetingChatResponse = client.calendar.v4.calendar_event_meeting_chat.delete(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.calendar.v4.calendar_event_meeting_chat.delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
