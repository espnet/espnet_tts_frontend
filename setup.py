#!/usr/bin/env python
import os
import subprocess

from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install

dirname = os.path.dirname(__file__)
if dirname == "":
    dirname = "."
dirname = os.path.abspath(dirname)


def install_hts_engine_API():
    subprocess.check_call(
        "cd " + dirname + " && "
        "git clone --depth 1 https://github.com/r9y9/hts_engine_API && "
        "cd hts_engine_API/src && "
        "./waf configure --prefix=../../build && ./waf build install",
        shell=True,
    )


def install_open_jtalk():
    subprocess.check_call(
        "cd " + dirname + " && "
        "git clone --depth 1 https://github.com/r9y9/open_jtalk && "
        "mkdir -p open_jtalk/src/build &&"
        "cd open_jtalk/src/build && "
        "cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON "
        "-DCMAKE_INSTALL_PREFIX=../../../build  .. && "
        "make install",
        shell=True,
    )


def install_pyopenjtalk():
    subprocess.check_call(
        "cd " + dirname + " && "
        "git clone --depth 1 https://github.com/r9y9/pyopenjtalk && "
        "OPEN_JTALK_INSTALL_PREFIX=" + dirname + "/build "
        "pip install -e pyopenjtalk",
        shell=True,
    )


class pyopenjtalk_install(install):
    def run(self):
        install_hts_engine_API()
        install_open_jtalk()
        install_pyopenjtalk()
        super(pyopenjtalk_install, self).run()


requirements = {
    "install": [
        "unidecode>=1.0.22",
        "inflect>=1.0.0",
        "underthesea",
        "jaconv",
        "g2p_en",
        "pypinyin",
    ],
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
    name="espnet_tts_frontend",
    version="0.0.2",
    long_description=open(os.path.join(dirname, 'README.md'),
                          encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="http://github.com/espnet/espnet_tts_frontend",
    packages=find_packages(include=["tacotron_cleaner*", "vietnamese_cleaner*"]),
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    cmdclass={"pyopenjtalk": pyopenjtalk_install},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
