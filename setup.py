#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


setup(
    name='exodus',
    version='0.0.1',
    license=None,
    description='The exodus application bundler.',
    long_description='See the documentation for details.',
    author='Intoli',
    author_email='contact@intoli.com',
    url='https://github.com/intoli/exodus',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    keywords=[
        'linux', 'executable', 'elf', 'binaries',
    ],
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'exodus = exodus.cli:main',
        ],
    },
)
