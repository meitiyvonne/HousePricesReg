#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='regression_model',
    version='0.1.0',
    # The `find_packages()` function will automatically 
    # locate the `regression_model` module within the `packages/regression_model/` directory.
    packages=find_packages(where=".", exclude=()), 
)