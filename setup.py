# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='cognitive_textanalytics',
    version='0.1.0',
    description='Python SDK for the Cognitive Text Analytics',
    long_description=readme,
    author='Microsoft',
    url='https://github.com/adgroc/Cognitive-TextAnalytics-Python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

