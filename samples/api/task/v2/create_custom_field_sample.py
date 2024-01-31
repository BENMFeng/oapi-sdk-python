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
    request: CreateCustomFieldRequest = CreateCustomFieldRequest.builder() \
        .user_id_type("open_id") \
        .request_body(InputCustomField.builder()
                      .resource_type("tasklist")
                      .resource_id("ec5ed63d-a4a9-44de-a935-7ba243471c0a")
                      .name("优先级")
                      .type("number")
                      .number_setting(NumberSetting.builder().build())
                      .member_setting(MemberSetting.builder().build())
                      .datetime_setting(DatetimeSetting.builder().build())
                      .single_select_setting(SelectSetting.builder().build())
                      .multi_select_setting(SelectSetting.builder().build())
                      .text_setting(TextSetting.builder().build())
                      .build()) \
        .build()

    # 发起请求
    response: CreateCustomFieldResponse = client.task.v2.custom_field.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.custom_field.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: CreateCustomFieldRequest = CreateCustomFieldRequest.builder() \
        .user_id_type("open_id") \
        .request_body(InputCustomField.builder()
                      .resource_type("tasklist")
                      .resource_id("ec5ed63d-a4a9-44de-a935-7ba243471c0a")
                      .name("优先级")
                      .type("number")
                      .number_setting(NumberSetting.builder().build())
                      .member_setting(MemberSetting.builder().build())
                      .datetime_setting(DatetimeSetting.builder().build())
                      .single_select_setting(SelectSetting.builder().build())
                      .multi_select_setting(SelectSetting.builder().build())
                      .text_setting(TextSetting.builder().build())
                      .build()) \
        .build()

    # 发起请求
    response: CreateCustomFieldResponse = await client.task.v2.custom_field.acreate(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.custom_field.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
