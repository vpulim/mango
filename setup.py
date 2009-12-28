from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(
    name = "mango",
    version = "0.1",
    description = "Django session and auth backends using MongoDB",
    author = "Vinay Pulim",
    license = "BSD License",
    url = "http://github.com/vpulim/mango",
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
    install_requires = [
        'pymongo>=1.3',
    ]
)
