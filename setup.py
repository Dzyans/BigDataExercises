from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("Ex3_3.pyx")
)
