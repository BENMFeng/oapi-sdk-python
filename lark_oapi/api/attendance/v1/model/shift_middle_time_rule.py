# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ShiftMiddleTimeRule(object):
    _types = {
        "middle_time_type": int,
        "fixed_middle_time": str,
    }

    def __init__(self, d=None):
        self.middle_time_type: Optional[int] = None
        self.fixed_middle_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ShiftMiddleTimeRuleBuilder":
        return ShiftMiddleTimeRuleBuilder()


class ShiftMiddleTimeRuleBuilder(object):
    def __init__(self) -> None:
        self._shift_middle_time_rule = ShiftMiddleTimeRule()

    def middle_time_type(self, middle_time_type: int) -> "ShiftMiddleTimeRuleBuilder":
        self._shift_middle_time_rule.middle_time_type = middle_time_type
        return self

    def fixed_middle_time(self, fixed_middle_time: str) -> "ShiftMiddleTimeRuleBuilder":
        self._shift_middle_time_rule.fixed_middle_time = fixed_middle_time
        return self

    def build(self) -> "ShiftMiddleTimeRule":
        return self._shift_middle_time_rule
