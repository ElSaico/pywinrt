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

from winrt.windows.ui.core.animationmetrics import AnimationEffect, AnimationEffectTarget, PropertyAnimationType

Self = typing.TypeVar('Self')

@typing.final
class AnimationDescription(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AnimationDescription: ...
    def __new__(cls: typing.Type[AnimationDescription], effect: AnimationEffect, target: AnimationEffectTarget) -> AnimationDescription:...
    @_property
    def animations(self) -> typing.Optional[windows_foundation_collections.IVectorView[IPropertyAnimation]]: ...
    @_property
    def delay_limit(self) -> datetime.timedelta: ...
    @_property
    def stagger_delay(self) -> datetime.timedelta: ...
    @_property
    def stagger_delay_factor(self) -> winrt.system.Single: ...
    @_property
    def z_order(self) -> winrt.system.Int32: ...

@typing.final
class OpacityAnimation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> OpacityAnimation: ...
    @_property
    def final_opacity(self) -> winrt.system.Single: ...
    @_property
    def initial_opacity(self) -> typing.Optional[typing.Optional[winrt.system.Single]]: ...
    @_property
    def control1(self) -> windows_foundation.Point: ...
    @_property
    def control2(self) -> windows_foundation.Point: ...
    @_property
    def delay(self) -> datetime.timedelta: ...
    @_property
    def duration(self) -> datetime.timedelta: ...
    @_property
    def type(self) -> PropertyAnimationType: ...

@typing.final
class PropertyAnimation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PropertyAnimation: ...
    @_property
    def control1(self) -> windows_foundation.Point: ...
    @_property
    def control2(self) -> windows_foundation.Point: ...
    @_property
    def delay(self) -> datetime.timedelta: ...
    @_property
    def duration(self) -> datetime.timedelta: ...
    @_property
    def type(self) -> PropertyAnimationType: ...

@typing.final
class ScaleAnimation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ScaleAnimation: ...
    @_property
    def control1(self) -> windows_foundation.Point: ...
    @_property
    def control2(self) -> windows_foundation.Point: ...
    @_property
    def delay(self) -> datetime.timedelta: ...
    @_property
    def duration(self) -> datetime.timedelta: ...
    @_property
    def type(self) -> PropertyAnimationType: ...
    @_property
    def final_scale_x(self) -> winrt.system.Single: ...
    @_property
    def final_scale_y(self) -> winrt.system.Single: ...
    @_property
    def initial_scale_x(self) -> typing.Optional[typing.Optional[winrt.system.Single]]: ...
    @_property
    def initial_scale_y(self) -> typing.Optional[typing.Optional[winrt.system.Single]]: ...
    @_property
    def normalized_origin(self) -> windows_foundation.Point: ...

@typing.final
class TranslationAnimation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TranslationAnimation: ...
    @_property
    def control1(self) -> windows_foundation.Point: ...
    @_property
    def control2(self) -> windows_foundation.Point: ...
    @_property
    def delay(self) -> datetime.timedelta: ...
    @_property
    def duration(self) -> datetime.timedelta: ...
    @_property
    def type(self) -> PropertyAnimationType: ...

@typing.final
class IPropertyAnimation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IPropertyAnimation: ...
    @_property
    def control1(self) -> windows_foundation.Point: ...
    @_property
    def control2(self) -> windows_foundation.Point: ...
    @_property
    def delay(self) -> datetime.timedelta: ...
    @_property
    def duration(self) -> datetime.timedelta: ...
    @_property
    def type(self) -> PropertyAnimationType: ...

