// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"
static_assert(winrt::check_version(PYWINRT_VERSION, "0.0.0"), "Mismatched Py/WinRT headers.");


#include <winrt/Windows.Graphics.DirectX.h>

namespace py::proj::Windows::Graphics::DirectX
{}

namespace py::impl::Windows::Graphics::DirectX
{}

namespace py::wrapper::Windows::Graphics::DirectX
{
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Graphics::DirectX::DirectXAlphaMode> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Graphics::DirectX::DirectXColorSpace> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Graphics::DirectX::DirectXPixelFormat> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Graphics::DirectX::DirectXPrimitiveTopology> = "i";


    template<>
    struct py_type<winrt::Windows::Graphics::DirectX::DirectXAlphaMode>
    {
        static constexpr const char* module_name = "winrt.windows.graphics.directx";
        static constexpr const char* type_name = "DirectXAlphaMode";
    };

    template<>
    struct py_type<winrt::Windows::Graphics::DirectX::DirectXColorSpace>
    {
        static constexpr const char* module_name = "winrt.windows.graphics.directx";
        static constexpr const char* type_name = "DirectXColorSpace";
    };

    template<>
    struct py_type<winrt::Windows::Graphics::DirectX::DirectXPixelFormat>
    {
        static constexpr const char* module_name = "winrt.windows.graphics.directx";
        static constexpr const char* type_name = "DirectXPixelFormat";
    };

    template<>
    struct py_type<winrt::Windows::Graphics::DirectX::DirectXPrimitiveTopology>
    {
        static constexpr const char* module_name = "winrt.windows.graphics.directx";
        static constexpr const char* type_name = "DirectXPrimitiveTopology";
    };
}
