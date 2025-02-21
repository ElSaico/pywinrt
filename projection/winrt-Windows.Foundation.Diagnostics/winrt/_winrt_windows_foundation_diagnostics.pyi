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
import winrt.windows.storage as windows_storage

from winrt.windows.foundation.diagnostics import CausalityRelation, CausalitySource, CausalitySynchronousWork, CausalityTraceLevel, ErrorOptions, LoggingFieldFormat, LoggingLevel, LoggingOpcode

Self = typing.TypeVar('Self')

@typing.final
class AsyncCausalityTracer_Static(type):
    def trace_operation_completion(cls, trace_level: CausalityTraceLevel, source: CausalitySource, platform_id: _uuid.UUID, operation_id: winrt.system.UInt64, status: windows_foundation.AsyncStatus, /) -> None: ...
    def trace_operation_creation(cls, trace_level: CausalityTraceLevel, source: CausalitySource, platform_id: _uuid.UUID, operation_id: winrt.system.UInt64, operation_name: str, related_context: winrt.system.UInt64, /) -> None: ...
    def trace_operation_relation(cls, trace_level: CausalityTraceLevel, source: CausalitySource, platform_id: _uuid.UUID, operation_id: winrt.system.UInt64, relation: CausalityRelation, /) -> None: ...
    def trace_synchronous_work_completion(cls, trace_level: CausalityTraceLevel, source: CausalitySource, work: CausalitySynchronousWork, /) -> None: ...
    def trace_synchronous_work_start(cls, trace_level: CausalityTraceLevel, source: CausalitySource, platform_id: _uuid.UUID, operation_id: winrt.system.UInt64, work: CausalitySynchronousWork, /) -> None: ...
    def add_tracing_status_changed(cls, handler: windows_foundation.EventHandler[TracingStatusChangedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_tracing_status_changed(cls, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...

@typing.final
class AsyncCausalityTracer(winrt.system.Object, metaclass=AsyncCausalityTracer_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AsyncCausalityTracer: ...

@typing.final
class ErrorDetails_Static(type):
    def create_from_h_result_async(cls, error_code: winrt.system.Int32, /) -> windows_foundation.IAsyncOperation[ErrorDetails]: ...

@typing.final
class ErrorDetails(winrt.system.Object, metaclass=ErrorDetails_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ErrorDetails: ...
    @_property
    def description(self) -> str: ...
    @_property
    def help_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @_property
    def long_description(self) -> str: ...

@typing.final
class FileLoggingSession(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> FileLoggingSession: ...
    def __new__(cls: typing.Type[FileLoggingSession], name: str) -> FileLoggingSession:...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], /) -> None: ...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], max_level: LoggingLevel, /) -> None: ...
    def close(self) -> None: ...
    def close_and_save_to_file_async(self) -> windows_foundation.IAsyncOperation[windows_storage.StorageFile]: ...
    def remove_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], /) -> None: ...
    def add_log_file_generated(self, handler: windows_foundation.TypedEventHandler[IFileLoggingSession, LogFileGeneratedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_log_file_generated(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def name(self) -> str: ...

@typing.final
class LogFileGeneratedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LogFileGeneratedEventArgs: ...
    @_property
    def file(self) -> typing.Optional[windows_storage.StorageFile]: ...

@typing.final
class LoggingActivity(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LoggingActivity: ...
    @typing.overload
    def __new__(cls: typing.Type[LoggingActivity], activity_name: str, logging_channel: typing.Optional[ILoggingChannel]) -> LoggingActivity:...
    @typing.overload
    def __new__(cls: typing.Type[LoggingActivity], activity_name: str, logging_channel: typing.Optional[ILoggingChannel], level: LoggingLevel) -> LoggingActivity:...
    def close(self) -> None: ...
    @typing.overload
    def is_enabled(self) -> bool: ...
    @typing.overload
    def is_enabled(self, level: LoggingLevel, /) -> bool: ...
    @typing.overload
    def is_enabled(self, level: LoggingLevel, keywords: winrt.system.Int64, /) -> bool: ...
    @typing.overload
    def log_event(self, event_name: str, /) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], /) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, /) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, options: typing.Optional[LoggingOptions], /) -> None: ...
    @typing.overload
    def start_activity(self, start_event_name: str, /) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], /) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, /) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, options: typing.Optional[LoggingOptions], /) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def stop_activity(self, stop_event_name: str, /) -> None: ...
    @typing.overload
    def stop_activity(self, stop_event_name: str, fields: typing.Optional[LoggingFields], /) -> None: ...
    @typing.overload
    def stop_activity(self, stop_event_name: str, fields: typing.Optional[LoggingFields], options: typing.Optional[LoggingOptions], /) -> None: ...
    @_property
    def id(self) -> _uuid.UUID: ...
    @_property
    def name(self) -> str: ...
    @_property
    def channel(self) -> typing.Optional[LoggingChannel]: ...

@typing.final
class LoggingChannel(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LoggingChannel: ...
    @typing.overload
    def __new__(cls: typing.Type[LoggingChannel], name: str, options: typing.Optional[LoggingChannelOptions]) -> LoggingChannel:...
    @typing.overload
    def __new__(cls: typing.Type[LoggingChannel], name: str, options: typing.Optional[LoggingChannelOptions], id: _uuid.UUID) -> LoggingChannel:...
    @typing.overload
    def __new__(cls: typing.Type[LoggingChannel], name: str) -> LoggingChannel:...
    def close(self) -> None: ...
    @typing.overload
    def is_enabled(self) -> bool: ...
    @typing.overload
    def is_enabled(self, level: LoggingLevel, /) -> bool: ...
    @typing.overload
    def is_enabled(self, level: LoggingLevel, keywords: winrt.system.Int64, /) -> bool: ...
    @typing.overload
    def log_event(self, event_name: str, /) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], /) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, /) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, options: typing.Optional[LoggingOptions], /) -> None: ...
    @typing.overload
    def log_message(self, event_string: str, /) -> None: ...
    @typing.overload
    def log_message(self, event_string: str, level: LoggingLevel, /) -> None: ...
    @typing.overload
    def log_value_pair(self, value1: str, value2: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def log_value_pair(self, value1: str, value2: winrt.system.Int32, level: LoggingLevel, /) -> None: ...
    @typing.overload
    def start_activity(self, start_event_name: str, /) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], /) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, /) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, options: typing.Optional[LoggingOptions], /) -> typing.Optional[LoggingActivity]: ...
    def add_logging_enabled(self, handler: windows_foundation.TypedEventHandler[ILoggingChannel, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_logging_enabled(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def enabled(self) -> bool: ...
    @_property
    def level(self) -> LoggingLevel: ...
    @_property
    def name(self) -> str: ...
    @_property
    def id(self) -> _uuid.UUID: ...

@typing.final
class LoggingChannelOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LoggingChannelOptions: ...
    @typing.overload
    def __new__(cls: typing.Type[LoggingChannelOptions]) -> LoggingChannelOptions:...
    @typing.overload
    def __new__(cls: typing.Type[LoggingChannelOptions], group: _uuid.UUID) -> LoggingChannelOptions:...
    @_property
    def group(self) -> _uuid.UUID: ...
    @group.setter
    def group(self, value: _uuid.UUID) -> None: ...

@typing.final
class LoggingFields(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LoggingFields: ...
    def __new__(cls: typing.Type[LoggingFields]) -> LoggingFields:...
    @typing.overload
    def add_boolean(self, name: str, value: bool, /) -> None: ...
    @typing.overload
    def add_boolean(self, name: str, value: bool, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_boolean(self, name: str, value: bool, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_boolean_array(self, name: str, value: winrt.system.Array[bool], /) -> None: ...
    @typing.overload
    def add_boolean_array(self, name: str, value: winrt.system.Array[bool], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_boolean_array(self, name: str, value: winrt.system.Array[bool], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_char16(self, name: str, value: winrt.system.Char16, /) -> None: ...
    @typing.overload
    def add_char16(self, name: str, value: winrt.system.Char16, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_char16(self, name: str, value: winrt.system.Char16, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_char16_array(self, name: str, value: winrt.system.Array[winrt.system.Char16], /) -> None: ...
    @typing.overload
    def add_char16_array(self, name: str, value: winrt.system.Array[winrt.system.Char16], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_char16_array(self, name: str, value: winrt.system.Array[winrt.system.Char16], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_date_time(self, name: str, value: datetime.datetime, /) -> None: ...
    @typing.overload
    def add_date_time(self, name: str, value: datetime.datetime, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_date_time(self, name: str, value: datetime.datetime, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_date_time_array(self, name: str, value: winrt.system.Array[datetime.datetime], /) -> None: ...
    @typing.overload
    def add_date_time_array(self, name: str, value: winrt.system.Array[datetime.datetime], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_date_time_array(self, name: str, value: winrt.system.Array[datetime.datetime], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_double(self, name: str, value: winrt.system.Double, /) -> None: ...
    @typing.overload
    def add_double(self, name: str, value: winrt.system.Double, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_double(self, name: str, value: winrt.system.Double, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_double_array(self, name: str, value: winrt.system.Array[winrt.system.Double], /) -> None: ...
    @typing.overload
    def add_double_array(self, name: str, value: winrt.system.Array[winrt.system.Double], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_double_array(self, name: str, value: winrt.system.Array[winrt.system.Double], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_empty(self, name: str, /) -> None: ...
    @typing.overload
    def add_empty(self, name: str, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_empty(self, name: str, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_guid(self, name: str, value: _uuid.UUID, /) -> None: ...
    @typing.overload
    def add_guid(self, name: str, value: _uuid.UUID, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_guid(self, name: str, value: _uuid.UUID, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_guid_array(self, name: str, value: winrt.system.Array[_uuid.UUID], /) -> None: ...
    @typing.overload
    def add_guid_array(self, name: str, value: winrt.system.Array[_uuid.UUID], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_guid_array(self, name: str, value: winrt.system.Array[_uuid.UUID], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_int16(self, name: str, value: winrt.system.Int16, /) -> None: ...
    @typing.overload
    def add_int16(self, name: str, value: winrt.system.Int16, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_int16(self, name: str, value: winrt.system.Int16, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_int16_array(self, name: str, value: winrt.system.Array[winrt.system.Int16], /) -> None: ...
    @typing.overload
    def add_int16_array(self, name: str, value: winrt.system.Array[winrt.system.Int16], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_int16_array(self, name: str, value: winrt.system.Array[winrt.system.Int16], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_int32(self, name: str, value: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_int32(self, name: str, value: winrt.system.Int32, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_int32(self, name: str, value: winrt.system.Int32, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_int32_array(self, name: str, value: winrt.system.Array[winrt.system.Int32], /) -> None: ...
    @typing.overload
    def add_int32_array(self, name: str, value: winrt.system.Array[winrt.system.Int32], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_int32_array(self, name: str, value: winrt.system.Array[winrt.system.Int32], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_int64(self, name: str, value: winrt.system.Int64, /) -> None: ...
    @typing.overload
    def add_int64(self, name: str, value: winrt.system.Int64, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_int64(self, name: str, value: winrt.system.Int64, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_int64_array(self, name: str, value: winrt.system.Array[winrt.system.Int64], /) -> None: ...
    @typing.overload
    def add_int64_array(self, name: str, value: winrt.system.Array[winrt.system.Int64], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_int64_array(self, name: str, value: winrt.system.Array[winrt.system.Int64], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_point(self, name: str, value: windows_foundation.Point, /) -> None: ...
    @typing.overload
    def add_point(self, name: str, value: windows_foundation.Point, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_point(self, name: str, value: windows_foundation.Point, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_point_array(self, name: str, value: winrt.system.Array[windows_foundation.Point], /) -> None: ...
    @typing.overload
    def add_point_array(self, name: str, value: winrt.system.Array[windows_foundation.Point], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_point_array(self, name: str, value: winrt.system.Array[windows_foundation.Point], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_rect(self, name: str, value: windows_foundation.Rect, /) -> None: ...
    @typing.overload
    def add_rect(self, name: str, value: windows_foundation.Rect, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_rect(self, name: str, value: windows_foundation.Rect, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_rect_array(self, name: str, value: winrt.system.Array[windows_foundation.Rect], /) -> None: ...
    @typing.overload
    def add_rect_array(self, name: str, value: winrt.system.Array[windows_foundation.Rect], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_rect_array(self, name: str, value: winrt.system.Array[windows_foundation.Rect], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_single(self, name: str, value: winrt.system.Single, /) -> None: ...
    @typing.overload
    def add_single(self, name: str, value: winrt.system.Single, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_single(self, name: str, value: winrt.system.Single, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_single_array(self, name: str, value: winrt.system.Array[winrt.system.Single], /) -> None: ...
    @typing.overload
    def add_single_array(self, name: str, value: winrt.system.Array[winrt.system.Single], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_single_array(self, name: str, value: winrt.system.Array[winrt.system.Single], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_size(self, name: str, value: windows_foundation.Size, /) -> None: ...
    @typing.overload
    def add_size(self, name: str, value: windows_foundation.Size, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_size(self, name: str, value: windows_foundation.Size, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_size_array(self, name: str, value: winrt.system.Array[windows_foundation.Size], /) -> None: ...
    @typing.overload
    def add_size_array(self, name: str, value: winrt.system.Array[windows_foundation.Size], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_size_array(self, name: str, value: winrt.system.Array[windows_foundation.Size], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_string(self, name: str, value: str, /) -> None: ...
    @typing.overload
    def add_string(self, name: str, value: str, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_string(self, name: str, value: str, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_string_array(self, name: str, value: winrt.system.Array[str], /) -> None: ...
    @typing.overload
    def add_string_array(self, name: str, value: winrt.system.Array[str], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_string_array(self, name: str, value: winrt.system.Array[str], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_time_span(self, name: str, value: datetime.timedelta, /) -> None: ...
    @typing.overload
    def add_time_span(self, name: str, value: datetime.timedelta, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_time_span(self, name: str, value: datetime.timedelta, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_time_span_array(self, name: str, value: winrt.system.Array[datetime.timedelta], /) -> None: ...
    @typing.overload
    def add_time_span_array(self, name: str, value: winrt.system.Array[datetime.timedelta], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_time_span_array(self, name: str, value: winrt.system.Array[datetime.timedelta], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_uint16(self, name: str, value: winrt.system.UInt16, /) -> None: ...
    @typing.overload
    def add_uint16(self, name: str, value: winrt.system.UInt16, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_uint16(self, name: str, value: winrt.system.UInt16, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_uint16_array(self, name: str, value: winrt.system.Array[winrt.system.UInt16], /) -> None: ...
    @typing.overload
    def add_uint16_array(self, name: str, value: winrt.system.Array[winrt.system.UInt16], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_uint16_array(self, name: str, value: winrt.system.Array[winrt.system.UInt16], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_uint32(self, name: str, value: winrt.system.UInt32, /) -> None: ...
    @typing.overload
    def add_uint32(self, name: str, value: winrt.system.UInt32, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_uint32(self, name: str, value: winrt.system.UInt32, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_uint32_array(self, name: str, value: winrt.system.Array[winrt.system.UInt32], /) -> None: ...
    @typing.overload
    def add_uint32_array(self, name: str, value: winrt.system.Array[winrt.system.UInt32], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_uint32_array(self, name: str, value: winrt.system.Array[winrt.system.UInt32], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_uint64(self, name: str, value: winrt.system.UInt64, /) -> None: ...
    @typing.overload
    def add_uint64(self, name: str, value: winrt.system.UInt64, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_uint64(self, name: str, value: winrt.system.UInt64, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_uint64_array(self, name: str, value: winrt.system.Array[winrt.system.UInt64], /) -> None: ...
    @typing.overload
    def add_uint64_array(self, name: str, value: winrt.system.Array[winrt.system.UInt64], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_uint64_array(self, name: str, value: winrt.system.Array[winrt.system.UInt64], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_uint8(self, name: str, value: winrt.system.UInt8, /) -> None: ...
    @typing.overload
    def add_uint8(self, name: str, value: winrt.system.UInt8, format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_uint8(self, name: str, value: winrt.system.UInt8, format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def add_uint8_array(self, name: str, value: winrt.system.Array[winrt.system.UInt8], /) -> None: ...
    @typing.overload
    def add_uint8_array(self, name: str, value: winrt.system.Array[winrt.system.UInt8], format: LoggingFieldFormat, /) -> None: ...
    @typing.overload
    def add_uint8_array(self, name: str, value: winrt.system.Array[winrt.system.UInt8], format: LoggingFieldFormat, tags: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def begin_struct(self, name: str, /) -> None: ...
    @typing.overload
    def begin_struct(self, name: str, tags: winrt.system.Int32, /) -> None: ...
    def clear(self) -> None: ...
    def end_struct(self) -> None: ...

@typing.final
class LoggingOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LoggingOptions: ...
    @typing.overload
    def __new__(cls: typing.Type[LoggingOptions]) -> LoggingOptions:...
    @typing.overload
    def __new__(cls: typing.Type[LoggingOptions], keywords: winrt.system.Int64) -> LoggingOptions:...
    @_property
    def task(self) -> winrt.system.Int16: ...
    @task.setter
    def task(self, value: winrt.system.Int16) -> None: ...
    @_property
    def tags(self) -> winrt.system.Int32: ...
    @tags.setter
    def tags(self, value: winrt.system.Int32) -> None: ...
    @_property
    def related_activity_id(self) -> _uuid.UUID: ...
    @related_activity_id.setter
    def related_activity_id(self, value: _uuid.UUID) -> None: ...
    @_property
    def opcode(self) -> LoggingOpcode: ...
    @opcode.setter
    def opcode(self, value: LoggingOpcode) -> None: ...
    @_property
    def keywords(self) -> winrt.system.Int64: ...
    @keywords.setter
    def keywords(self, value: winrt.system.Int64) -> None: ...
    @_property
    def activity_id(self) -> _uuid.UUID: ...
    @activity_id.setter
    def activity_id(self, value: _uuid.UUID) -> None: ...

@typing.final
class LoggingSession(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LoggingSession: ...
    def __new__(cls: typing.Type[LoggingSession], name: str) -> LoggingSession:...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], /) -> None: ...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], max_level: LoggingLevel, /) -> None: ...
    def close(self) -> None: ...
    def remove_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], /) -> None: ...
    def save_to_file_async(self, folder: typing.Optional[windows_storage.IStorageFolder], file_name: str, /) -> windows_foundation.IAsyncOperation[windows_storage.StorageFile]: ...
    @_property
    def name(self) -> str: ...

@typing.final
class RuntimeBrokerErrorSettings(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RuntimeBrokerErrorSettings: ...
    def __new__(cls: typing.Type[RuntimeBrokerErrorSettings]) -> RuntimeBrokerErrorSettings:...
    def get_error_options(self) -> ErrorOptions: ...
    def set_error_options(self, value: ErrorOptions, /) -> None: ...

@typing.final
class TracingStatusChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TracingStatusChangedEventArgs: ...
    @_property
    def enabled(self) -> bool: ...
    @_property
    def trace_level(self) -> CausalityTraceLevel: ...

@typing.final
class IErrorReportingSettings(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IErrorReportingSettings: ...
    def get_error_options(self) -> ErrorOptions: ...
    def set_error_options(self, value: ErrorOptions, /) -> None: ...

@typing.final
class IFileLoggingSession(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IFileLoggingSession: ...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], /) -> None: ...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], max_level: LoggingLevel, /) -> None: ...
    def close(self) -> None: ...
    def close_and_save_to_file_async(self) -> windows_foundation.IAsyncOperation[windows_storage.StorageFile]: ...
    def remove_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], /) -> None: ...
    def add_log_file_generated(self, handler: windows_foundation.TypedEventHandler[IFileLoggingSession, LogFileGeneratedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_log_file_generated(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def name(self) -> str: ...

@typing.final
class ILoggingChannel(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ILoggingChannel: ...
    def close(self) -> None: ...
    @typing.overload
    def log_message(self, event_string: str, /) -> None: ...
    @typing.overload
    def log_message(self, event_string: str, level: LoggingLevel, /) -> None: ...
    @typing.overload
    def log_value_pair(self, value1: str, value2: winrt.system.Int32, /) -> None: ...
    @typing.overload
    def log_value_pair(self, value1: str, value2: winrt.system.Int32, level: LoggingLevel, /) -> None: ...
    def add_logging_enabled(self, handler: windows_foundation.TypedEventHandler[ILoggingChannel, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_logging_enabled(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def enabled(self) -> bool: ...
    @_property
    def level(self) -> LoggingLevel: ...
    @_property
    def name(self) -> str: ...

@typing.final
class ILoggingSession(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ILoggingSession: ...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], /) -> None: ...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], max_level: LoggingLevel, /) -> None: ...
    def close(self) -> None: ...
    def remove_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], /) -> None: ...
    def save_to_file_async(self, folder: typing.Optional[windows_storage.IStorageFolder], file_name: str, /) -> windows_foundation.IAsyncOperation[windows_storage.StorageFile]: ...
    @_property
    def name(self) -> str: ...

@typing.final
class ILoggingTarget(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ILoggingTarget: ...
    @typing.overload
    def is_enabled(self) -> bool: ...
    @typing.overload
    def is_enabled(self, level: LoggingLevel, /) -> bool: ...
    @typing.overload
    def is_enabled(self, level: LoggingLevel, keywords: winrt.system.Int64, /) -> bool: ...
    @typing.overload
    def log_event(self, event_name: str, /) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], /) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, /) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, options: typing.Optional[LoggingOptions], /) -> None: ...
    @typing.overload
    def start_activity(self, start_event_name: str, /) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], /) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, /) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, options: typing.Optional[LoggingOptions], /) -> typing.Optional[LoggingActivity]: ...

