// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"
static_assert(winrt::check_version(PYWINRT_VERSION, "0.0.0"), "Mismatched Py/WinRT headers.");

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Storage.h")
#include "py.Windows.Storage.h"
#endif

#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.Storage.h>

#include <winrt/Windows.ApplicationModel.Store.h>

namespace py::proj::Windows::ApplicationModel::Store
{}

namespace py::impl::Windows::ApplicationModel::Store
{
    struct LicenseChangedEventHandler
    {
        static winrt::Windows::ApplicationModel::Store::LicenseChangedEventHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)]()
            {
                auto gil = py::ensure_gil();

                py::pyobj_handle args{ nullptr };
                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }
            };
        };
    };
}

namespace py::wrapper::Windows::ApplicationModel::Store
{
    using CurrentApp = py::winrt_wrapper<winrt::Windows::ApplicationModel::Store::CurrentApp>;
    using CurrentAppSimulator = py::winrt_wrapper<winrt::Windows::ApplicationModel::Store::CurrentAppSimulator>;
    using LicenseInformation = py::winrt_wrapper<winrt::Windows::ApplicationModel::Store::LicenseInformation>;
    using ListingInformation = py::winrt_wrapper<winrt::Windows::ApplicationModel::Store::ListingInformation>;
    using ProductLicense = py::winrt_wrapper<winrt::Windows::ApplicationModel::Store::ProductLicense>;
    using ProductListing = py::winrt_wrapper<winrt::Windows::ApplicationModel::Store::ProductListing>;
    using ProductPurchaseDisplayProperties = py::winrt_wrapper<winrt::Windows::ApplicationModel::Store::ProductPurchaseDisplayProperties>;
    using PurchaseResults = py::winrt_wrapper<winrt::Windows::ApplicationModel::Store::PurchaseResults>;
    using UnfulfilledConsumable = py::winrt_wrapper<winrt::Windows::ApplicationModel::Store::UnfulfilledConsumable>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::ApplicationModel::Store::FulfillmentResult> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::ApplicationModel::Store::ProductPurchaseStatus> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::ApplicationModel::Store::ProductType> = "i";


    template<>
    struct py_type<winrt::Windows::ApplicationModel::Store::FulfillmentResult>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.store";
        static constexpr const char* type_name = "FulfillmentResult";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::Store::ProductPurchaseStatus>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.store";
        static constexpr const char* type_name = "ProductPurchaseStatus";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::Store::ProductType>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.store";
        static constexpr const char* type_name = "ProductType";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::Store::CurrentApp>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.store";
        static constexpr const char* type_name = "CurrentApp";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::Store::CurrentAppSimulator>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.store";
        static constexpr const char* type_name = "CurrentAppSimulator";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::Store::LicenseInformation>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.store";
        static constexpr const char* type_name = "LicenseInformation";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::Store::ListingInformation>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.store";
        static constexpr const char* type_name = "ListingInformation";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::Store::ProductLicense>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.store";
        static constexpr const char* type_name = "ProductLicense";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::Store::ProductListing>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.store";
        static constexpr const char* type_name = "ProductListing";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::Store::ProductPurchaseDisplayProperties>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.store";
        static constexpr const char* type_name = "ProductPurchaseDisplayProperties";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::Store::PurchaseResults>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.store";
        static constexpr const char* type_name = "PurchaseResults";
    };

    template<>
    struct py_type<winrt::Windows::ApplicationModel::Store::UnfulfilledConsumable>
    {
        static constexpr const char* module_name = "winrt.windows.applicationmodel.store";
        static constexpr const char* type_name = "UnfulfilledConsumable";
    };
    template <>
    struct delegate_python_type<winrt::Windows::ApplicationModel::Store::LicenseChangedEventHandler>
    {
        using type = py::impl::Windows::ApplicationModel::Store::LicenseChangedEventHandler;
    };

}
