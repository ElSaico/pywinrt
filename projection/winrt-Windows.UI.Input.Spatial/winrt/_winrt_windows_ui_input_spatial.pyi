# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.devices.haptics as windows_devices_haptics
import winrt.windows.devices.power as windows_devices_power
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.foundation.numerics as windows_foundation_numerics
import winrt.windows.perception as windows_perception
import winrt.windows.perception.people as windows_perception_people
import winrt.windows.perception.spatial as windows_perception_spatial
import winrt.windows.storage.streams as windows_storage_streams

from winrt.windows.ui.input.spatial import SpatialGestureSettings, SpatialInteractionPressKind, SpatialInteractionSourceHandedness, SpatialInteractionSourceKind, SpatialInteractionSourcePositionAccuracy

Self = typing.TypeVar('Self')

@typing.final
class SpatialGestureRecognizer(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialGestureRecognizer: ...
    def __new__(cls: typing.Type[SpatialGestureRecognizer], settings: SpatialGestureSettings) -> SpatialGestureRecognizer:...
    def cancel_pending_gestures(self) -> None: ...
    def capture_interaction(self, interaction: typing.Optional[SpatialInteraction], /) -> None: ...
    def try_set_gesture_settings(self, settings: SpatialGestureSettings, /) -> bool: ...
    def add_hold_canceled(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialHoldCanceledEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_hold_canceled(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_hold_completed(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialHoldCompletedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_hold_completed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_hold_started(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialHoldStartedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_hold_started(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_manipulation_canceled(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialManipulationCanceledEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_manipulation_canceled(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_manipulation_completed(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialManipulationCompletedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_manipulation_completed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_manipulation_started(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialManipulationStartedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_manipulation_started(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_manipulation_updated(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialManipulationUpdatedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_manipulation_updated(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_navigation_canceled(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialNavigationCanceledEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_navigation_canceled(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_navigation_completed(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialNavigationCompletedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_navigation_completed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_navigation_started(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialNavigationStartedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_navigation_started(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_navigation_updated(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialNavigationUpdatedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_navigation_updated(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_recognition_ended(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialRecognitionEndedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_recognition_ended(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_recognition_started(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialRecognitionStartedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_recognition_started(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_tapped(self, handler: windows_foundation.TypedEventHandler[SpatialGestureRecognizer, SpatialTappedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_tapped(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def gesture_settings(self) -> SpatialGestureSettings: ...

@typing.final
class SpatialHoldCanceledEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialHoldCanceledEventArgs: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...

@typing.final
class SpatialHoldCompletedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialHoldCompletedEventArgs: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...

@typing.final
class SpatialHoldStartedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialHoldStartedEventArgs: ...
    def try_get_pointer_pose(self, coordinate_system: typing.Optional[windows_perception_spatial.SpatialCoordinateSystem], /) -> typing.Optional[SpatialPointerPose]: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...

@typing.final
class SpatialInteraction(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialInteraction: ...
    @_property
    def source_state(self) -> typing.Optional[SpatialInteractionSourceState]: ...

@typing.final
class SpatialInteractionController(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialInteractionController: ...
    def try_get_battery_report(self) -> typing.Optional[windows_devices_power.BatteryReport]: ...
    def try_get_renderable_model_async(self) -> windows_foundation.IAsyncOperation[windows_storage_streams.IRandomAccessStreamWithContentType]: ...
    @_property
    def has_thumbstick(self) -> bool: ...
    @_property
    def has_touchpad(self) -> bool: ...
    @_property
    def product_id(self) -> winrt.system.UInt16: ...
    @_property
    def simple_haptics_controller(self) -> typing.Optional[windows_devices_haptics.SimpleHapticsController]: ...
    @_property
    def vendor_id(self) -> winrt.system.UInt16: ...
    @_property
    def version(self) -> winrt.system.UInt16: ...

@typing.final
class SpatialInteractionControllerProperties(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialInteractionControllerProperties: ...
    @_property
    def is_thumbstick_pressed(self) -> bool: ...
    @_property
    def is_touchpad_pressed(self) -> bool: ...
    @_property
    def is_touchpad_touched(self) -> bool: ...
    @_property
    def thumbstick_x(self) -> winrt.system.Double: ...
    @_property
    def thumbstick_y(self) -> winrt.system.Double: ...
    @_property
    def touchpad_x(self) -> winrt.system.Double: ...
    @_property
    def touchpad_y(self) -> winrt.system.Double: ...

@typing.final
class SpatialInteractionDetectedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialInteractionDetectedEventArgs: ...
    def try_get_pointer_pose(self, coordinate_system: typing.Optional[windows_perception_spatial.SpatialCoordinateSystem], /) -> typing.Optional[SpatialPointerPose]: ...
    @_property
    def interaction(self) -> typing.Optional[SpatialInteraction]: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...
    @_property
    def interaction_source(self) -> typing.Optional[SpatialInteractionSource]: ...

@typing.final
class SpatialInteractionManager_Static(type):
    def get_for_current_view(cls) -> typing.Optional[SpatialInteractionManager]: ...
    def is_source_kind_supported(cls, kind: SpatialInteractionSourceKind, /) -> bool: ...

@typing.final
class SpatialInteractionManager(winrt.system.Object, metaclass=SpatialInteractionManager_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialInteractionManager: ...
    def get_detected_sources_at_timestamp(self, time_stamp: typing.Optional[windows_perception.PerceptionTimestamp], /) -> typing.Optional[windows_foundation_collections.IVectorView[SpatialInteractionSourceState]]: ...
    def add_interaction_detected(self, handler: windows_foundation.TypedEventHandler[SpatialInteractionManager, SpatialInteractionDetectedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_interaction_detected(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_source_detected(self, handler: windows_foundation.TypedEventHandler[SpatialInteractionManager, SpatialInteractionSourceEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_source_detected(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_source_lost(self, handler: windows_foundation.TypedEventHandler[SpatialInteractionManager, SpatialInteractionSourceEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_source_lost(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_source_pressed(self, handler: windows_foundation.TypedEventHandler[SpatialInteractionManager, SpatialInteractionSourceEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_source_pressed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_source_released(self, handler: windows_foundation.TypedEventHandler[SpatialInteractionManager, SpatialInteractionSourceEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_source_released(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_source_updated(self, handler: windows_foundation.TypedEventHandler[SpatialInteractionManager, SpatialInteractionSourceEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_source_updated(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...

@typing.final
class SpatialInteractionSource(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialInteractionSource: ...
    def try_create_hand_mesh_observer(self) -> typing.Optional[windows_perception_people.HandMeshObserver]: ...
    def try_create_hand_mesh_observer_async(self) -> windows_foundation.IAsyncOperation[windows_perception_people.HandMeshObserver]: ...
    def try_get_state_at_timestamp(self, timestamp: typing.Optional[windows_perception.PerceptionTimestamp], /) -> typing.Optional[SpatialInteractionSourceState]: ...
    @_property
    def id(self) -> winrt.system.UInt32: ...
    @_property
    def kind(self) -> SpatialInteractionSourceKind: ...
    @_property
    def controller(self) -> typing.Optional[SpatialInteractionController]: ...
    @_property
    def is_grasp_supported(self) -> bool: ...
    @_property
    def is_menu_supported(self) -> bool: ...
    @_property
    def is_pointing_supported(self) -> bool: ...
    @_property
    def handedness(self) -> SpatialInteractionSourceHandedness: ...

@typing.final
class SpatialInteractionSourceEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialInteractionSourceEventArgs: ...
    @_property
    def state(self) -> typing.Optional[SpatialInteractionSourceState]: ...
    @_property
    def press_kind(self) -> SpatialInteractionPressKind: ...

@typing.final
class SpatialInteractionSourceLocation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialInteractionSourceLocation: ...
    @_property
    def position(self) -> typing.Optional[typing.Optional[windows_foundation_numerics.Vector3]]: ...
    @_property
    def velocity(self) -> typing.Optional[typing.Optional[windows_foundation_numerics.Vector3]]: ...
    @_property
    def orientation(self) -> typing.Optional[typing.Optional[windows_foundation_numerics.Quaternion]]: ...
    @_property
    def angular_velocity(self) -> typing.Optional[typing.Optional[windows_foundation_numerics.Vector3]]: ...
    @_property
    def position_accuracy(self) -> SpatialInteractionSourcePositionAccuracy: ...
    @_property
    def source_pointer_pose(self) -> typing.Optional[SpatialPointerInteractionSourcePose]: ...

@typing.final
class SpatialInteractionSourceProperties(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialInteractionSourceProperties: ...
    def try_get_location(self, coordinate_system: typing.Optional[windows_perception_spatial.SpatialCoordinateSystem], /) -> typing.Optional[SpatialInteractionSourceLocation]: ...
    def try_get_source_loss_mitigation_direction(self, coordinate_system: typing.Optional[windows_perception_spatial.SpatialCoordinateSystem], /) -> typing.Optional[typing.Optional[windows_foundation_numerics.Vector3]]: ...
    @_property
    def source_loss_risk(self) -> winrt.system.Double: ...

@typing.final
class SpatialInteractionSourceState(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialInteractionSourceState: ...
    def try_get_hand_pose(self) -> typing.Optional[windows_perception_people.HandPose]: ...
    def try_get_pointer_pose(self, coordinate_system: typing.Optional[windows_perception_spatial.SpatialCoordinateSystem], /) -> typing.Optional[SpatialPointerPose]: ...
    @_property
    def is_pressed(self) -> bool: ...
    @_property
    def properties(self) -> typing.Optional[SpatialInteractionSourceProperties]: ...
    @_property
    def source(self) -> typing.Optional[SpatialInteractionSource]: ...
    @_property
    def timestamp(self) -> typing.Optional[windows_perception.PerceptionTimestamp]: ...
    @_property
    def controller_properties(self) -> typing.Optional[SpatialInteractionControllerProperties]: ...
    @_property
    def is_grasped(self) -> bool: ...
    @_property
    def is_menu_pressed(self) -> bool: ...
    @_property
    def is_select_pressed(self) -> bool: ...
    @_property
    def select_pressed_value(self) -> winrt.system.Double: ...

@typing.final
class SpatialManipulationCanceledEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialManipulationCanceledEventArgs: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...

@typing.final
class SpatialManipulationCompletedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialManipulationCompletedEventArgs: ...
    def try_get_cumulative_delta(self, coordinate_system: typing.Optional[windows_perception_spatial.SpatialCoordinateSystem], /) -> typing.Optional[SpatialManipulationDelta]: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...

@typing.final
class SpatialManipulationDelta(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialManipulationDelta: ...
    @_property
    def translation(self) -> windows_foundation_numerics.Vector3: ...

@typing.final
class SpatialManipulationStartedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialManipulationStartedEventArgs: ...
    def try_get_pointer_pose(self, coordinate_system: typing.Optional[windows_perception_spatial.SpatialCoordinateSystem], /) -> typing.Optional[SpatialPointerPose]: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...

@typing.final
class SpatialManipulationUpdatedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialManipulationUpdatedEventArgs: ...
    def try_get_cumulative_delta(self, coordinate_system: typing.Optional[windows_perception_spatial.SpatialCoordinateSystem], /) -> typing.Optional[SpatialManipulationDelta]: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...

@typing.final
class SpatialNavigationCanceledEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialNavigationCanceledEventArgs: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...

@typing.final
class SpatialNavigationCompletedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialNavigationCompletedEventArgs: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...
    @_property
    def normalized_offset(self) -> windows_foundation_numerics.Vector3: ...

@typing.final
class SpatialNavigationStartedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialNavigationStartedEventArgs: ...
    def try_get_pointer_pose(self, coordinate_system: typing.Optional[windows_perception_spatial.SpatialCoordinateSystem], /) -> typing.Optional[SpatialPointerPose]: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...
    @_property
    def is_navigating_x(self) -> bool: ...
    @_property
    def is_navigating_y(self) -> bool: ...
    @_property
    def is_navigating_z(self) -> bool: ...

@typing.final
class SpatialNavigationUpdatedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialNavigationUpdatedEventArgs: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...
    @_property
    def normalized_offset(self) -> windows_foundation_numerics.Vector3: ...

@typing.final
class SpatialPointerInteractionSourcePose(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialPointerInteractionSourcePose: ...
    @_property
    def forward_direction(self) -> windows_foundation_numerics.Vector3: ...
    @_property
    def position(self) -> windows_foundation_numerics.Vector3: ...
    @_property
    def up_direction(self) -> windows_foundation_numerics.Vector3: ...
    @_property
    def orientation(self) -> windows_foundation_numerics.Quaternion: ...
    @_property
    def position_accuracy(self) -> SpatialInteractionSourcePositionAccuracy: ...

@typing.final
class SpatialPointerPose_Static(type):
    def try_get_at_timestamp(cls, coordinate_system: typing.Optional[windows_perception_spatial.SpatialCoordinateSystem], timestamp: typing.Optional[windows_perception.PerceptionTimestamp], /) -> typing.Optional[SpatialPointerPose]: ...

@typing.final
class SpatialPointerPose(winrt.system.Object, metaclass=SpatialPointerPose_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialPointerPose: ...
    def try_get_interaction_source_pose(self, source: typing.Optional[SpatialInteractionSource], /) -> typing.Optional[SpatialPointerInteractionSourcePose]: ...
    @_property
    def head(self) -> typing.Optional[windows_perception_people.HeadPose]: ...
    @_property
    def timestamp(self) -> typing.Optional[windows_perception.PerceptionTimestamp]: ...
    @_property
    def eyes(self) -> typing.Optional[windows_perception_people.EyesPose]: ...
    @_property
    def is_head_captured_by_system(self) -> bool: ...

@typing.final
class SpatialRecognitionEndedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialRecognitionEndedEventArgs: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...

@typing.final
class SpatialRecognitionStartedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialRecognitionStartedEventArgs: ...
    def is_gesture_possible(self, gesture: SpatialGestureSettings, /) -> bool: ...
    def try_get_pointer_pose(self, coordinate_system: typing.Optional[windows_perception_spatial.SpatialCoordinateSystem], /) -> typing.Optional[SpatialPointerPose]: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...

@typing.final
class SpatialTappedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SpatialTappedEventArgs: ...
    def try_get_pointer_pose(self, coordinate_system: typing.Optional[windows_perception_spatial.SpatialCoordinateSystem], /) -> typing.Optional[SpatialPointerPose]: ...
    @_property
    def interaction_source_kind(self) -> SpatialInteractionSourceKind: ...
    @_property
    def tap_count(self) -> winrt.system.UInt32: ...

