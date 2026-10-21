from setuptools import setup, Extension
from glob import glob
import numpy as np

setup(
    ext_modules=[
        Extension(
            name="MPLn23d",
            sources=sorted(glob("src/*.c")),
            depends=["src/MPLn23d.h"],
            include_dirs=[np.get_include()]
        ),
    ]
)
