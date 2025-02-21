// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"
static_assert(winrt::check_version(PYWINRT_VERSION, "0.0.0"), "Mismatched Py/WinRT headers.");

#if __has_include("py.Windows.Devices.Enumeration.h")
#include "py.Windows.Devices.Enumeration.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#if __has_include("py.Windows.UI.Popups.h")
#include "py.Windows.UI.Popups.h"
#endif

#include <winrt/Windows.Devices.Enumeration.h>
#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.Storage.Streams.h>
#include <winrt/Windows.UI.Popups.h>

#include <winrt/Windows.Media.DialProtocol.h>

namespace py::proj::Windows::Media::DialProtocol
{}

namespace py::impl::Windows::Media::DialProtocol
{}

namespace py::wrapper::Windows::Media::DialProtocol
{
    using DialApp = py::winrt_wrapper<winrt::Windows::Media::DialProtocol::DialApp>;
    using DialAppStateDetails = py::winrt_wrapper<winrt::Windows::Media::DialProtocol::DialAppStateDetails>;
    using DialDevice = py::winrt_wrapper<winrt::Windows::Media::DialProtocol::DialDevice>;
    using DialDevicePicker = py::winrt_wrapper<winrt::Windows::Media::DialProtocol::DialDevicePicker>;
    using DialDevicePickerFilter = py::winrt_wrapper<winrt::Windows::Media::DialProtocol::DialDevicePickerFilter>;
    using DialDeviceSelectedEventArgs = py::winrt_wrapper<winrt::Windows::Media::DialProtocol::DialDeviceSelectedEventArgs>;
    using DialDisconnectButtonClickedEventArgs = py::winrt_wrapper<winrt::Windows::Media::DialProtocol::DialDisconnectButtonClickedEventArgs>;
    using DialReceiverApp = py::winrt_wrapper<winrt::Windows::Media::DialProtocol::DialReceiverApp>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Media::DialProtocol::DialAppLaunchResult> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Media::DialProtocol::DialAppState> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Media::DialProtocol::DialAppStopResult> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Media::DialProtocol::DialDeviceDisplayStatus> = "i";


    template<>
    struct py_type<winrt::Windows::Media::DialProtocol::DialAppLaunchResult>
    {
        static constexpr const char* module_name = "winrt.windows.media.dialprotocol";
        static constexpr const char* type_name = "DialAppLaunchResult";
    };

    template<>
    struct py_type<winrt::Windows::Media::DialProtocol::DialAppState>
    {
        static constexpr const char* module_name = "winrt.windows.media.dialprotocol";
        static constexpr const char* type_name = "DialAppState";
    };

    template<>
    struct py_type<winrt::Windows::Media::DialProtocol::DialAppStopResult>
    {
        static constexpr const char* module_name = "winrt.windows.media.dialprotocol";
        static constexpr const char* type_name = "DialAppStopResult";
    };

    template<>
    struct py_type<winrt::Windows::Media::DialProtocol::DialDeviceDisplayStatus>
    {
        static constexpr const char* module_name = "winrt.windows.media.dialprotocol";
        static constexpr const char* type_name = "DialDeviceDisplayStatus";
    };

    template<>
    struct py_type<winrt::Windows::Media::DialProtocol::DialApp>
    {
        static constexpr const char* module_name = "winrt.windows.media.dialprotocol";
        static constexpr const char* type_name = "DialApp";
    };

    template<>
    struct py_type<winrt::Windows::Media::DialProtocol::DialAppStateDetails>
    {
        static constexpr const char* module_name = "winrt.windows.media.dialprotocol";
        static constexpr const char* type_name = "DialAppStateDetails";
    };

    template<>
    struct py_type<winrt::Windows::Media::DialProtocol::DialDevice>
    {
        static constexpr const char* module_name = "winrt.windows.media.dialprotocol";
        static constexpr const char* type_name = "DialDevice";
    };

    template<>
    struct py_type<winrt::Windows::Media::DialProtocol::DialDevicePicker>
    {
        static constexpr const char* module_name = "winrt.windows.media.dialprotocol";
        static constexpr const char* type_name = "DialDevicePicker";
    };

    template<>
    struct py_type<winrt::Windows::Media::DialProtocol::DialDevicePickerFilter>
    {
        static constexpr const char* module_name = "winrt.windows.media.dialprotocol";
        static constexpr const char* type_name = "DialDevicePickerFilter";
    };

    template<>
    struct py_type<winrt::Windows::Media::DialProtocol::DialDeviceSelectedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.media.dialprotocol";
        static constexpr const char* type_name = "DialDeviceSelectedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Media::DialProtocol::DialDisconnectButtonClickedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.media.dialprotocol";
        static constexpr const char* type_name = "DialDisconnectButtonClickedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Media::DialProtocol::DialReceiverApp>
    {
        static constexpr const char* module_name = "winrt.windows.media.dialprotocol";
        static constexpr const char* type_name = "DialReceiverApp";
    };
}
