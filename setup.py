from setuptools import setup, Extension
from glob import glob
import numpy as np

setup(
    name='MPLn23d',
    version='0.0.1',
    install_requires=['numpy'],
    author='Kenjiro Sugio',
    author_email='ksugio@hiroshima-u.ac.jp',
    description='Measure features of second phases in microstructures of materilas',
    url='https://github.com/ksugio/MPImage',
    ext_modules=[
        Extension(
            name='MPLn23d',
            sources=glob('src/*.c'),
            include_dirs=[np.get_include()]
        )
    ]
)