// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"
static_assert(winrt::check_version(PYWINRT_VERSION, "0.0.0"), "Mismatched Py/WinRT headers.");

#if __has_include("py.Windows.Devices.Bluetooth.h")
#include "py.Windows.Devices.Bluetooth.h"
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

#include <winrt/Windows.Devices.Bluetooth.h>
#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.Storage.Streams.h>

#include <winrt/Windows.Devices.Bluetooth.Advertisement.h>

namespace py::proj::Windows::Devices::Bluetooth::Advertisement
{}

namespace py::impl::Windows::Devices::Bluetooth::Advertisement
{}

namespace py::wrapper::Windows::Devices::Bluetooth::Advertisement
{
    using BluetoothLEAdvertisement = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisement>;
    using BluetoothLEAdvertisementBytePattern = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementBytePattern>;
    using BluetoothLEAdvertisementDataSection = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementDataSection>;
    using BluetoothLEAdvertisementDataTypes = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementDataTypes>;
    using BluetoothLEAdvertisementFilter = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementFilter>;
    using BluetoothLEAdvertisementPublisher = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementPublisher>;
    using BluetoothLEAdvertisementPublisherStatusChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementPublisherStatusChangedEventArgs>;
    using BluetoothLEAdvertisementReceivedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementReceivedEventArgs>;
    using BluetoothLEAdvertisementWatcher = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementWatcher>;
    using BluetoothLEAdvertisementWatcherStoppedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementWatcherStoppedEventArgs>;
    using BluetoothLEManufacturerData = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEManufacturerData>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementFlags> = "I";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementPublisherStatus> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementWatcherStatus> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEScanningMode> = "i";


    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementFlags>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisementFlags";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementPublisherStatus>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisementPublisherStatus";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementType>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisementType";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementWatcherStatus>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisementWatcherStatus";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEScanningMode>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEScanningMode";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisement>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisement";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementBytePattern>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisementBytePattern";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementDataSection>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisementDataSection";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementDataTypes>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisementDataTypes";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementFilter>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisementFilter";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementPublisher>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisementPublisher";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementPublisherStatusChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisementPublisherStatusChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementReceivedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisementReceivedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementWatcher>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisementWatcher";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementWatcherStoppedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEAdvertisementWatcherStoppedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEManufacturerData>
    {
        static constexpr const char* module_name = "winrt.windows.devices.bluetooth.advertisement";
        static constexpr const char* type_name = "BluetoothLEManufacturerData";
    };
}
