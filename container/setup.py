# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='sample',
    version='0.0.1',
    description='Shared Python package for EVs-IBM project',
    long_description=readme,
    author='Hugh Nguyen',
    author_email='test@test.com',
    url='https://github.com/HieuNguyen202/ppt',
    packages=find_packages(exclude=('tests', 'docs'))
)

