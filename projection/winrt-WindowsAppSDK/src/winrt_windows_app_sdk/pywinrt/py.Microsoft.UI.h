// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"
static_assert(winrt::check_version(PYWINRT_VERSION, "0.0.0"), "Mismatched Py/WinRT headers.");

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.UI.h")
#include "py.Windows.UI.h"
#endif

#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.UI.h>

#include <winrt/Microsoft.UI.h>

namespace py::proj::Microsoft::UI
{}

namespace py::impl::Microsoft::UI
{
    struct ClosableNotifierHandler
    {
        static winrt::Microsoft::UI::ClosableNotifierHandler get(PyObject* callable)
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

namespace py::wrapper::Microsoft::UI
{
    using ColorHelper = py::winrt_wrapper<winrt::Microsoft::UI::ColorHelper>;
    using Colors = py::winrt_wrapper<winrt::Microsoft::UI::Colors>;
    using IClosableNotifier = py::winrt_wrapper<winrt::Microsoft::UI::IClosableNotifier>;
    using DisplayId = py::winrt_struct_wrapper<winrt::Microsoft::UI::DisplayId>;
    using IconId = py::winrt_struct_wrapper<winrt::Microsoft::UI::IconId>;
    using WindowId = py::winrt_struct_wrapper<winrt::Microsoft::UI::WindowId>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::UI::DisplayId> = "T{Q:value:}";

    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::UI::IconId> = "T{Q:value:}";

    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::UI::WindowId> = "T{Q:value:}";


    template<>
    struct py_type<winrt::Microsoft::UI::ColorHelper>
    {
        static constexpr const char* module_name = "winrt.microsoft.ui";
        static constexpr const char* type_name = "ColorHelper";
    };

    template<>
    struct py_type<winrt::Microsoft::UI::Colors>
    {
        static constexpr const char* module_name = "winrt.microsoft.ui";
        static constexpr const char* type_name = "Colors";
    };

    template<>
    struct py_type<winrt::Microsoft::UI::IClosableNotifier>
    {
        static constexpr const char* module_name = "winrt.microsoft.ui";
        static constexpr const char* type_name = "IClosableNotifier";
    };

    template<>
    struct py_type<winrt::Microsoft::UI::DisplayId>
    {
        static constexpr const char* module_name = "winrt.microsoft.ui";
        static constexpr const char* type_name = "DisplayId";
    };

    template<>
    struct py_type<winrt::Microsoft::UI::IconId>
    {
        static constexpr const char* module_name = "winrt.microsoft.ui";
        static constexpr const char* type_name = "IconId";
    };

    template<>
    struct py_type<winrt::Microsoft::UI::WindowId>
    {
        static constexpr const char* module_name = "winrt.microsoft.ui";
        static constexpr const char* type_name = "WindowId";
    };
    template <>
    struct delegate_python_type<winrt::Microsoft::UI::ClosableNotifierHandler>
    {
        using type = py::impl::Microsoft::UI::ClosableNotifierHandler;
    };

}
