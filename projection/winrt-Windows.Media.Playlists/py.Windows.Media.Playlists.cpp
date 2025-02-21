// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#include "py.Windows.Media.Playlists.h"


namespace py::cpp::Windows::Media::Playlists
{
    // ----- Playlist class --------------------

    static PyObject* _new_Playlist(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        if (kwds != nullptr)
        {
            py::set_invalid_kwd_args_error();
            return nullptr;
        }

        auto arg_count = PyTuple_Size(args);
        if (arg_count == 0)
        {
            try
            {
                winrt::Windows::Media::Playlists::Playlist instance{  };
                return py::wrap(instance, type);
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static void _dealloc_Playlist(py::wrapper::Windows::Media::Playlists::Playlist* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* Playlist_LoadAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Media.Playlists.Playlist", L"LoadAsync", 1))
                {
                    py::set_arg_count_version_error(1);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::Windows::Storage::IStorageFile>(args, 0);

                return py::convert(winrt::Windows::Media::Playlists::Playlist::LoadAsync(param0));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* Playlist_SaveAsAsync(py::wrapper::Windows::Media::Playlists::Playlist* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 3)
        {
            try
            {
                if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Media.Playlists.Playlist", L"SaveAsAsync", 3))
                {
                    py::set_arg_count_version_error(3);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::Windows::Storage::IStorageFolder>(args, 0);
                auto param1 = py::convert_to<winrt::hstring>(args, 1);
                auto param2 = py::convert_to<winrt::Windows::Storage::NameCollisionOption>(args, 2);

                return py::convert(self->obj.SaveAsAsync(param0, param1, param2));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 4)
        {
            try
            {
                if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Media.Playlists.Playlist", L"SaveAsAsync", 4))
                {
                    py::set_arg_count_version_error(4);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::Windows::Storage::IStorageFolder>(args, 0);
                auto param1 = py::convert_to<winrt::hstring>(args, 1);
                auto param2 = py::convert_to<winrt::Windows::Storage::NameCollisionOption>(args, 2);
                auto param3 = py::convert_to<winrt::Windows::Media::Playlists::PlaylistFormat>(args, 3);

                return py::convert(self->obj.SaveAsAsync(param0, param1, param2, param3));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* Playlist_SaveAsync(py::wrapper::Windows::Media::Playlists::Playlist* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Media.Playlists.Playlist", L"SaveAsync", 0))
                {
                    py::set_arg_count_version_error(0);
                    return nullptr;
                }

                return py::convert(self->obj.SaveAsync());
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* Playlist_get_Files(py::wrapper::Windows::Media::Playlists::Playlist* self, void* /*unused*/) noexcept
    {
        try
        {
            if (!winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.Media.Playlists.Playlist", L"Files"))
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.Files());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _assign_array_Playlist(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Media::Playlists::Playlist>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_Playlist(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Media::Playlists::Playlist>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_Playlist[] = {
        { "save_as_async", reinterpret_cast<PyCFunction>(Playlist_SaveAsAsync), METH_VARARGS, nullptr },
        { "save_async", reinterpret_cast<PyCFunction>(Playlist_SaveAsync), METH_VARARGS, nullptr },
        { "_assign_array_", _assign_array_Playlist, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_Playlist), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_Playlist[] = {
        { "files", reinterpret_cast<getter>(Playlist_get_Files), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_Playlist[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_Playlist) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_Playlist) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_Playlist) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_Playlist) },
        { },
    };

    static PyType_Spec type_spec_Playlist =
    {
        "winrt._winrt_windows_media_playlists.Playlist",
        sizeof(py::wrapper::Windows::Media::Playlists::Playlist),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_Playlist
    };

    static PyGetSetDef getset_Playlist_Static[] = {
        { }
    };

    static PyMethodDef methods_Playlist_Static[] = {
        { "load_async", reinterpret_cast<PyCFunction>(Playlist_LoadAsync), METH_VARARGS, nullptr },
        { }
    };

    static PyType_Slot type_slots_Playlist_Static[] = 
    {
        { Py_tp_base, reinterpret_cast<void*>(&PyType_Type) },
        { Py_tp_getset, reinterpret_cast<void*>(getset_Playlist_Static) },
        { Py_tp_methods, reinterpret_cast<void*>(methods_Playlist_Static) },
        { }
    };

    static PyType_Spec type_spec_Playlist_Static =
    {
        "winrt._winrt_windows_media_playlists.Playlist_Static",
        static_cast<int>(PyType_Type.tp_basicsize),
        static_cast<int>(PyType_Type.tp_itemsize),
        Py_TPFLAGS_DEFAULT,
        type_slots_Playlist_Static
    };

    // ----- Windows.Media.Playlists Initialization --------------------
    PyDoc_STRVAR(module_doc, "Windows::Media::Playlists");


    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winrt_windows_media_playlists",
           module_doc,
           0,
           nullptr,
           nullptr,
           nullptr,
           nullptr,
           nullptr};

} // py::cpp::Windows::Media::Playlists

PyMODINIT_FUNC PyInit__winrt_windows_media_playlists(void) noexcept
{
    using namespace py::cpp::Windows::Media::Playlists;

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

    py::pyobj_handle type_Playlist_Static{PyType_FromSpec(&type_spec_Playlist_Static)};
    if (!type_Playlist_Static)
    {
        return nullptr;
    }

    if (py::register_python_type(module.get(), &type_spec_Playlist, object_bases.get(), reinterpret_cast<PyTypeObject*>(type_Playlist_Static.get())) == -1)
    {
        return nullptr;
    }


    return module.detach();
}
