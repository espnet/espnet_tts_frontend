#!/usr/bin/env python
import os

from setuptools import find_packages
from setuptools import setup

dirname = os.path.dirname(__file__)
if dirname == "":
    dirname = "."


requirements = {
    "install": ["unidecode", "inflect", "underthesea"],
    "setup": [],
    "test": [],
    "doc": []
}
install_requires = requirements["install"]
setup_requires = requirements["setup"]
tests_require = requirements["test"]
extras_require = {
    k: v for k, v in requirements.items() if k not in ["install", "setup"]
}

setup(
    name="tacotron_cleaner",
    version="0.0.0",
    url="http://github.com/espnet/espnet_tts_cleaner",
    packages=find_packages(include=["tacotron_cleaner*", "vietnamese_cleaner*"]),
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
