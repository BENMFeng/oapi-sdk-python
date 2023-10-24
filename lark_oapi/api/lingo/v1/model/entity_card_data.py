# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class EntityCardData(object):
    _types = {
        "card": str,
        "id": str,
        "key": str,
        "card_type": int,
        "template_name": str,
    }

    def __init__(self, d=None):
        self.card: Optional[str] = None
        self.id: Optional[str] = None
        self.key: Optional[str] = None
        self.card_type: Optional[int] = None
        self.template_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EntityCardDataBuilder":
        return EntityCardDataBuilder()


class EntityCardDataBuilder(object):
    def __init__(self) -> None:
        self._entity_card_data = EntityCardData()

    def card(self, card: str) -> "EntityCardDataBuilder":
        self._entity_card_data.card = card
        return self

    def id(self, id: str) -> "EntityCardDataBuilder":
        self._entity_card_data.id = id
        return self

    def key(self, key: str) -> "EntityCardDataBuilder":
        self._entity_card_data.key = key
        return self

    def card_type(self, card_type: int) -> "EntityCardDataBuilder":
        self._entity_card_data.card_type = card_type
        return self

    def template_name(self, template_name: str) -> "EntityCardDataBuilder":
        self._entity_card_data.template_name = template_name
        return self

    def build(self) -> "EntityCardData":
        return self._entity_card_data
