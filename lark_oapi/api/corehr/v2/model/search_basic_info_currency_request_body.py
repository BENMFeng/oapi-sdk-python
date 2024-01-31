# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class SearchBasicInfoCurrencyRequestBody(object):
    _types = {
        "currency_id_list": List[str],
        "status_list": List[int],
    }

    def __init__(self, d=None):
        self.currency_id_list: Optional[List[str]] = None
        self.status_list: Optional[List[int]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchBasicInfoCurrencyRequestBodyBuilder":
        return SearchBasicInfoCurrencyRequestBodyBuilder()


class SearchBasicInfoCurrencyRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._search_basic_info_currency_request_body = SearchBasicInfoCurrencyRequestBody()

    def currency_id_list(self, currency_id_list: List[str]) -> "SearchBasicInfoCurrencyRequestBodyBuilder":
        self._search_basic_info_currency_request_body.currency_id_list = currency_id_list
        return self

    def status_list(self, status_list: List[int]) -> "SearchBasicInfoCurrencyRequestBodyBuilder":
        self._search_basic_info_currency_request_body.status_list = status_list
        return self

    def build(self) -> "SearchBasicInfoCurrencyRequestBody":
        return self._search_basic_info_currency_request_body
