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
class AppContainerNameAndAccess:
    app_container_name: str
    access_mask: winrt.system.UInt32
    def __init__(self, app_container_name: str, access_mask: winrt.system.UInt32) -> None: ...

@typing.final
class SecurityDescriptorHelpers_Static(type):
    def get_sddl_for_app_container_names(cls, access_requests: winrt.system.Array[AppContainerNameAndAccess], principal_string_sid: str, principal_access_mask: winrt.system.UInt32, /) -> str: ...
    def get_security_descriptor_bytes_from_app_container_names(cls, access_requests: winrt.system.Array[AppContainerNameAndAccess], principal_string_sid: str, principal_access_mask: winrt.system.UInt32, /) -> winrt.system.UInt8: ...

@typing.final
class SecurityDescriptorHelpers(winrt.system.Object, metaclass=SecurityDescriptorHelpers_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SecurityDescriptorHelpers: ...

