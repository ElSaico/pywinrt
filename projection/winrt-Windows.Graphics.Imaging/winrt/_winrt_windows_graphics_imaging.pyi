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
import winrt.windows.graphics.directx.direct3d11 as windows_graphics_directx_direct3d11
import winrt.windows.storage.streams as windows_storage_streams

from winrt.windows.graphics.imaging import BitmapAlphaMode, BitmapBufferAccessMode, BitmapFlip, BitmapInterpolationMode, BitmapPixelFormat, BitmapRotation, ColorManagementMode, ExifOrientationMode, JpegSubsamplingMode, PngFilterMode, TiffCompressionMode

Self = typing.TypeVar('Self')

@typing.final
class BitmapBounds:
    x: winrt.system.UInt32
    y: winrt.system.UInt32
    width: winrt.system.UInt32
    height: winrt.system.UInt32
    def __init__(self, x: winrt.system.UInt32, y: winrt.system.UInt32, width: winrt.system.UInt32, height: winrt.system.UInt32) -> None: ...

@typing.final
class BitmapPlaneDescription:
    start_index: winrt.system.Int32
    width: winrt.system.Int32
    height: winrt.system.Int32
    stride: winrt.system.Int32
    def __init__(self, start_index: winrt.system.Int32, width: winrt.system.Int32, height: winrt.system.Int32, stride: winrt.system.Int32) -> None: ...

@typing.final
class BitmapSize:
    width: winrt.system.UInt32
    height: winrt.system.UInt32
    def __init__(self, width: winrt.system.UInt32, height: winrt.system.UInt32) -> None: ...

@typing.final
class BitmapBuffer(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> BitmapBuffer: ...
    def close(self) -> None: ...
    def create_reference(self) -> typing.Optional[windows_foundation.IMemoryBufferReference]: ...
    def get_plane_count(self) -> winrt.system.Int32: ...
    def get_plane_description(self, index: winrt.system.Int32, /) -> BitmapPlaneDescription: ...

@typing.final
class BitmapCodecInformation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> BitmapCodecInformation: ...
    @_property
    def codec_id(self) -> _uuid.UUID: ...
    @_property
    def file_extensions(self) -> typing.Optional[windows_foundation_collections.IVectorView[str]]: ...
    @_property
    def friendly_name(self) -> str: ...
    @_property
    def mime_types(self) -> typing.Optional[windows_foundation_collections.IVectorView[str]]: ...

@typing.final
class BitmapDecoder_Static(type):
    @typing.overload
    def create_async(cls, stream: typing.Optional[windows_storage_streams.IRandomAccessStream], /) -> windows_foundation.IAsyncOperation[BitmapDecoder]: ...
    @typing.overload
    def create_async(cls, decoder_id: _uuid.UUID, stream: typing.Optional[windows_storage_streams.IRandomAccessStream], /) -> windows_foundation.IAsyncOperation[BitmapDecoder]: ...
    def get_decoder_information_enumerator(cls) -> typing.Optional[windows_foundation_collections.IVectorView[BitmapCodecInformation]]: ...
    @_property
    def bmp_decoder_id(cls) -> _uuid.UUID: ...
    @_property
    def gif_decoder_id(cls) -> _uuid.UUID: ...
    @_property
    def ico_decoder_id(cls) -> _uuid.UUID: ...
    @_property
    def jpeg_decoder_id(cls) -> _uuid.UUID: ...
    @_property
    def jpeg_x_r_decoder_id(cls) -> _uuid.UUID: ...
    @_property
    def png_decoder_id(cls) -> _uuid.UUID: ...
    @_property
    def tiff_decoder_id(cls) -> _uuid.UUID: ...
    @_property
    def heif_decoder_id(cls) -> _uuid.UUID: ...
    @_property
    def webp_decoder_id(cls) -> _uuid.UUID: ...

@typing.final
class BitmapDecoder(winrt.system.Object, metaclass=BitmapDecoder_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> BitmapDecoder: ...
    def get_frame_async(self, frame_index: winrt.system.UInt32, /) -> windows_foundation.IAsyncOperation[BitmapFrame]: ...
    @typing.overload
    def get_pixel_data_async(self) -> windows_foundation.IAsyncOperation[PixelDataProvider]: ...
    @typing.overload
    def get_pixel_data_async(self, pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: typing.Optional[BitmapTransform], exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode, /) -> windows_foundation.IAsyncOperation[PixelDataProvider]: ...
    def get_preview_async(self) -> windows_foundation.IAsyncOperation[ImageStream]: ...
    @typing.overload
    def get_software_bitmap_async(self) -> windows_foundation.IAsyncOperation[SoftwareBitmap]: ...
    @typing.overload
    def get_software_bitmap_async(self, pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, /) -> windows_foundation.IAsyncOperation[SoftwareBitmap]: ...
    @typing.overload
    def get_software_bitmap_async(self, pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: typing.Optional[BitmapTransform], exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode, /) -> windows_foundation.IAsyncOperation[SoftwareBitmap]: ...
    def get_thumbnail_async(self) -> windows_foundation.IAsyncOperation[ImageStream]: ...
    @_property
    def bitmap_container_properties(self) -> typing.Optional[BitmapPropertiesView]: ...
    @_property
    def decoder_information(self) -> typing.Optional[BitmapCodecInformation]: ...
    @_property
    def frame_count(self) -> winrt.system.UInt32: ...
    @_property
    def bitmap_alpha_mode(self) -> BitmapAlphaMode: ...
    @_property
    def bitmap_pixel_format(self) -> BitmapPixelFormat: ...
    @_property
    def bitmap_properties(self) -> typing.Optional[BitmapPropertiesView]: ...
    @_property
    def dpi_x(self) -> winrt.system.Double: ...
    @_property
    def dpi_y(self) -> winrt.system.Double: ...
    @_property
    def oriented_pixel_height(self) -> winrt.system.UInt32: ...
    @_property
    def oriented_pixel_width(self) -> winrt.system.UInt32: ...
    @_property
    def pixel_height(self) -> winrt.system.UInt32: ...
    @_property
    def pixel_width(self) -> winrt.system.UInt32: ...

@typing.final
class BitmapEncoder_Static(type):
    @typing.overload
    def create_async(cls, encoder_id: _uuid.UUID, stream: typing.Optional[windows_storage_streams.IRandomAccessStream], /) -> windows_foundation.IAsyncOperation[BitmapEncoder]: ...
    @typing.overload
    def create_async(cls, encoder_id: _uuid.UUID, stream: typing.Optional[windows_storage_streams.IRandomAccessStream], encoding_options: typing.Iterable[windows_foundation_collections.IKeyValuePair[str, BitmapTypedValue]], /) -> windows_foundation.IAsyncOperation[BitmapEncoder]: ...
    def create_for_in_place_property_encoding_async(cls, bitmap_decoder: typing.Optional[BitmapDecoder], /) -> windows_foundation.IAsyncOperation[BitmapEncoder]: ...
    def create_for_transcoding_async(cls, stream: typing.Optional[windows_storage_streams.IRandomAccessStream], bitmap_decoder: typing.Optional[BitmapDecoder], /) -> windows_foundation.IAsyncOperation[BitmapEncoder]: ...
    def get_encoder_information_enumerator(cls) -> typing.Optional[windows_foundation_collections.IVectorView[BitmapCodecInformation]]: ...
    @_property
    def bmp_encoder_id(cls) -> _uuid.UUID: ...
    @_property
    def gif_encoder_id(cls) -> _uuid.UUID: ...
    @_property
    def jpeg_encoder_id(cls) -> _uuid.UUID: ...
    @_property
    def jpeg_x_r_encoder_id(cls) -> _uuid.UUID: ...
    @_property
    def png_encoder_id(cls) -> _uuid.UUID: ...
    @_property
    def tiff_encoder_id(cls) -> _uuid.UUID: ...
    @_property
    def heif_encoder_id(cls) -> _uuid.UUID: ...

@typing.final
class BitmapEncoder(winrt.system.Object, metaclass=BitmapEncoder_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> BitmapEncoder: ...
    def flush_async(self) -> windows_foundation.IAsyncAction: ...
    @typing.overload
    def go_to_next_frame_async(self) -> windows_foundation.IAsyncAction: ...
    @typing.overload
    def go_to_next_frame_async(self, encoding_options: typing.Iterable[windows_foundation_collections.IKeyValuePair[str, BitmapTypedValue]], /) -> windows_foundation.IAsyncAction: ...
    def set_pixel_data(self, pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, width: winrt.system.UInt32, height: winrt.system.UInt32, dpi_x: winrt.system.Double, dpi_y: winrt.system.Double, pixels: winrt.system.Array[winrt.system.UInt8], /) -> None: ...
    def set_software_bitmap(self, bitmap: typing.Optional[SoftwareBitmap], /) -> None: ...
    @_property
    def is_thumbnail_generated(self) -> bool: ...
    @is_thumbnail_generated.setter
    def is_thumbnail_generated(self, value: bool) -> None: ...
    @_property
    def generated_thumbnail_width(self) -> winrt.system.UInt32: ...
    @generated_thumbnail_width.setter
    def generated_thumbnail_width(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def generated_thumbnail_height(self) -> winrt.system.UInt32: ...
    @generated_thumbnail_height.setter
    def generated_thumbnail_height(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def bitmap_container_properties(self) -> typing.Optional[BitmapProperties]: ...
    @_property
    def bitmap_properties(self) -> typing.Optional[BitmapProperties]: ...
    @_property
    def bitmap_transform(self) -> typing.Optional[BitmapTransform]: ...
    @_property
    def encoder_information(self) -> typing.Optional[BitmapCodecInformation]: ...

@typing.final
class BitmapFrame(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> BitmapFrame: ...
    @typing.overload
    def get_pixel_data_async(self) -> windows_foundation.IAsyncOperation[PixelDataProvider]: ...
    @typing.overload
    def get_pixel_data_async(self, pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: typing.Optional[BitmapTransform], exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode, /) -> windows_foundation.IAsyncOperation[PixelDataProvider]: ...
    @typing.overload
    def get_software_bitmap_async(self) -> windows_foundation.IAsyncOperation[SoftwareBitmap]: ...
    @typing.overload
    def get_software_bitmap_async(self, pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, /) -> windows_foundation.IAsyncOperation[SoftwareBitmap]: ...
    @typing.overload
    def get_software_bitmap_async(self, pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: typing.Optional[BitmapTransform], exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode, /) -> windows_foundation.IAsyncOperation[SoftwareBitmap]: ...
    def get_thumbnail_async(self) -> windows_foundation.IAsyncOperation[ImageStream]: ...
    @_property
    def bitmap_alpha_mode(self) -> BitmapAlphaMode: ...
    @_property
    def bitmap_pixel_format(self) -> BitmapPixelFormat: ...
    @_property
    def bitmap_properties(self) -> typing.Optional[BitmapPropertiesView]: ...
    @_property
    def dpi_x(self) -> winrt.system.Double: ...
    @_property
    def dpi_y(self) -> winrt.system.Double: ...
    @_property
    def oriented_pixel_height(self) -> winrt.system.UInt32: ...
    @_property
    def oriented_pixel_width(self) -> winrt.system.UInt32: ...
    @_property
    def pixel_height(self) -> winrt.system.UInt32: ...
    @_property
    def pixel_width(self) -> winrt.system.UInt32: ...

@typing.final
class BitmapProperties(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> BitmapProperties: ...
    def get_properties_async(self, properties_to_retrieve: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[BitmapPropertySet]: ...
    def set_properties_async(self, properties_to_set: typing.Iterable[windows_foundation_collections.IKeyValuePair[str, BitmapTypedValue]], /) -> windows_foundation.IAsyncAction: ...

@typing.final
class BitmapPropertiesView(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> BitmapPropertiesView: ...
    def get_properties_async(self, properties_to_retrieve: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[BitmapPropertySet]: ...

@typing.final
class BitmapPropertySet(winrt.system.Object, winrt._winrt.MutableMapping[str, BitmapTypedValue]):
    def __len__(self) -> int: ...
    def __iter__(self) -> typing.Iterator[str]: ...
    def __contains__(self, key: object) -> bool:...
    def __setitem__(self, key: str, value: BitmapTypedValue) -> None: ...
    def __getitem__(self, key: str) -> BitmapTypedValue: ...
    def __delitem__(self, key: str) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> BitmapPropertySet: ...
    def __new__(cls: typing.Type[BitmapPropertySet]) -> BitmapPropertySet:...
    def clear(self) -> None: ...
    def first(self) -> typing.Optional[windows_foundation_collections.IIterator[windows_foundation_collections.IKeyValuePair[str, BitmapTypedValue]]]: ...
    def get_view(self) -> typing.Optional[windows_foundation_collections.IMapView[str, BitmapTypedValue]]: ...
    def has_key(self, key: str, /) -> bool: ...
    def insert(self, key: str, value: typing.Optional[BitmapTypedValue], /) -> bool: ...
    def lookup(self, key: str, /) -> typing.Optional[BitmapTypedValue]: ...
    def remove(self, key: str, /) -> None: ...
    @_property
    def size(self) -> winrt.system.UInt32: ...

@typing.final
class BitmapTransform(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> BitmapTransform: ...
    def __new__(cls: typing.Type[BitmapTransform]) -> BitmapTransform:...
    @_property
    def scaled_width(self) -> winrt.system.UInt32: ...
    @scaled_width.setter
    def scaled_width(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def scaled_height(self) -> winrt.system.UInt32: ...
    @scaled_height.setter
    def scaled_height(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def rotation(self) -> BitmapRotation: ...
    @rotation.setter
    def rotation(self, value: BitmapRotation) -> None: ...
    @_property
    def interpolation_mode(self) -> BitmapInterpolationMode: ...
    @interpolation_mode.setter
    def interpolation_mode(self, value: BitmapInterpolationMode) -> None: ...
    @_property
    def flip(self) -> BitmapFlip: ...
    @flip.setter
    def flip(self, value: BitmapFlip) -> None: ...
    @_property
    def bounds(self) -> BitmapBounds: ...
    @bounds.setter
    def bounds(self, value: BitmapBounds) -> None: ...

@typing.final
class BitmapTypedValue(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> BitmapTypedValue: ...
    def __new__(cls: typing.Type[BitmapTypedValue], value: typing.Optional[winrt.system.Object], type: windows_foundation.PropertyType) -> BitmapTypedValue:...
    @_property
    def type(self) -> windows_foundation.PropertyType: ...
    @_property
    def value(self) -> typing.Optional[winrt.system.Object]: ...

@typing.final
class ImageStream(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ImageStream: ...
    def clone_stream(self) -> typing.Optional[windows_storage_streams.IRandomAccessStream]: ...
    def close(self) -> None: ...
    def flush_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def get_input_stream_at(self, position: winrt.system.UInt64, /) -> typing.Optional[windows_storage_streams.IInputStream]: ...
    def get_output_stream_at(self, position: winrt.system.UInt64, /) -> typing.Optional[windows_storage_streams.IOutputStream]: ...
    def read_async(self, buffer: typing.Optional[windows_storage_streams.IBuffer], count: winrt.system.UInt32, options: windows_storage_streams.InputStreamOptions, /) -> windows_foundation.IAsyncOperationWithProgress[windows_storage_streams.IBuffer, winrt.system.UInt32]: ...
    def seek(self, position: winrt.system.UInt64, /) -> None: ...
    def write_async(self, buffer: typing.Optional[windows_storage_streams.IBuffer], /) -> windows_foundation.IAsyncOperationWithProgress[winrt.system.UInt32, winrt.system.UInt32]: ...
    @_property
    def content_type(self) -> str: ...
    @_property
    def size(self) -> winrt.system.UInt64: ...
    @size.setter
    def size(self, value: winrt.system.UInt64) -> None: ...
    @_property
    def can_read(self) -> bool: ...
    @_property
    def can_write(self) -> bool: ...
    @_property
    def position(self) -> winrt.system.UInt64: ...

@typing.final
class PixelDataProvider(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PixelDataProvider: ...
    def detach_pixel_data(self) -> winrt.system.UInt8: ...

@typing.final
class SoftwareBitmap_Static(type):
    @typing.overload
    def convert(cls, source: typing.Optional[SoftwareBitmap], format: BitmapPixelFormat, /) -> typing.Optional[SoftwareBitmap]: ...
    @typing.overload
    def convert(cls, source: typing.Optional[SoftwareBitmap], format: BitmapPixelFormat, alpha: BitmapAlphaMode, /) -> typing.Optional[SoftwareBitmap]: ...
    def copy(cls, source: typing.Optional[SoftwareBitmap], /) -> typing.Optional[SoftwareBitmap]: ...
    @typing.overload
    def create_copy_from_buffer(cls, source: typing.Optional[windows_storage_streams.IBuffer], format: BitmapPixelFormat, width: winrt.system.Int32, height: winrt.system.Int32, /) -> typing.Optional[SoftwareBitmap]: ...
    @typing.overload
    def create_copy_from_buffer(cls, source: typing.Optional[windows_storage_streams.IBuffer], format: BitmapPixelFormat, width: winrt.system.Int32, height: winrt.system.Int32, alpha: BitmapAlphaMode, /) -> typing.Optional[SoftwareBitmap]: ...
    @typing.overload
    def create_copy_from_surface_async(cls, surface: typing.Optional[windows_graphics_directx_direct3d11.IDirect3DSurface], /) -> windows_foundation.IAsyncOperation[SoftwareBitmap]: ...
    @typing.overload
    def create_copy_from_surface_async(cls, surface: typing.Optional[windows_graphics_directx_direct3d11.IDirect3DSurface], alpha: BitmapAlphaMode, /) -> windows_foundation.IAsyncOperation[SoftwareBitmap]: ...

@typing.final
class SoftwareBitmap(winrt.system.Object, metaclass=SoftwareBitmap_Static):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SoftwareBitmap: ...
    @typing.overload
    def __new__(cls: typing.Type[SoftwareBitmap], format: BitmapPixelFormat, width: winrt.system.Int32, height: winrt.system.Int32) -> SoftwareBitmap:...
    @typing.overload
    def __new__(cls: typing.Type[SoftwareBitmap], format: BitmapPixelFormat, width: winrt.system.Int32, height: winrt.system.Int32, alpha: BitmapAlphaMode) -> SoftwareBitmap:...
    def close(self) -> None: ...
    def copy_from_buffer(self, buffer: typing.Optional[windows_storage_streams.IBuffer], /) -> None: ...
    def copy_to(self, bitmap: typing.Optional[SoftwareBitmap], /) -> None: ...
    def copy_to_buffer(self, buffer: typing.Optional[windows_storage_streams.IBuffer], /) -> None: ...
    def get_read_only_view(self) -> typing.Optional[SoftwareBitmap]: ...
    def lock_buffer(self, mode: BitmapBufferAccessMode, /) -> typing.Optional[BitmapBuffer]: ...
    @_property
    def dpi_y(self) -> winrt.system.Double: ...
    @dpi_y.setter
    def dpi_y(self, value: winrt.system.Double) -> None: ...
    @_property
    def dpi_x(self) -> winrt.system.Double: ...
    @dpi_x.setter
    def dpi_x(self, value: winrt.system.Double) -> None: ...
    @_property
    def bitmap_alpha_mode(self) -> BitmapAlphaMode: ...
    @_property
    def bitmap_pixel_format(self) -> BitmapPixelFormat: ...
    @_property
    def is_read_only(self) -> bool: ...
    @_property
    def pixel_height(self) -> winrt.system.Int32: ...
    @_property
    def pixel_width(self) -> winrt.system.Int32: ...

@typing.final
class IBitmapFrame(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IBitmapFrame: ...
    @typing.overload
    def get_pixel_data_async(self) -> windows_foundation.IAsyncOperation[PixelDataProvider]: ...
    @typing.overload
    def get_pixel_data_async(self, pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: typing.Optional[BitmapTransform], exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode, /) -> windows_foundation.IAsyncOperation[PixelDataProvider]: ...
    def get_thumbnail_async(self) -> windows_foundation.IAsyncOperation[ImageStream]: ...
    @_property
    def bitmap_alpha_mode(self) -> BitmapAlphaMode: ...
    @_property
    def bitmap_pixel_format(self) -> BitmapPixelFormat: ...
    @_property
    def bitmap_properties(self) -> typing.Optional[BitmapPropertiesView]: ...
    @_property
    def dpi_x(self) -> winrt.system.Double: ...
    @_property
    def dpi_y(self) -> winrt.system.Double: ...
    @_property
    def oriented_pixel_height(self) -> winrt.system.UInt32: ...
    @_property
    def oriented_pixel_width(self) -> winrt.system.UInt32: ...
    @_property
    def pixel_height(self) -> winrt.system.UInt32: ...
    @_property
    def pixel_width(self) -> winrt.system.UInt32: ...

@typing.final
class IBitmapFrameWithSoftwareBitmap(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IBitmapFrameWithSoftwareBitmap: ...
    @typing.overload
    def get_pixel_data_async(self) -> windows_foundation.IAsyncOperation[PixelDataProvider]: ...
    @typing.overload
    def get_pixel_data_async(self, pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: typing.Optional[BitmapTransform], exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode, /) -> windows_foundation.IAsyncOperation[PixelDataProvider]: ...
    @typing.overload
    def get_software_bitmap_async(self) -> windows_foundation.IAsyncOperation[SoftwareBitmap]: ...
    @typing.overload
    def get_software_bitmap_async(self, pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, /) -> windows_foundation.IAsyncOperation[SoftwareBitmap]: ...
    @typing.overload
    def get_software_bitmap_async(self, pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: typing.Optional[BitmapTransform], exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode, /) -> windows_foundation.IAsyncOperation[SoftwareBitmap]: ...
    def get_thumbnail_async(self) -> windows_foundation.IAsyncOperation[ImageStream]: ...
    @_property
    def bitmap_alpha_mode(self) -> BitmapAlphaMode: ...
    @_property
    def bitmap_pixel_format(self) -> BitmapPixelFormat: ...
    @_property
    def bitmap_properties(self) -> typing.Optional[BitmapPropertiesView]: ...
    @_property
    def dpi_x(self) -> winrt.system.Double: ...
    @_property
    def dpi_y(self) -> winrt.system.Double: ...
    @_property
    def oriented_pixel_height(self) -> winrt.system.UInt32: ...
    @_property
    def oriented_pixel_width(self) -> winrt.system.UInt32: ...
    @_property
    def pixel_height(self) -> winrt.system.UInt32: ...
    @_property
    def pixel_width(self) -> winrt.system.UInt32: ...

@typing.final
class IBitmapPropertiesView(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IBitmapPropertiesView: ...
    def get_properties_async(self, properties_to_retrieve: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[BitmapPropertySet]: ...

