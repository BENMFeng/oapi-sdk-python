# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetJobRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.job_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetJobRequestBuilder":
        return GetJobRequestBuilder()


class GetJobRequestBuilder(object):

    def __init__(self) -> None:
        get_job_request = GetJobRequest()
        get_job_request.http_method = HttpMethod.GET
        get_job_request.uri = "/open-apis/corehr/v2/jobs/:job_id"
        get_job_request.token_types = {AccessTokenType.TENANT}
        self._get_job_request: GetJobRequest = get_job_request

    def job_id(self, job_id: str) -> "GetJobRequestBuilder":
        self._get_job_request.job_id = job_id
        self._get_job_request.paths["job_id"] = str(job_id)
        return self

    def build(self) -> GetJobRequest:
        return self._get_job_request
