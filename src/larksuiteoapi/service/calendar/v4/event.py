# -*- coding: UTF-8 -*-
# Code generated by lark suite oapi sdk gen

from typing import Callable

from ....config import Config
from ....context import Context
from ....event.event import set_event_callback

from .model import *


class CalendarChangedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, CalendarChangedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, CalendarChangedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, CalendarChangedEvent], Any]) -> None
        handler = CalendarChangedEventHandler(callback)
        set_event_callback(conf, "calendar.calendar.changed_v4",
                          handler.handle, clazz=CalendarChangedEvent)


class CalendarAclCreatedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, CalendarAclCreatedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, CalendarAclCreatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, CalendarAclCreatedEvent], Any]) -> None
        handler = CalendarAclCreatedEventHandler(callback)
        set_event_callback(conf, "calendar.calendar.acl.created_v4",
                          handler.handle, clazz=CalendarAclCreatedEvent)


class CalendarAclDeletedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, CalendarAclDeletedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, CalendarAclDeletedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, CalendarAclDeletedEvent], Any]) -> None
        handler = CalendarAclDeletedEventHandler(callback)
        set_event_callback(conf, "calendar.calendar.acl.deleted_v4",
                          handler.handle, clazz=CalendarAclDeletedEvent)


class CalendarEventChangedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, CalendarEventChangedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, CalendarEventChangedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, CalendarEventChangedEvent], Any]) -> None
        handler = CalendarEventChangedEventHandler(callback)
        set_event_callback(conf, "calendar.calendar.event.changed_v4",
                          handler.handle, clazz=CalendarEventChangedEvent)
