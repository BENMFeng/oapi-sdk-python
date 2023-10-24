# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_probation_assessment_request import CreateProbationAssessmentRequest
from ..model.create_probation_assessment_response import CreateProbationAssessmentResponse
from ..model.delete_probation_assessment_request import DeleteProbationAssessmentRequest
from ..model.delete_probation_assessment_response import DeleteProbationAssessmentResponse
from ..model.patch_probation_assessment_request import PatchProbationAssessmentRequest
from ..model.patch_probation_assessment_response import PatchProbationAssessmentResponse


class ProbationAssessment(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateProbationAssessmentRequest,
               option: Optional[RequestOption] = None) -> CreateProbationAssessmentResponse:
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
        response: CreateProbationAssessmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     CreateProbationAssessmentResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteProbationAssessmentRequest,
               option: Optional[RequestOption] = None) -> DeleteProbationAssessmentResponse:
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
        response: DeleteProbationAssessmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     DeleteProbationAssessmentResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchProbationAssessmentRequest,
              option: Optional[RequestOption] = None) -> PatchProbationAssessmentResponse:
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
        response: PatchProbationAssessmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                    PatchProbationAssessmentResponse)
        response.raw = resp

        return response
