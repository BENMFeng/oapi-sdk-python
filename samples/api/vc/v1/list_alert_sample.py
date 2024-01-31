# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.vc.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListAlertRequest = ListAlertRequest.builder() \
        .start_time("1608888867") \
        .end_time("1608888867") \
        .query_type(1) \
        .query_value("6911188411932033028") \
        .page_size(100) \
        .page_token("100") \
        .build()

    # 发起请求
    response: ListAlertResponse = client.vc.v1.alert.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.alert.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: ListAlertRequest = ListAlertRequest.builder() \
        .start_time("1608888867") \
        .end_time("1608888867") \
        .query_type(1) \
        .query_value("6911188411932033028") \
        .page_size(100) \
        .page_token("100") \
        .build()

    # 发起请求
    response: ListAlertResponse = await client.vc.v1.alert.alist(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.alert.alist failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
