# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='py_csv_to_json',
    version='0.0.1',
    description='Converting the csv file to json using python',
    long_description=readme,
    author='Quadyster Cloud Devs',
    author_email='',
    url='https://github.com/quad-cloud/py_csv_to_json.git',
    packages=find_packages(exclude=('docs'))
)
