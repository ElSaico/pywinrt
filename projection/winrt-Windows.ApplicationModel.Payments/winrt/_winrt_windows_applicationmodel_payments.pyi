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

from winrt.windows.applicationmodel.payments import PaymentCanMakePaymentResultStatus, PaymentOptionPresence, PaymentRequestChangeKind, PaymentRequestCompletionStatus, PaymentRequestStatus, PaymentShippingType
from winrt.windows.applicationmodel.payments import PaymentRequestChangedHandler

Self = typing.TypeVar('Self')

@typing.final
class PaymentAddress(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentAddress: ...
    def __new__(cls: typing.Type[PaymentAddress]) -> PaymentAddress:...
    @_property
    def sorting_code(self) -> str: ...
    @sorting_code.setter
    def sorting_code(self, value: str) -> None: ...
    @_property
    def region(self) -> str: ...
    @region.setter
    def region(self, value: str) -> None: ...
    @_property
    def recipient(self) -> str: ...
    @recipient.setter
    def recipient(self, value: str) -> None: ...
    @_property
    def postal_code(self) -> str: ...
    @postal_code.setter
    def postal_code(self, value: str) -> None: ...
    @_property
    def phone_number(self) -> str: ...
    @phone_number.setter
    def phone_number(self, value: str) -> None: ...
    @_property
    def organization(self) -> str: ...
    @organization.setter
    def organization(self, value: str) -> None: ...
    @_property
    def language_code(self) -> str: ...
    @language_code.setter
    def language_code(self, value: str) -> None: ...
    @_property
    def dependent_locality(self) -> str: ...
    @dependent_locality.setter
    def dependent_locality(self, value: str) -> None: ...
    @_property
    def country(self) -> str: ...
    @country.setter
    def country(self, value: str) -> None: ...
    @_property
    def city(self) -> str: ...
    @city.setter
    def city(self, value: str) -> None: ...
    @_property
    def address_lines(self) -> typing.Optional[windows_foundation_collections.IVectorView[str]]: ...
    @address_lines.setter
    def address_lines(self, value: typing.Optional[windows_foundation_collections.IVectorView[str]]) -> None: ...
    @_property
    def properties(self) -> typing.Optional[windows_foundation_collections.ValueSet]: ...

@typing.final
class PaymentCanMakePaymentResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentCanMakePaymentResult: ...
    def __new__(cls: typing.Type[PaymentCanMakePaymentResult], value: PaymentCanMakePaymentResultStatus) -> PaymentCanMakePaymentResult:...
    @_property
    def status(self) -> PaymentCanMakePaymentResultStatus: ...

@typing.final
class PaymentCurrencyAmount(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentCurrencyAmount: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentCurrencyAmount], value: str, currency: str) -> PaymentCurrencyAmount:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentCurrencyAmount], value: str, currency: str, currency_system: str) -> PaymentCurrencyAmount:...
    @_property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str) -> None: ...
    @_property
    def currency_system(self) -> str: ...
    @currency_system.setter
    def currency_system(self, value: str) -> None: ...
    @_property
    def currency(self) -> str: ...
    @currency.setter
    def currency(self, value: str) -> None: ...

@typing.final
class PaymentDetails(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentDetails: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentDetails], total: typing.Optional[PaymentItem]) -> PaymentDetails:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentDetails], total: typing.Optional[PaymentItem], display_items: typing.Iterable[PaymentItem]) -> PaymentDetails:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentDetails]) -> PaymentDetails:...
    @_property
    def total(self) -> typing.Optional[PaymentItem]: ...
    @total.setter
    def total(self, value: typing.Optional[PaymentItem]) -> None: ...
    @_property
    def shipping_options(self) -> typing.Optional[windows_foundation_collections.IVectorView[PaymentShippingOption]]: ...
    @shipping_options.setter
    def shipping_options(self, value: typing.Optional[windows_foundation_collections.IVectorView[PaymentShippingOption]]) -> None: ...
    @_property
    def modifiers(self) -> typing.Optional[windows_foundation_collections.IVectorView[PaymentDetailsModifier]]: ...
    @modifiers.setter
    def modifiers(self, value: typing.Optional[windows_foundation_collections.IVectorView[PaymentDetailsModifier]]) -> None: ...
    @_property
    def display_items(self) -> typing.Optional[windows_foundation_collections.IVectorView[PaymentItem]]: ...
    @display_items.setter
    def display_items(self, value: typing.Optional[windows_foundation_collections.IVectorView[PaymentItem]]) -> None: ...

@typing.final
class PaymentDetailsModifier(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentDetailsModifier: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentDetailsModifier], supported_method_ids: typing.Iterable[str], total: typing.Optional[PaymentItem]) -> PaymentDetailsModifier:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentDetailsModifier], supported_method_ids: typing.Iterable[str], total: typing.Optional[PaymentItem], additional_display_items: typing.Iterable[PaymentItem]) -> PaymentDetailsModifier:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentDetailsModifier], supported_method_ids: typing.Iterable[str], total: typing.Optional[PaymentItem], additional_display_items: typing.Iterable[PaymentItem], json_data: str) -> PaymentDetailsModifier:...
    @_property
    def additional_display_items(self) -> typing.Optional[windows_foundation_collections.IVectorView[PaymentItem]]: ...
    @_property
    def json_data(self) -> str: ...
    @_property
    def supported_method_ids(self) -> typing.Optional[windows_foundation_collections.IVectorView[str]]: ...
    @_property
    def total(self) -> typing.Optional[PaymentItem]: ...

@typing.final
class PaymentItem(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentItem: ...
    def __new__(cls: typing.Type[PaymentItem], label: str, amount: typing.Optional[PaymentCurrencyAmount]) -> PaymentItem:...
    @_property
    def pending(self) -> bool: ...
    @pending.setter
    def pending(self, value: bool) -> None: ...
    @_property
    def label(self) -> str: ...
    @label.setter
    def label(self, value: str) -> None: ...
    @_property
    def amount(self) -> typing.Optional[PaymentCurrencyAmount]: ...
    @amount.setter
    def amount(self, value: typing.Optional[PaymentCurrencyAmount]) -> None: ...

@typing.final
class PaymentMediator(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentMediator: ...
    def __new__(cls: typing.Type[PaymentMediator]) -> PaymentMediator:...
    def can_make_payment_async(self, payment_request: typing.Optional[PaymentRequest], /) -> windows_foundation.IAsyncOperation[PaymentCanMakePaymentResult]: ...
    def get_supported_method_ids_async(self) -> windows_foundation.IAsyncOperation[windows_foundation_collections.IVectorView[str]]: ...
    @typing.overload
    def submit_payment_request_async(self, payment_request: typing.Optional[PaymentRequest], /) -> windows_foundation.IAsyncOperation[PaymentRequestSubmitResult]: ...
    @typing.overload
    def submit_payment_request_async(self, payment_request: typing.Optional[PaymentRequest], change_handler: typing.Optional[PaymentRequestChangedHandler], /) -> windows_foundation.IAsyncOperation[PaymentRequestSubmitResult]: ...

@typing.final
class PaymentMerchantInfo(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentMerchantInfo: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentMerchantInfo], uri: typing.Optional[windows_foundation.Uri]) -> PaymentMerchantInfo:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentMerchantInfo]) -> PaymentMerchantInfo:...
    @_property
    def package_full_name(self) -> str: ...
    @_property
    def uri(self) -> typing.Optional[windows_foundation.Uri]: ...

@typing.final
class PaymentMethodData(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentMethodData: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentMethodData], supported_method_ids: typing.Iterable[str]) -> PaymentMethodData:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentMethodData], supported_method_ids: typing.Iterable[str], json_data: str) -> PaymentMethodData:...
    @_property
    def json_data(self) -> str: ...
    @_property
    def supported_method_ids(self) -> typing.Optional[windows_foundation_collections.IVectorView[str]]: ...

@typing.final
class PaymentOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentOptions: ...
    def __new__(cls: typing.Type[PaymentOptions]) -> PaymentOptions:...
    @_property
    def shipping_type(self) -> PaymentShippingType: ...
    @shipping_type.setter
    def shipping_type(self, value: PaymentShippingType) -> None: ...
    @_property
    def request_shipping(self) -> bool: ...
    @request_shipping.setter
    def request_shipping(self, value: bool) -> None: ...
    @_property
    def request_payer_phone_number(self) -> PaymentOptionPresence: ...
    @request_payer_phone_number.setter
    def request_payer_phone_number(self, value: PaymentOptionPresence) -> None: ...
    @_property
    def request_payer_name(self) -> PaymentOptionPresence: ...
    @request_payer_name.setter
    def request_payer_name(self, value: PaymentOptionPresence) -> None: ...
    @_property
    def request_payer_email(self) -> PaymentOptionPresence: ...
    @request_payer_email.setter
    def request_payer_email(self, value: PaymentOptionPresence) -> None: ...

@typing.final
class PaymentRequest(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentRequest: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentRequest], details: typing.Optional[PaymentDetails], method_data: typing.Iterable[PaymentMethodData], merchant_info: typing.Optional[PaymentMerchantInfo], options: typing.Optional[PaymentOptions], id: str) -> PaymentRequest:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentRequest], details: typing.Optional[PaymentDetails], method_data: typing.Iterable[PaymentMethodData]) -> PaymentRequest:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentRequest], details: typing.Optional[PaymentDetails], method_data: typing.Iterable[PaymentMethodData], merchant_info: typing.Optional[PaymentMerchantInfo]) -> PaymentRequest:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentRequest], details: typing.Optional[PaymentDetails], method_data: typing.Iterable[PaymentMethodData], merchant_info: typing.Optional[PaymentMerchantInfo], options: typing.Optional[PaymentOptions]) -> PaymentRequest:...
    @_property
    def details(self) -> typing.Optional[PaymentDetails]: ...
    @_property
    def merchant_info(self) -> typing.Optional[PaymentMerchantInfo]: ...
    @_property
    def method_data(self) -> typing.Optional[windows_foundation_collections.IVectorView[PaymentMethodData]]: ...
    @_property
    def options(self) -> typing.Optional[PaymentOptions]: ...
    @_property
    def id(self) -> str: ...

@typing.final
class PaymentRequestChangedArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentRequestChangedArgs: ...
    def acknowledge(self, change_result: typing.Optional[PaymentRequestChangedResult], /) -> None: ...
    @_property
    def change_kind(self) -> PaymentRequestChangeKind: ...
    @_property
    def selected_shipping_option(self) -> typing.Optional[PaymentShippingOption]: ...
    @_property
    def shipping_address(self) -> typing.Optional[PaymentAddress]: ...

@typing.final
class PaymentRequestChangedResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentRequestChangedResult: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentRequestChangedResult], change_accepted_by_merchant: bool) -> PaymentRequestChangedResult:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentRequestChangedResult], change_accepted_by_merchant: bool, updated_payment_details: typing.Optional[PaymentDetails]) -> PaymentRequestChangedResult:...
    @_property
    def updated_payment_details(self) -> typing.Optional[PaymentDetails]: ...
    @updated_payment_details.setter
    def updated_payment_details(self, value: typing.Optional[PaymentDetails]) -> None: ...
    @_property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str) -> None: ...
    @_property
    def change_accepted_by_merchant(self) -> bool: ...
    @change_accepted_by_merchant.setter
    def change_accepted_by_merchant(self, value: bool) -> None: ...

@typing.final
class PaymentRequestSubmitResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentRequestSubmitResult: ...
    @_property
    def response(self) -> typing.Optional[PaymentResponse]: ...
    @_property
    def status(self) -> PaymentRequestStatus: ...

@typing.final
class PaymentResponse(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentResponse: ...
    def complete_async(self, status: PaymentRequestCompletionStatus, /) -> windows_foundation.IAsyncAction: ...
    @_property
    def payer_email(self) -> str: ...
    @_property
    def payer_name(self) -> str: ...
    @_property
    def payer_phone_number(self) -> str: ...
    @_property
    def payment_token(self) -> typing.Optional[PaymentToken]: ...
    @_property
    def shipping_address(self) -> typing.Optional[PaymentAddress]: ...
    @_property
    def shipping_option(self) -> typing.Optional[PaymentShippingOption]: ...

@typing.final
class PaymentShippingOption(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentShippingOption: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentShippingOption], label: str, amount: typing.Optional[PaymentCurrencyAmount]) -> PaymentShippingOption:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentShippingOption], label: str, amount: typing.Optional[PaymentCurrencyAmount], selected: bool) -> PaymentShippingOption:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentShippingOption], label: str, amount: typing.Optional[PaymentCurrencyAmount], selected: bool, tag: str) -> PaymentShippingOption:...
    @_property
    def tag(self) -> str: ...
    @tag.setter
    def tag(self, value: str) -> None: ...
    @_property
    def label(self) -> str: ...
    @label.setter
    def label(self, value: str) -> None: ...
    @_property
    def is_selected(self) -> bool: ...
    @is_selected.setter
    def is_selected(self, value: bool) -> None: ...
    @_property
    def amount(self) -> typing.Optional[PaymentCurrencyAmount]: ...
    @amount.setter
    def amount(self, value: typing.Optional[PaymentCurrencyAmount]) -> None: ...

@typing.final
class PaymentToken(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PaymentToken: ...
    @typing.overload
    def __new__(cls: typing.Type[PaymentToken], payment_method_id: str) -> PaymentToken:...
    @typing.overload
    def __new__(cls: typing.Type[PaymentToken], payment_method_id: str, json_details: str) -> PaymentToken:...
    @_property
    def json_details(self) -> str: ...
    @_property
    def payment_method_id(self) -> str: ...

