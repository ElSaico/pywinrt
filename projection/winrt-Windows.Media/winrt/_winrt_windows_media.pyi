# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.applicationmodel.appservice as windows_applicationmodel_appservice
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.graphics.directx as windows_graphics_directx
import winrt.windows.graphics.directx.direct3d11 as windows_graphics_directx_direct3d11
import winrt.windows.graphics.imaging as windows_graphics_imaging
import winrt.windows.storage as windows_storage
import winrt.windows.storage.streams as windows_storage_streams

from winrt.windows.media import AudioBufferAccessMode, AudioProcessing, MediaPlaybackAutoRepeatMode, MediaPlaybackStatus, MediaPlaybackType, MediaTimelineControllerState, SoundLevel, SystemMediaTransportControlsButton, SystemMediaTransportControlsProperty

Self = typing.TypeVar('Self')

@typing.final
class MediaTimeRange:
    start: datetime.timedelta
    end: datetime.timedelta
    def __init__(self, start: datetime.timedelta, end: datetime.timedelta) -> None: ...

@typing.final
class AudioBuffer(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AudioBuffer: ...
    def close(self) -> None: ...
    def create_reference(self) -> typing.Optional[windows_foundation.IMemoryBufferReference]: ...
    @_property
    def length(self) -> winrt.system.UInt32: ...
    @length.setter
    def length(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def capacity(self) -> winrt.system.UInt32: ...

@typing.final
class AudioFrame(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AudioFrame: ...
    def __new__(cls: typing.Type[AudioFrame], capacity: winrt.system.UInt32) -> AudioFrame:...
    def close(self) -> None: ...
    def lock_buffer(self, mode: AudioBufferAccessMode, /) -> typing.Optional[AudioBuffer]: ...
    @_property
    def system_relative_time(self) -> typing.Optional[typing.Optional[datetime.timedelta]]: ...
    @system_relative_time.setter
    def system_relative_time(self, value: typing.Optional[typing.Optional[datetime.timedelta]]) -> None: ...
    @_property
    def relative_time(self) -> typing.Optional[typing.Optional[datetime.timedelta]]: ...
    @relative_time.setter
    def relative_time(self, value: typing.Optional[typing.Optional[datetime.timedelta]]) -> None: ...
    @_property
    def is_discontinuous(self) -> bool: ...
    @is_discontinuous.setter
    def is_discontinuous(self, value: bool) -> None: ...
    @_property
    def duration(self) -> typing.Optional[typing.Optional[datetime.timedelta]]: ...
    @duration.setter
    def duration(self, value: typing.Optional[typing.Optional[datetime.timedelta]]) -> None: ...
    @_property
    def extended_properties(self) -> typing.Optional[windows_foundation_collections.IPropertySet]: ...
    @_property
    def is_read_only(self) -> bool: ...
    @_property
    def type(self) -> str: ...

@typing.final
class AutoRepeatModeChangeRequestedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AutoRepeatModeChangeRequestedEventArgs: ...
    @_property
    def requested_auto_repeat_mode(self) -> MediaPlaybackAutoRepeatMode: ...

@typing.final
class ImageDisplayProperties(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ImageDisplayProperties: ...
    @_property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str) -> None: ...
    @_property
    def subtitle(self) -> str: ...
    @subtitle.setter
    def subtitle(self, value: str) -> None: ...

@typing.final
class MediaControl_Static(type):
    def add_channel_down_pressed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_channel_down_pressed(cls, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_channel_up_pressed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_channel_up_pressed(cls, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_fast_forward_pressed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_fast_forward_pressed(cls, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_next_track_pressed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_next_track_pressed(cls, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_pause_pressed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_pause_pressed(cls, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_play_pause_toggle_pressed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_play_pause_toggle_pressed(cls, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_play_pressed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_play_pressed(cls, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_previous_track_pressed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_previous_track_pressed(cls, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_record_pressed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_record_pressed(cls, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_rewind_pressed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_rewind_pressed(cls, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_sound_level_changed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_sound_level_changed(cls, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_stop_pressed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_stop_pressed(cls, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def track_name(cls) -> str: ...
    @track_name.setter
    def track_name(cls, value: str) -> None: ...
    @_property
    def is_playing(cls) -> bool: ...
    @is_playing.setter
    def is_playing(cls, value: bool) -> None: ...
    @_property
    def artist_name(cls) -> str: ...
    @artist_name.setter
    def artist_name(cls, value: str) -> None: ...
    @_property
    def album_art(cls) -> typing.Optional[windows_foundation.Uri]: ...
    @album_art.setter
    def album_art(cls, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def sound_level(cls) -> SoundLevel: ...

@typing.final
class MediaControl(winrt.system.Object, metaclass=MediaControl_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MediaControl: ...

@typing.final
class MediaExtensionManager(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MediaExtensionManager: ...
    def __new__(cls: typing.Type[MediaExtensionManager]) -> MediaExtensionManager:...
    @typing.overload
    def register_audio_decoder(self, activatable_class_id: str, input_subtype: _uuid.UUID, output_subtype: _uuid.UUID, /) -> None: ...
    @typing.overload
    def register_audio_decoder(self, activatable_class_id: str, input_subtype: _uuid.UUID, output_subtype: _uuid.UUID, configuration: typing.Optional[windows_foundation_collections.IPropertySet], /) -> None: ...
    @typing.overload
    def register_audio_encoder(self, activatable_class_id: str, input_subtype: _uuid.UUID, output_subtype: _uuid.UUID, /) -> None: ...
    @typing.overload
    def register_audio_encoder(self, activatable_class_id: str, input_subtype: _uuid.UUID, output_subtype: _uuid.UUID, configuration: typing.Optional[windows_foundation_collections.IPropertySet], /) -> None: ...
    @typing.overload
    def register_byte_stream_handler(self, activatable_class_id: str, file_extension: str, mime_type: str, /) -> None: ...
    @typing.overload
    def register_byte_stream_handler(self, activatable_class_id: str, file_extension: str, mime_type: str, configuration: typing.Optional[windows_foundation_collections.IPropertySet], /) -> None: ...
    def register_media_extension_for_app_service(self, extension: typing.Optional[IMediaExtension], connection: typing.Optional[windows_applicationmodel_appservice.AppServiceConnection], /) -> None: ...
    @typing.overload
    def register_scheme_handler(self, activatable_class_id: str, scheme: str, /) -> None: ...
    @typing.overload
    def register_scheme_handler(self, activatable_class_id: str, scheme: str, configuration: typing.Optional[windows_foundation_collections.IPropertySet], /) -> None: ...
    @typing.overload
    def register_video_decoder(self, activatable_class_id: str, input_subtype: _uuid.UUID, output_subtype: _uuid.UUID, /) -> None: ...
    @typing.overload
    def register_video_decoder(self, activatable_class_id: str, input_subtype: _uuid.UUID, output_subtype: _uuid.UUID, configuration: typing.Optional[windows_foundation_collections.IPropertySet], /) -> None: ...
    @typing.overload
    def register_video_encoder(self, activatable_class_id: str, input_subtype: _uuid.UUID, output_subtype: _uuid.UUID, /) -> None: ...
    @typing.overload
    def register_video_encoder(self, activatable_class_id: str, input_subtype: _uuid.UUID, output_subtype: _uuid.UUID, configuration: typing.Optional[windows_foundation_collections.IPropertySet], /) -> None: ...

@typing.final
class MediaMarkerTypes_Static(type):
    @_property
    def bookmark(cls) -> str: ...

@typing.final
class MediaMarkerTypes(winrt.system.Object, metaclass=MediaMarkerTypes_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MediaMarkerTypes: ...

@typing.final
class MediaProcessingTriggerDetails(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MediaProcessingTriggerDetails: ...
    @_property
    def arguments(self) -> typing.Optional[windows_foundation_collections.ValueSet]: ...

@typing.final
class MediaTimelineController(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MediaTimelineController: ...
    def __new__(cls: typing.Type[MediaTimelineController]) -> MediaTimelineController:...
    def pause(self) -> None: ...
    def resume(self) -> None: ...
    def start(self) -> None: ...
    def add_position_changed(self, position_changed_event_handler: windows_foundation.TypedEventHandler[MediaTimelineController, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_position_changed(self, event_cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_state_changed(self, state_changed_event_handler: windows_foundation.TypedEventHandler[MediaTimelineController, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_state_changed(self, event_cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_ended(self, event_handler: windows_foundation.TypedEventHandler[MediaTimelineController, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_ended(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_failed(self, event_handler: windows_foundation.TypedEventHandler[MediaTimelineController, MediaTimelineControllerFailedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_failed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def position(self) -> datetime.timedelta: ...
    @position.setter
    def position(self, value: datetime.timedelta) -> None: ...
    @_property
    def clock_rate(self) -> winrt.system.Double: ...
    @clock_rate.setter
    def clock_rate(self, value: winrt.system.Double) -> None: ...
    @_property
    def state(self) -> MediaTimelineControllerState: ...
    @_property
    def is_looping_enabled(self) -> bool: ...
    @is_looping_enabled.setter
    def is_looping_enabled(self, value: bool) -> None: ...
    @_property
    def duration(self) -> typing.Optional[typing.Optional[datetime.timedelta]]: ...
    @duration.setter
    def duration(self, value: typing.Optional[typing.Optional[datetime.timedelta]]) -> None: ...

@typing.final
class MediaTimelineControllerFailedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MediaTimelineControllerFailedEventArgs: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...

@typing.final
class MusicDisplayProperties(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MusicDisplayProperties: ...
    @_property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str) -> None: ...
    @_property
    def artist(self) -> str: ...
    @artist.setter
    def artist(self, value: str) -> None: ...
    @_property
    def album_artist(self) -> str: ...
    @album_artist.setter
    def album_artist(self, value: str) -> None: ...
    @_property
    def track_number(self) -> winrt.system.UInt32: ...
    @track_number.setter
    def track_number(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def album_title(self) -> str: ...
    @album_title.setter
    def album_title(self, value: str) -> None: ...
    @_property
    def genres(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...
    @_property
    def album_track_count(self) -> winrt.system.UInt32: ...
    @album_track_count.setter
    def album_track_count(self, value: winrt.system.UInt32) -> None: ...

@typing.final
class PlaybackPositionChangeRequestedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PlaybackPositionChangeRequestedEventArgs: ...
    @_property
    def requested_playback_position(self) -> datetime.timedelta: ...

@typing.final
class PlaybackRateChangeRequestedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PlaybackRateChangeRequestedEventArgs: ...
    @_property
    def requested_playback_rate(self) -> winrt.system.Double: ...

@typing.final
class ShuffleEnabledChangeRequestedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ShuffleEnabledChangeRequestedEventArgs: ...
    @_property
    def requested_shuffle_enabled(self) -> bool: ...

@typing.final
class SystemMediaTransportControls_Static(type):
    def get_for_current_view(cls) -> typing.Optional[SystemMediaTransportControls]: ...

@typing.final
class SystemMediaTransportControls(winrt.system.Object, metaclass=SystemMediaTransportControls_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SystemMediaTransportControls: ...
    def update_timeline_properties(self, timeline_properties: typing.Optional[SystemMediaTransportControlsTimelineProperties], /) -> None: ...
    def add_button_pressed(self, handler: windows_foundation.TypedEventHandler[SystemMediaTransportControls, SystemMediaTransportControlsButtonPressedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_button_pressed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_property_changed(self, handler: windows_foundation.TypedEventHandler[SystemMediaTransportControls, SystemMediaTransportControlsPropertyChangedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_property_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_auto_repeat_mode_change_requested(self, handler: windows_foundation.TypedEventHandler[SystemMediaTransportControls, AutoRepeatModeChangeRequestedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_auto_repeat_mode_change_requested(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_playback_position_change_requested(self, handler: windows_foundation.TypedEventHandler[SystemMediaTransportControls, PlaybackPositionChangeRequestedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_playback_position_change_requested(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_playback_rate_change_requested(self, handler: windows_foundation.TypedEventHandler[SystemMediaTransportControls, PlaybackRateChangeRequestedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_playback_rate_change_requested(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_shuffle_enabled_change_requested(self, handler: windows_foundation.TypedEventHandler[SystemMediaTransportControls, ShuffleEnabledChangeRequestedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_shuffle_enabled_change_requested(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def is_play_enabled(self) -> bool: ...
    @is_play_enabled.setter
    def is_play_enabled(self, value: bool) -> None: ...
    @_property
    def is_pause_enabled(self) -> bool: ...
    @is_pause_enabled.setter
    def is_pause_enabled(self, value: bool) -> None: ...
    @_property
    def is_next_enabled(self) -> bool: ...
    @is_next_enabled.setter
    def is_next_enabled(self, value: bool) -> None: ...
    @_property
    def is_previous_enabled(self) -> bool: ...
    @is_previous_enabled.setter
    def is_previous_enabled(self, value: bool) -> None: ...
    @_property
    def is_enabled(self) -> bool: ...
    @is_enabled.setter
    def is_enabled(self, value: bool) -> None: ...
    @_property
    def is_channel_down_enabled(self) -> bool: ...
    @is_channel_down_enabled.setter
    def is_channel_down_enabled(self, value: bool) -> None: ...
    @_property
    def is_fast_forward_enabled(self) -> bool: ...
    @is_fast_forward_enabled.setter
    def is_fast_forward_enabled(self, value: bool) -> None: ...
    @_property
    def is_channel_up_enabled(self) -> bool: ...
    @is_channel_up_enabled.setter
    def is_channel_up_enabled(self, value: bool) -> None: ...
    @_property
    def playback_status(self) -> MediaPlaybackStatus: ...
    @playback_status.setter
    def playback_status(self, value: MediaPlaybackStatus) -> None: ...
    @_property
    def is_stop_enabled(self) -> bool: ...
    @is_stop_enabled.setter
    def is_stop_enabled(self, value: bool) -> None: ...
    @_property
    def is_rewind_enabled(self) -> bool: ...
    @is_rewind_enabled.setter
    def is_rewind_enabled(self, value: bool) -> None: ...
    @_property
    def is_record_enabled(self) -> bool: ...
    @is_record_enabled.setter
    def is_record_enabled(self, value: bool) -> None: ...
    @_property
    def display_updater(self) -> typing.Optional[SystemMediaTransportControlsDisplayUpdater]: ...
    @_property
    def sound_level(self) -> SoundLevel: ...
    @_property
    def shuffle_enabled(self) -> bool: ...
    @shuffle_enabled.setter
    def shuffle_enabled(self, value: bool) -> None: ...
    @_property
    def playback_rate(self) -> winrt.system.Double: ...
    @playback_rate.setter
    def playback_rate(self, value: winrt.system.Double) -> None: ...
    @_property
    def auto_repeat_mode(self) -> MediaPlaybackAutoRepeatMode: ...
    @auto_repeat_mode.setter
    def auto_repeat_mode(self, value: MediaPlaybackAutoRepeatMode) -> None: ...

@typing.final
class SystemMediaTransportControlsButtonPressedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SystemMediaTransportControlsButtonPressedEventArgs: ...
    @_property
    def button(self) -> SystemMediaTransportControlsButton: ...

@typing.final
class SystemMediaTransportControlsDisplayUpdater(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SystemMediaTransportControlsDisplayUpdater: ...
    def clear_all(self) -> None: ...
    def copy_from_file_async(self, type: MediaPlaybackType, source: typing.Optional[windows_storage.StorageFile], /) -> windows_foundation.IAsyncOperation[bool]: ...
    def update(self) -> None: ...
    @_property
    def type(self) -> MediaPlaybackType: ...
    @type.setter
    def type(self, value: MediaPlaybackType) -> None: ...
    @_property
    def thumbnail(self) -> typing.Optional[windows_storage_streams.RandomAccessStreamReference]: ...
    @thumbnail.setter
    def thumbnail(self, value: typing.Optional[windows_storage_streams.RandomAccessStreamReference]) -> None: ...
    @_property
    def app_media_id(self) -> str: ...
    @app_media_id.setter
    def app_media_id(self, value: str) -> None: ...
    @_property
    def image_properties(self) -> typing.Optional[ImageDisplayProperties]: ...
    @_property
    def music_properties(self) -> typing.Optional[MusicDisplayProperties]: ...
    @_property
    def video_properties(self) -> typing.Optional[VideoDisplayProperties]: ...

@typing.final
class SystemMediaTransportControlsPropertyChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SystemMediaTransportControlsPropertyChangedEventArgs: ...
    @_property
    def property(self) -> SystemMediaTransportControlsProperty: ...

@typing.final
class SystemMediaTransportControlsTimelineProperties(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SystemMediaTransportControlsTimelineProperties: ...
    def __new__(cls: typing.Type[SystemMediaTransportControlsTimelineProperties]) -> SystemMediaTransportControlsTimelineProperties:...
    @_property
    def start_time(self) -> datetime.timedelta: ...
    @start_time.setter
    def start_time(self, value: datetime.timedelta) -> None: ...
    @_property
    def position(self) -> datetime.timedelta: ...
    @position.setter
    def position(self, value: datetime.timedelta) -> None: ...
    @_property
    def min_seek_time(self) -> datetime.timedelta: ...
    @min_seek_time.setter
    def min_seek_time(self, value: datetime.timedelta) -> None: ...
    @_property
    def max_seek_time(self) -> datetime.timedelta: ...
    @max_seek_time.setter
    def max_seek_time(self, value: datetime.timedelta) -> None: ...
    @_property
    def end_time(self) -> datetime.timedelta: ...
    @end_time.setter
    def end_time(self, value: datetime.timedelta) -> None: ...

@typing.final
class VideoDisplayProperties(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> VideoDisplayProperties: ...
    @_property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str) -> None: ...
    @_property
    def subtitle(self) -> str: ...
    @subtitle.setter
    def subtitle(self, value: str) -> None: ...
    @_property
    def genres(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...

@typing.final
class VideoEffects_Static(type):
    @_property
    def video_stabilization(cls) -> str: ...

@typing.final
class VideoEffects(winrt.system.Object, metaclass=VideoEffects_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> VideoEffects: ...

@typing.final
class VideoFrame_Static(type):
    @typing.overload
    def create_as_direct3_d11_surface_backed(cls, format: windows_graphics_directx.DirectXPixelFormat, width: winrt.system.Int32, height: winrt.system.Int32, /) -> typing.Optional[VideoFrame]: ...
    @typing.overload
    def create_as_direct3_d11_surface_backed(cls, format: windows_graphics_directx.DirectXPixelFormat, width: winrt.system.Int32, height: winrt.system.Int32, device: typing.Optional[windows_graphics_directx_direct3d11.IDirect3DDevice], /) -> typing.Optional[VideoFrame]: ...
    def create_with_direct3_d11_surface(cls, surface: typing.Optional[windows_graphics_directx_direct3d11.IDirect3DSurface], /) -> typing.Optional[VideoFrame]: ...
    def create_with_software_bitmap(cls, bitmap: typing.Optional[windows_graphics_imaging.SoftwareBitmap], /) -> typing.Optional[VideoFrame]: ...

@typing.final
class VideoFrame(winrt.system.Object, metaclass=VideoFrame_Static):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> VideoFrame: ...
    @typing.overload
    def __new__(cls: typing.Type[VideoFrame], format: windows_graphics_imaging.BitmapPixelFormat, width: winrt.system.Int32, height: winrt.system.Int32) -> VideoFrame:...
    @typing.overload
    def __new__(cls: typing.Type[VideoFrame], format: windows_graphics_imaging.BitmapPixelFormat, width: winrt.system.Int32, height: winrt.system.Int32, alpha: windows_graphics_imaging.BitmapAlphaMode) -> VideoFrame:...
    def close(self) -> None: ...
    @typing.overload
    def copy_to_async(self, frame: typing.Optional[VideoFrame], /) -> windows_foundation.IAsyncAction: ...
    @typing.overload
    def copy_to_async(self, frame: typing.Optional[VideoFrame], source_bounds: typing.Optional[windows_graphics_imaging.BitmapBounds], destination_bounds: typing.Optional[windows_graphics_imaging.BitmapBounds], /) -> windows_foundation.IAsyncAction: ...
    @_property
    def system_relative_time(self) -> typing.Optional[typing.Optional[datetime.timedelta]]: ...
    @system_relative_time.setter
    def system_relative_time(self, value: typing.Optional[typing.Optional[datetime.timedelta]]) -> None: ...
    @_property
    def relative_time(self) -> typing.Optional[typing.Optional[datetime.timedelta]]: ...
    @relative_time.setter
    def relative_time(self, value: typing.Optional[typing.Optional[datetime.timedelta]]) -> None: ...
    @_property
    def is_discontinuous(self) -> bool: ...
    @is_discontinuous.setter
    def is_discontinuous(self, value: bool) -> None: ...
    @_property
    def duration(self) -> typing.Optional[typing.Optional[datetime.timedelta]]: ...
    @duration.setter
    def duration(self, value: typing.Optional[typing.Optional[datetime.timedelta]]) -> None: ...
    @_property
    def extended_properties(self) -> typing.Optional[windows_foundation_collections.IPropertySet]: ...
    @_property
    def is_read_only(self) -> bool: ...
    @_property
    def type(self) -> str: ...
    @_property
    def direct3_d_surface(self) -> typing.Optional[windows_graphics_directx_direct3d11.IDirect3DSurface]: ...
    @_property
    def software_bitmap(self) -> typing.Optional[windows_graphics_imaging.SoftwareBitmap]: ...

@typing.final
class IMediaExtension(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IMediaExtension: ...
    def set_properties(self, configuration: typing.Optional[windows_foundation_collections.IPropertySet], /) -> None: ...

@typing.final
class IMediaFrame(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IMediaFrame: ...
    def close(self) -> None: ...
    @_property
    def duration(self) -> typing.Optional[typing.Optional[datetime.timedelta]]: ...
    @duration.setter
    def duration(self, value: typing.Optional[typing.Optional[datetime.timedelta]]) -> None: ...
    @_property
    def extended_properties(self) -> typing.Optional[windows_foundation_collections.IPropertySet]: ...
    @_property
    def is_discontinuous(self) -> bool: ...
    @is_discontinuous.setter
    def is_discontinuous(self, value: bool) -> None: ...
    @_property
    def is_read_only(self) -> bool: ...
    @_property
    def relative_time(self) -> typing.Optional[typing.Optional[datetime.timedelta]]: ...
    @relative_time.setter
    def relative_time(self, value: typing.Optional[typing.Optional[datetime.timedelta]]) -> None: ...
    @_property
    def system_relative_time(self) -> typing.Optional[typing.Optional[datetime.timedelta]]: ...
    @system_relative_time.setter
    def system_relative_time(self, value: typing.Optional[typing.Optional[datetime.timedelta]]) -> None: ...
    @_property
    def type(self) -> str: ...

@typing.final
class IMediaMarker(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IMediaMarker: ...
    @_property
    def media_marker_type(self) -> str: ...
    @_property
    def text(self) -> str: ...
    @_property
    def time(self) -> datetime.timedelta: ...

@typing.final
class IMediaMarkers(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IMediaMarkers: ...
    @_property
    def markers(self) -> typing.Optional[windows_foundation_collections.IVectorView[IMediaMarker]]: ...

