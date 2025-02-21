# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.storage as windows_storage

from winrt.windows.media.apprecording import AppRecordingSaveScreenshotOption

Self = typing.TypeVar('Self')

@typing.final
class AppRecordingManager_Static(type):
    def get_default(cls) -> typing.Optional[AppRecordingManager]: ...

@typing.final
class AppRecordingManager(winrt.system.Object, metaclass=AppRecordingManager_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppRecordingManager: ...
    def get_status(self) -> typing.Optional[AppRecordingStatus]: ...
    def record_time_span_to_file_async(self, start_time: datetime.datetime, duration: datetime.timedelta, file: typing.Optional[windows_storage.StorageFile], /) -> windows_foundation.IAsyncOperation[AppRecordingResult]: ...
    def save_screenshot_to_files_async(self, folder: typing.Optional[windows_storage.StorageFolder], filename_prefix: str, option: AppRecordingSaveScreenshotOption, requested_formats: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[AppRecordingSaveScreenshotResult]: ...
    def start_recording_to_file_async(self, file: typing.Optional[windows_storage.StorageFile], /) -> windows_foundation.IAsyncOperation[AppRecordingResult]: ...
    @_property
    def supported_screenshot_media_encoding_subtypes(self) -> typing.Optional[windows_foundation_collections.IVectorView[str]]: ...

@typing.final
class AppRecordingResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppRecordingResult: ...
    @_property
    def duration(self) -> datetime.timedelta: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def is_file_truncated(self) -> bool: ...
    @_property
    def succeeded(self) -> bool: ...

@typing.final
class AppRecordingSaveScreenshotResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppRecordingSaveScreenshotResult: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def saved_screenshot_infos(self) -> typing.Optional[windows_foundation_collections.IVectorView[AppRecordingSavedScreenshotInfo]]: ...
    @_property
    def succeeded(self) -> bool: ...

@typing.final
class AppRecordingSavedScreenshotInfo(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppRecordingSavedScreenshotInfo: ...
    @_property
    def file(self) -> typing.Optional[windows_storage.StorageFile]: ...
    @_property
    def media_encoding_subtype(self) -> str: ...

@typing.final
class AppRecordingStatus(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppRecordingStatus: ...
    @_property
    def can_record(self) -> bool: ...
    @_property
    def can_record_time_span(self) -> bool: ...
    @_property
    def details(self) -> typing.Optional[AppRecordingStatusDetails]: ...
    @_property
    def historical_buffer_duration(self) -> datetime.timedelta: ...

@typing.final
class AppRecordingStatusDetails(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppRecordingStatusDetails: ...
    @_property
    def is_any_app_broadcasting(self) -> bool: ...
    @_property
    def is_app_inactive(self) -> bool: ...
    @_property
    def is_blocked_for_app(self) -> bool: ...
    @_property
    def is_capture_resource_unavailable(self) -> bool: ...
    @_property
    def is_disabled_by_system(self) -> bool: ...
    @_property
    def is_disabled_by_user(self) -> bool: ...
    @_property
    def is_game_stream_in_progress(self) -> bool: ...
    @_property
    def is_gpu_constrained(self) -> bool: ...
    @_property
    def is_time_span_recording_disabled(self) -> bool: ...

