import pybind11
from distutils.core import setup, Extension

ext_modules = [
    Extension(
        'nstetc',
        ['main.cpp'],
        include_dirs=[pybind11.get_include()],
        language='c++',
    ),
]

setup(
    name='nstetc',
    version='1.0.0',
    author='Debruine',
    description='NotStatETC extension',
    ext_modules = ext_modules,
    requires=['pybind11']
)
