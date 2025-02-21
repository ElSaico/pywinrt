// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#include "py.Windows.Graphics.Effects.h"


namespace py::cpp::Windows::Graphics::Effects
{
    // ----- IGraphicsEffect interface --------------------

    static PyObject* _new_IGraphicsEffect(PyTypeObject* /*unused*/, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        static_assert(py::py_type<winrt::Windows::Graphics::Effects::IGraphicsEffect>::type_name);
        py::set_invalid_activation_error(py::py_type<winrt::Windows::Graphics::Effects::IGraphicsEffect>::type_name);
        return nullptr;
    }

    static void _dealloc_IGraphicsEffect(py::wrapper::Windows::Graphics::Effects::IGraphicsEffect* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* IGraphicsEffect_get_Name(py::wrapper::Windows::Graphics::Effects::IGraphicsEffect* self, void* /*unused*/) noexcept
    {
        try
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Graphics.Effects.IGraphicsEffect", L"Name"))
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.Name());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int IGraphicsEffect_put_Name(py::wrapper::Windows::Graphics::Effects::IGraphicsEffect* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Graphics.Effects.IGraphicsEffect", L"Name"))
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return -1;
            }

            auto param0 = py::convert_to<winrt::hstring>(arg);

            self->obj.Name(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* _assign_array_IGraphicsEffect(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Graphics::Effects::IGraphicsEffect>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_IGraphicsEffect(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Graphics::Effects::IGraphicsEffect>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_IGraphicsEffect[] = {
        { "_assign_array_", _assign_array_IGraphicsEffect, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_IGraphicsEffect), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_IGraphicsEffect[] = {
        { "name", reinterpret_cast<getter>(IGraphicsEffect_get_Name), reinterpret_cast<setter>(IGraphicsEffect_put_Name), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_IGraphicsEffect[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_IGraphicsEffect) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_IGraphicsEffect) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_IGraphicsEffect) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_IGraphicsEffect) },
        { },
    };

    static PyType_Spec type_spec_IGraphicsEffect =
    {
        "winrt._winrt_windows_graphics_effects.IGraphicsEffect",
        sizeof(py::wrapper::Windows::Graphics::Effects::IGraphicsEffect),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_IGraphicsEffect
    };

    // ----- IGraphicsEffectSource interface --------------------

    static PyObject* _new_IGraphicsEffectSource(PyTypeObject* /*unused*/, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        static_assert(py::py_type<winrt::Windows::Graphics::Effects::IGraphicsEffectSource>::type_name);
        py::set_invalid_activation_error(py::py_type<winrt::Windows::Graphics::Effects::IGraphicsEffectSource>::type_name);
        return nullptr;
    }

    static void _dealloc_IGraphicsEffectSource(py::wrapper::Windows::Graphics::Effects::IGraphicsEffectSource* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* _assign_array_IGraphicsEffectSource(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Graphics::Effects::IGraphicsEffectSource>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_IGraphicsEffectSource(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Graphics::Effects::IGraphicsEffectSource>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_IGraphicsEffectSource[] = {
        { "_assign_array_", _assign_array_IGraphicsEffectSource, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_IGraphicsEffectSource), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_IGraphicsEffectSource[] = {
        { }
    };

    static PyType_Slot _type_slots_IGraphicsEffectSource[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_IGraphicsEffectSource) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_IGraphicsEffectSource) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_IGraphicsEffectSource) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_IGraphicsEffectSource) },
        { },
    };

    static PyType_Spec type_spec_IGraphicsEffectSource =
    {
        "winrt._winrt_windows_graphics_effects.IGraphicsEffectSource",
        sizeof(py::wrapper::Windows::Graphics::Effects::IGraphicsEffectSource),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_IGraphicsEffectSource
    };

    // ----- Windows.Graphics.Effects Initialization --------------------
    PyDoc_STRVAR(module_doc, "Windows::Graphics::Effects");


    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winrt_windows_graphics_effects",
           module_doc,
           0,
           nullptr,
           nullptr,
           nullptr,
           nullptr,
           nullptr};

} // py::cpp::Windows::Graphics::Effects

PyMODINIT_FUNC PyInit__winrt_windows_graphics_effects(void) noexcept
{
    using namespace py::cpp::Windows::Graphics::Effects;

    if (py::import_winrt_runtime() == -1)
    {
        return nullptr;
    }

    py::pyobj_handle module{PyModule_Create(&module_def)};

    if (!module)
    {
        return nullptr;
    }

    auto object_type = py::get_object_type();
    if (!object_type)
    {
        return nullptr;
    }

    py::pyobj_handle object_bases{PyTuple_Pack(1, object_type)};

    if (!object_bases)
    {
        return nullptr;
    }

    if (py::register_python_type(module.get(), &type_spec_IGraphicsEffect, object_bases.get(), nullptr) == -1)
    {
        return nullptr;
    }

    if (py::register_python_type(module.get(), &type_spec_IGraphicsEffectSource, object_bases.get(), nullptr) == -1)
    {
        return nullptr;
    }


    return module.detach();
}
