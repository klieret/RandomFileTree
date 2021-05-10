#!/usr/bin/env python3

# std
from distutils.core import setup
# noinspection PyUnresolvedReferences
import setuptools  # see below (1)
from pathlib import Path

# (1) see https://stackoverflow.com/questions/8295644/
# Without this import, install_requires won't work.


keywords = [
    "testing",
    "filetree",
    "tree"
]

description = "Create a random file/directory tree/structure in python for" \
              "testing purposes."

this_dir = Path(__file__).resolve().parent

packages = setuptools.find_packages()

with (this_dir / "README.rst").open() as fh:
    long_description = fh.read()

with (this_dir / "randomfiletree" / "version.txt").open() as vf:
    version = vf.read()

setup(
    name='RandomFileTree',
    version=version,
    packages=packages,
    url="https://github.com/klieret/RandomFileTree",
    project_urls={
        "Bug Tracker": "https://github.com/klieret/RandomFileTree/issues",
        "Documentation": "https://randomfiletree.readthedocs.io/",
        "Source Code": "https://github.com/klieret/RandomFileTree/",
    },
    package_data={
        'randomfiletree': ['version.txt'],
    },
    install_requires=[],
    license="MIT",
    scripts=["randomfiletree/bin/randomfiletree"],
    keywords=keywords,
    description=description,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
    ],
    include_package_data=True,
)
