# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

install_requires = ['pylama']


setup(
    name='pre_commit_python_pylama',
    description='A pre-commit hook that run pylama.',
    url='https://github.com/iXioN/pylama-pre-commit.git',
    version='1.0.1',

    author='Antonin Lacombe',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'pylama_wrapper = pre_commit_hook.pylama_wrapper:main',
        ],
    },
)
