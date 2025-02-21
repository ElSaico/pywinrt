# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system

Self = typing.TypeVar('Self')

@typing.final
class AutomationConnection(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AutomationConnection: ...
    @_property
    def app_user_model_id(self) -> str: ...
    @_property
    def executable_file_name(self) -> str: ...
    @_property
    def is_remote_system(self) -> bool: ...

@typing.final
class AutomationConnectionBoundObject(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AutomationConnectionBoundObject: ...
    @_property
    def connection(self) -> typing.Optional[AutomationConnection]: ...

@typing.final
class AutomationElement(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AutomationElement: ...
    @_property
    def app_user_model_id(self) -> str: ...
    @_property
    def executable_file_name(self) -> str: ...
    @_property
    def is_remote_system(self) -> bool: ...

@typing.final
class AutomationTextRange(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AutomationTextRange: ...

