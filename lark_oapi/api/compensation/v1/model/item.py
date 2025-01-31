# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n_content import I18nContent
from .i18n_content import I18nContent


class Item(object):
    _types = {
        "id": str,
        "name": str,
        "description": str,
        "category_id": str,
        "value_type": str,
        "pay_off_frequency_type": str,
        "decimal_places": int,
        "active_status": int,
        "i18n_names": List[I18nContent],
        "i18n_descriptions": List[I18nContent],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.category_id: Optional[str] = None
        self.value_type: Optional[str] = None
        self.pay_off_frequency_type: Optional[str] = None
        self.decimal_places: Optional[int] = None
        self.active_status: Optional[int] = None
        self.i18n_names: Optional[List[I18nContent]] = None
        self.i18n_descriptions: Optional[List[I18nContent]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ItemBuilder":
        return ItemBuilder()


class ItemBuilder(object):
    def __init__(self) -> None:
        self._item = Item()

    def id(self, id: str) -> "ItemBuilder":
        self._item.id = id
        return self

    def name(self, name: str) -> "ItemBuilder":
        self._item.name = name
        return self

    def description(self, description: str) -> "ItemBuilder":
        self._item.description = description
        return self

    def category_id(self, category_id: str) -> "ItemBuilder":
        self._item.category_id = category_id
        return self

    def value_type(self, value_type: str) -> "ItemBuilder":
        self._item.value_type = value_type
        return self

    def pay_off_frequency_type(self, pay_off_frequency_type: str) -> "ItemBuilder":
        self._item.pay_off_frequency_type = pay_off_frequency_type
        return self

    def decimal_places(self, decimal_places: int) -> "ItemBuilder":
        self._item.decimal_places = decimal_places
        return self

    def active_status(self, active_status: int) -> "ItemBuilder":
        self._item.active_status = active_status
        return self

    def i18n_names(self, i18n_names: List[I18nContent]) -> "ItemBuilder":
        self._item.i18n_names = i18n_names
        return self

    def i18n_descriptions(self, i18n_descriptions: List[I18nContent]) -> "ItemBuilder":
        self._item.i18n_descriptions = i18n_descriptions
        return self

    def build(self) -> "Item":
        return self._item
