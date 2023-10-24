# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MyAiAvPluginCardStatus(object):
    _types = {
        "from_status": str,
        "to_status": str,
    }

    def __init__(self, d=None):
        self.from_status: Optional[str] = None
        self.to_status: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiAvPluginCardStatusBuilder":
        return MyAiAvPluginCardStatusBuilder()


class MyAiAvPluginCardStatusBuilder(object):
    def __init__(self) -> None:
        self._my_ai_av_plugin_card_status = MyAiAvPluginCardStatus()

    def from_status(self, from_status: str) -> "MyAiAvPluginCardStatusBuilder":
        self._my_ai_av_plugin_card_status.from_status = from_status
        return self

    def to_status(self, to_status: str) -> "MyAiAvPluginCardStatusBuilder":
        self._my_ai_av_plugin_card_status.to_status = to_status
        return self

    def build(self) -> "MyAiAvPluginCardStatus":
        return self._my_ai_av_plugin_card_status
