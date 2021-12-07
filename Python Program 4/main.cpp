#include "nstetc.cpp"

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(nstetc, m)
{
    m.def("NonStatETC", &NonStatETC);
};

