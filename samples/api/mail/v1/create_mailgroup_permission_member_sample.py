# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.mail.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateMailgroupPermissionMemberRequest = CreateMailgroupPermissionMemberRequest.builder() \
        .mailgroup_id("xxxxxxxxxxxxxxx 或 test_mail_group@xxx.xx") \
        .user_id_type("user_id") \
        .department_id_type("xxx") \
        .request_body(MailgroupPermissionMember.builder()
                      .user_id("xxxxxxxxxx")
                      .department_id("xxxxxxxxxx")
                      .email("xxx@xx.x")
                      .type("USER")
                      .build()) \
        .build()

    # 发起请求
    response: CreateMailgroupPermissionMemberResponse = client.mail.v1.mailgroup_permission_member.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.mail.v1.mailgroup_permission_member.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: CreateMailgroupPermissionMemberRequest = CreateMailgroupPermissionMemberRequest.builder() \
        .mailgroup_id("xxxxxxxxxxxxxxx 或 test_mail_group@xxx.xx") \
        .user_id_type("user_id") \
        .department_id_type("xxx") \
        .request_body(MailgroupPermissionMember.builder()
                      .user_id("xxxxxxxxxx")
                      .department_id("xxxxxxxxxx")
                      .email("xxx@xx.x")
                      .type("USER")
                      .build()) \
        .build()

    # 发起请求
    response: CreateMailgroupPermissionMemberResponse = await client.mail.v1.mailgroup_permission_member.acreate(
        request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.mail.v1.mailgroup_permission_member.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
