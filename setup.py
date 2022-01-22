#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import exists
from setuptools import setup, find_packages

author = 'mathcube'
email = 'mathcube7@gmail.com'
description = 'Tools for using SymPy'
name = 'sympytools'
year = '2022'
url = 'https://github.com/mathcube7/sympytools'
version = '0.0.1'

setup(
    name=name,
    author=author,
    author_email=email,
    url=url,
    version=version,
    packages=find_packages(),
    package_dir={name: name},
    include_package_data=True,
    license='MIT',
    description=description,
    long_description=open('README.md').read() if exists('README.md') else '',
    long_description_content_type="text/markdown",
    install_requires=['sphinx', 'sympy', 'IPython', 'ipywidgets', 'clipboard'
                      ],
    python_requires=">=3.6",
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 ],
    platforms=['ALL'],
)
