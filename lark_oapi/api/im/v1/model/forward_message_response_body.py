# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .mention import Mention
from .message_body import MessageBody
from .sender import Sender


class ForwardMessageResponseBody(object):
    _types = {
        "message_id": str,
        "root_id": str,
        "parent_id": str,
        "thread_id": str,
        "msg_type": str,
        "create_time": int,
        "update_time": int,
        "deleted": bool,
        "updated": bool,
        "chat_id": str,
        "sender": Sender,
        "body": MessageBody,
        "mentions": List[Mention],
        "upper_message_id": str,
    }

    def __init__(self, d=None):
        self.message_id: Optional[str] = None
        self.root_id: Optional[str] = None
        self.parent_id: Optional[str] = None
        self.thread_id: Optional[str] = None
        self.msg_type: Optional[str] = None
        self.create_time: Optional[int] = None
        self.update_time: Optional[int] = None
        self.deleted: Optional[bool] = None
        self.updated: Optional[bool] = None
        self.chat_id: Optional[str] = None
        self.sender: Optional[Sender] = None
        self.body: Optional[MessageBody] = None
        self.mentions: Optional[List[Mention]] = None
        self.upper_message_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ForwardMessageResponseBodyBuilder":
        return ForwardMessageResponseBodyBuilder()


class ForwardMessageResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._forward_message_response_body = ForwardMessageResponseBody()

    def message_id(self, message_id: str) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.message_id = message_id
        return self

    def root_id(self, root_id: str) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.root_id = root_id
        return self

    def parent_id(self, parent_id: str) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.parent_id = parent_id
        return self

    def thread_id(self, thread_id: str) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.thread_id = thread_id
        return self

    def msg_type(self, msg_type: str) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.msg_type = msg_type
        return self

    def create_time(self, create_time: int) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.create_time = create_time
        return self

    def update_time(self, update_time: int) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.update_time = update_time
        return self

    def deleted(self, deleted: bool) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.deleted = deleted
        return self

    def updated(self, updated: bool) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.updated = updated
        return self

    def chat_id(self, chat_id: str) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.chat_id = chat_id
        return self

    def sender(self, sender: Sender) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.sender = sender
        return self

    def body(self, body: MessageBody) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.body = body
        return self

    def mentions(self, mentions: List[Mention]) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.mentions = mentions
        return self

    def upper_message_id(self, upper_message_id: str) -> "ForwardMessageResponseBodyBuilder":
        self._forward_message_response_body.upper_message_id = upper_message_id
        return self

    def build(self) -> "ForwardMessageResponseBody":
        return self._forward_message_response_body
