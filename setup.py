# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='algorithms_in_python',
    version='0.1.0',
    description='Algorithms in python',
    long_description=readme,
    author='Junior Teudjio Mbativou',
    author_email='teudjiombativou@gmail.com',
    url='https://github.com/teudjio',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

