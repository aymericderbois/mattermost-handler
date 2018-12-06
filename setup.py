#!/usr/bin/env python

import setuptools
from distutils.core import setup

setup(
    name='mattermost-handler',
    version='1.0.2',
    description='A basic log handler for mattermost income url',
    author='Aymeric Derbois',
    author_email='aymeric@derbois.com',
    url='https://github.com/aymericderbois/py-mattermost-webhooks-log-handler',
    packages=['mattermost_handler'],
    install_requires=[
        'requests>=2.20.0',
    ]
)
