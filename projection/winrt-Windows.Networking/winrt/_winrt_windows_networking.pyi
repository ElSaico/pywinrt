# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.networking.connectivity as windows_networking_connectivity

from winrt.windows.networking import DomainNameType, HostNameSortOptions, HostNameType

Self = typing.TypeVar('Self')

@typing.final
class EndpointPair(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> EndpointPair: ...
    def __new__(cls: typing.Type[EndpointPair], local_host_name: typing.Optional[HostName], local_service_name: str, remote_host_name: typing.Optional[HostName], remote_service_name: str) -> EndpointPair:...
    @_property
    def remote_service_name(self) -> str: ...
    @remote_service_name.setter
    def remote_service_name(self, value: str) -> None: ...
    @_property
    def remote_host_name(self) -> typing.Optional[HostName]: ...
    @remote_host_name.setter
    def remote_host_name(self, value: typing.Optional[HostName]) -> None: ...
    @_property
    def local_service_name(self) -> str: ...
    @local_service_name.setter
    def local_service_name(self, value: str) -> None: ...
    @_property
    def local_host_name(self) -> typing.Optional[HostName]: ...
    @local_host_name.setter
    def local_host_name(self, value: typing.Optional[HostName]) -> None: ...

@typing.final
class HostName_Static(type):
    def compare(cls, value1: str, value2: str, /) -> winrt.system.Int32: ...

@typing.final
class HostName(winrt.system.Object, metaclass=HostName_Static):
    def __str__(self) -> str: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> HostName: ...
    def __new__(cls: typing.Type[HostName], host_name: str) -> HostName:...
    def is_equal(self, host_name: typing.Optional[HostName], /) -> bool: ...
    def to_string(self) -> str: ...
    @_property
    def canonical_name(self) -> str: ...
    @_property
    def display_name(self) -> str: ...
    @_property
    def i_p_information(self) -> typing.Optional[windows_networking_connectivity.IPInformation]: ...
    @_property
    def raw_name(self) -> str: ...
    @_property
    def type(self) -> HostNameType: ...

