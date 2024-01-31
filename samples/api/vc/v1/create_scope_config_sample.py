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
    request: CreateScopeConfigRequest = CreateScopeConfigRequest.builder() \
        .user_id_type("open_id") \
        .request_body(ScopeConfig.builder()
                      .scope_type(1)
                      .scope_id("omm_608d34d82d531b27fa993902d350a307")
                      .scope_config(RoomConfig.builder().build())
                      .build()) \
        .build()

    # 发起请求
    response: CreateScopeConfigResponse = client.vc.v1.scope_config.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.scope_config.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: CreateScopeConfigRequest = CreateScopeConfigRequest.builder() \
        .user_id_type("open_id") \
        .request_body(ScopeConfig.builder()
                      .scope_type(1)
                      .scope_id("omm_608d34d82d531b27fa993902d350a307")
                      .scope_config(RoomConfig.builder().build())
                      .build()) \
        .build()

    # 发起请求
    response: CreateScopeConfigResponse = await client.vc.v1.scope_config.acreate(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.scope_config.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
