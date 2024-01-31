# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.task.v2 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateCommentRequest = CreateCommentRequest.builder() \
        .user_id_type("open_id") \
        .request_body(InputComment.builder()
                      .content("这是一条评论。")
                      .reply_to_comment_id("6937231762296684564")
                      .resource_type("task")
                      .resource_id("ccb55625-95d2-2e80-655f-0e40bf67953f")
                      .build()) \
        .build()

    # 发起请求
    response: CreateCommentResponse = client.task.v2.comment.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.comment.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


# 异步方式
async def amain():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateCommentRequest = CreateCommentRequest.builder() \
        .user_id_type("open_id") \
        .request_body(InputComment.builder()
                      .content("这是一条评论。")
                      .reply_to_comment_id("6937231762296684564")
                      .resource_type("task")
                      .resource_id("ccb55625-95d2-2e80-655f-0e40bf67953f")
                      .build()) \
        .build()

    # 发起请求
    response: CreateCommentResponse = await client.task.v2.comment.acreate(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.comment.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
