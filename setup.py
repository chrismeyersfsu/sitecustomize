#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name='sitecustomize',
    version='1.0.1',
    url='https://github.com/chrismeyersfsu/sitecustomize',
    author='Chris Meyers',
    author_email='cmeyers@ansible.com',
    keywords='environment addsitedir',
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    install_requires=[],
)
