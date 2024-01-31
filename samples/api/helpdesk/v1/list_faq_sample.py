# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.helpdesk.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListFaqRequest = ListFaqRequest.builder() \
        .category_id("6856395522433908739") \
        .status("1") \
        .search("点餐") \
        .page_token("6856395634652479491") \
        .page_size(20) \
        .build()

    # 发起请求
    response: ListFaqResponse = client.helpdesk.v1.faq.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.helpdesk.v1.faq.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: ListFaqRequest = ListFaqRequest.builder() \
        .category_id("6856395522433908739") \
        .status("1") \
        .search("点餐") \
        .page_token("6856395634652479491") \
        .page_size(20) \
        .build()

    # 发起请求
    response: ListFaqResponse = await client.helpdesk.v1.faq.alist(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.helpdesk.v1.faq.alist failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
