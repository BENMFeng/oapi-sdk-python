# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.task.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: DeleteTaskRequest = DeleteTaskRequest.builder() \
        .task_id("83912691-2e43-47fc-94a4-d512e03984fa") \
        .build()

    # 发起请求
    response: DeleteTaskResponse = client.task.v1.task.delete(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v1.task.delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: DeleteTaskRequest = DeleteTaskRequest.builder() \
        .task_id("83912691-2e43-47fc-94a4-d512e03984fa") \
        .build()

    # 发起请求
    response: DeleteTaskResponse = await client.task.v1.task.adelete(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v1.task.adelete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
