# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.generate_caldav_conf_setting_request import GenerateCaldavConfSettingRequest
from ..model.generate_caldav_conf_setting_response import GenerateCaldavConfSettingResponse


class Setting(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def generate_caldav_conf(self, request: GenerateCaldavConfSettingRequest,
                             option: Optional[RequestOption] = None) -> GenerateCaldavConfSettingResponse:
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
        response: GenerateCaldavConfSettingResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     GenerateCaldavConfSettingResponse)
        response.raw = resp

        return response

    async def agenerate_caldav_conf(self, request: GenerateCaldavConfSettingRequest,
                                    option: Optional[RequestOption] = None) -> GenerateCaldavConfSettingResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GenerateCaldavConfSettingResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     GenerateCaldavConfSettingResponse)
        response.raw = resp

        return response
