#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import setuptools
from pathlib import Path

keywords = ["testing", "filetree", "tree"]

description = (
    "Create a random file/directory tree/structure in python for"
    "testing purposes."
)

this_dir = Path(__file__).resolve().parent

packages = setuptools.find_packages()

with (this_dir / "README.rst").open() as fh:
    long_description = fh.read()

with (this_dir / "randomfiletree" / "version.txt").open() as vf:
    version = vf.read()

setuptools.setup(
    name="RandomFileTree",
    version=version,
    packages=packages,
    url="https://github.com/klieret/RandomFileTree",
    project_urls={
        "Bug Tracker": "https://github.com/klieret/RandomFileTree/issues",
        "Documentation": "https://randomfiletree.readthedocs.io/",
        "Source Code": "https://github.com/klieret/RandomFileTree/",
    },
    package_data={
        "randomfiletree": ["version.txt"],
    },
    install_requires=[],
    license="MIT",
    entry_points={"console_scripts": ["randomfiletree=randomfiletree.cli:cli"]},
    keywords=keywords,
    description=description,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    include_package_data=True,
)
