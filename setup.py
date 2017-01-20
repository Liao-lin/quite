"""
QT UI Extension

Author: SF-Zhou
Date: 2016-08-07

See:
https://github.com/sf-zhou/quite
"""

from setuptools import setup, find_packages

setup(
    name='quite',
    version='0.0.3',
    description='QT UI Extension',
    url='https://github.com/sf-zhou/quite',

    author='SF-Zhou',
    author_email='sfzhou.scut@gmail.com',

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='qt ui',
    packages=find_packages(exclude=['docs', 'tests']),
    package_data={ 'quite': [
        './quite/tools/bin/pyside-rcc.exe',
        './quite/tools/bin/QtCore4.dll',
        './quite/tools/bin/QtXml4.dll'
    ]},
    install_requires=['st', 'prett']
)
