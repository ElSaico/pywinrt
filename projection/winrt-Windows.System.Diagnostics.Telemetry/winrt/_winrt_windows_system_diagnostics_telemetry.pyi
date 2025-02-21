# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system

from winrt.windows.system.diagnostics.telemetry import PlatformTelemetryRegistrationStatus

Self = typing.TypeVar('Self')

@typing.final
class PlatformTelemetryClient_Static(type):
    @typing.overload
    def register(cls, id: str, /) -> typing.Optional[PlatformTelemetryRegistrationResult]: ...
    @typing.overload
    def register(cls, id: str, settings: typing.Optional[PlatformTelemetryRegistrationSettings], /) -> typing.Optional[PlatformTelemetryRegistrationResult]: ...

@typing.final
class PlatformTelemetryClient(winrt.system.Object, metaclass=PlatformTelemetryClient_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PlatformTelemetryClient: ...

@typing.final
class PlatformTelemetryRegistrationResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PlatformTelemetryRegistrationResult: ...
    @_property
    def status(self) -> PlatformTelemetryRegistrationStatus: ...

@typing.final
class PlatformTelemetryRegistrationSettings(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PlatformTelemetryRegistrationSettings: ...
    def __new__(cls: typing.Type[PlatformTelemetryRegistrationSettings]) -> PlatformTelemetryRegistrationSettings:...
    @_property
    def upload_quota_size(self) -> winrt.system.UInt32: ...
    @upload_quota_size.setter
    def upload_quota_size(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def storage_size(self) -> winrt.system.UInt32: ...
    @storage_size.setter
    def storage_size(self, value: winrt.system.UInt32) -> None: ...

