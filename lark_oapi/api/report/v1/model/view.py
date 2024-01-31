# Code generated by Lark OpenAPI.

from lark_oapi.core.construct import init


class View(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ViewBuilder":
        return ViewBuilder()


class ViewBuilder(object):
    def __init__(self) -> None:
        self._view = View()

    def build(self) -> "View":
        return self._view
