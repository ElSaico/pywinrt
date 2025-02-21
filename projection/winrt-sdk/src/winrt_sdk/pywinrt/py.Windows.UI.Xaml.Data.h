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

#if __has_include("py.Windows.UI.Xaml.h")
#include "py.Windows.UI.Xaml.h"
#endif

#if __has_include("py.Windows.UI.Xaml.Interop.h")
#include "py.Windows.UI.Xaml.Interop.h"
#endif

#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.UI.Xaml.h>
#include <winrt/Windows.UI.Xaml.Interop.h>

#include <winrt/Windows.UI.Xaml.Data.h>

namespace py::proj::Windows::UI::Xaml::Data
{}

namespace py::impl::Windows::UI::Xaml::Data
{
    struct CurrentChangingEventHandler
    {
        static winrt::Windows::UI::Xaml::Data::CurrentChangingEventHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)](auto param0, auto param1)
            {
                auto gil = py::ensure_gil();

                py::pyobj_handle py_param0{ py::convert(param0) };

                if (!py_param0) {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw std::invalid_argument("param0");
                }

                py::pyobj_handle py_param1{ py::convert(param1) };

                if (!py_param1) {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw std::invalid_argument("param1");
                }

                py::pyobj_handle args{ PyTuple_Pack(2, py_param0.get(), py_param1.get()) };

                if (!args) {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }

                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }
            };
        };
    };

    struct PropertyChangedEventHandler
    {
        static winrt::Windows::UI::Xaml::Data::PropertyChangedEventHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)](auto param0, auto param1)
            {
                auto gil = py::ensure_gil();

                py::pyobj_handle py_param0{ py::convert(param0) };

                if (!py_param0) {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw std::invalid_argument("param0");
                }

                py::pyobj_handle py_param1{ py::convert(param1) };

                if (!py_param1) {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw std::invalid_argument("param1");
                }

                py::pyobj_handle args{ PyTuple_Pack(2, py_param0.get(), py_param1.get()) };

                if (!args) {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }

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

namespace py::wrapper::Windows::UI::Xaml::Data
{
    using Binding = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::Binding>;
    using BindingBase = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::BindingBase>;
    using BindingExpression = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::BindingExpression>;
    using BindingExpressionBase = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::BindingExpressionBase>;
    using BindingOperations = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::BindingOperations>;
    using CollectionViewSource = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::CollectionViewSource>;
    using CurrentChangingEventArgs = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::CurrentChangingEventArgs>;
    using ItemIndexRange = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::ItemIndexRange>;
    using PropertyChangedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::PropertyChangedEventArgs>;
    using RelativeSource = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::RelativeSource>;
    using ICollectionView = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::ICollectionView>;
    using ICollectionViewFactory = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::ICollectionViewFactory>;
    using ICollectionViewGroup = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::ICollectionViewGroup>;
    using ICustomProperty = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::ICustomProperty>;
    using ICustomPropertyProvider = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::ICustomPropertyProvider>;
    using IItemsRangeInfo = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::IItemsRangeInfo>;
    using INotifyPropertyChanged = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::INotifyPropertyChanged>;
    using ISelectionInfo = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::ISelectionInfo>;
    using ISupportIncrementalLoading = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::ISupportIncrementalLoading>;
    using IValueConverter = py::winrt_wrapper<winrt::Windows::UI::Xaml::Data::IValueConverter>;
    using LoadMoreItemsResult = py::winrt_struct_wrapper<winrt::Windows::UI::Xaml::Data::LoadMoreItemsResult>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Xaml::Data::BindingMode> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Xaml::Data::RelativeSourceMode> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Xaml::Data::UpdateSourceTrigger> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::UI::Xaml::Data::LoadMoreItemsResult> = "T{I:count:}";


    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::BindingMode>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "BindingMode";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::RelativeSourceMode>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "RelativeSourceMode";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::UpdateSourceTrigger>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "UpdateSourceTrigger";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::Binding>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "Binding";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::BindingBase>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "BindingBase";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::BindingExpression>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "BindingExpression";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::BindingExpressionBase>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "BindingExpressionBase";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::BindingOperations>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "BindingOperations";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::CollectionViewSource>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "CollectionViewSource";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::CurrentChangingEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "CurrentChangingEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::ItemIndexRange>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "ItemIndexRange";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::PropertyChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "PropertyChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::RelativeSource>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "RelativeSource";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::ICollectionView>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "ICollectionView";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::ICollectionViewFactory>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "ICollectionViewFactory";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::ICollectionViewGroup>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "ICollectionViewGroup";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::ICustomProperty>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "ICustomProperty";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::ICustomPropertyProvider>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "ICustomPropertyProvider";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::IItemsRangeInfo>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "IItemsRangeInfo";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::INotifyPropertyChanged>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "INotifyPropertyChanged";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::ISelectionInfo>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "ISelectionInfo";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::ISupportIncrementalLoading>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "ISupportIncrementalLoading";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::IValueConverter>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "IValueConverter";
    };

    template<>
    struct py_type<winrt::Windows::UI::Xaml::Data::LoadMoreItemsResult>
    {
        static constexpr const char* module_name = "winrt.windows.ui.xaml.data";
        static constexpr const char* type_name = "LoadMoreItemsResult";
    };
    template <>
    struct delegate_python_type<winrt::Windows::UI::Xaml::Data::CurrentChangingEventHandler>
    {
        using type = py::impl::Windows::UI::Xaml::Data::CurrentChangingEventHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::UI::Xaml::Data::PropertyChangedEventHandler>
    {
        using type = py::impl::Windows::UI::Xaml::Data::PropertyChangedEventHandler;
    };

}
