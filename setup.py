import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

cython_sources =  []
cython_sources.append('src/p2t.pyx')

cpp_sources = []
cpp_sources.append('poly2tri/common/shapes.cc')
cpp_sources.append('poly2tri/sweep/advancing_front.cc')
cpp_sources.append('poly2tri/sweep/cdt.cc')
cpp_sources.append('poly2tri/sweep/sweep.cc')
cpp_sources.append('poly2tri/sweep/sweep_context.cc')

extension = Extension("p2t",cython_sources + cpp_sources,language = "c++")
ext_modules = cythonize([extension])

setup(
    name = "poly2tri",
    version = "0.3.3",
    author = "Mason Green",
    description = "A 2D constrained Delaunay triangulation library",
    long_description = read('README'),
    url = "http://code.google.com/p/poly2tri/",
    ext_modules = ext_modules,
)
