#!/usr/bin/env python3

"""Create random directory and file tree.

This is done in an iterative fashion: For every iteration, files and folders
are created based on set probabilities in all subfolders of the target folder.
"""

import argparse
from randomfiletree.core import iterative_gaussian_tree
from typing import no_type_check


def parser() -> argparse.ArgumentParser:
    _parser = argparse.ArgumentParser(description=__doc__)
    _parser.add_argument(
        dest="basedir", help="Directory to create file/directory structure in"
    )
    _parser.add_argument(
        "-d",
        "--directories",
        default=1,
        dest="nfolders",
        help="Average number of folders to create in every subfolder of the "
        " target folder in every iteration",
        type=float,
    )
    _parser.add_argument(
        "-f",
        "--files",
        default=1,
        dest="nfiles",
        help="Average number of files to create in every subfolder of the "
        "target folder in every iteration",
        type=float,
    )
    _parser.add_argument(
        "--files-sigma",
        default=1,
        dest="files_sigma",
        help="Spread of number of files created in each step",
        type=float,
    )
    _parser.add_argument(
        "--directories-sigma",
        default=1,
        dest="folders_sigma",
        help="Spread of number of folders created in each step",
        type=float,
    )
    _parser.add_argument(
        "-r",
        "--repeat",
        default=2,
        help="Number of times to traverse existing file/directory structure to "
        "create new elements",
        type=int,
    )
    _parser.add_argument(
        "--maxdepth",
        default=None,
        help="Maximal depth of file/directory structure to create",
        type=int,
    )
    return _parser


@no_type_check  # TODO rewrite function to make mypy happy with Optional args
def cli(args=None):
    if not args:
        args = parser().parse_args()
    iterative_gaussian_tree(
        basedir=args.basedir,
        nfiles=args.nfiles,
        nfolders=args.nfolders,
        repeat=args.repeat,
        maxdepth=args.maxdepth,
        sigma_files=args.files_sigma,
        sigma_folders=args.folders_sigma,
    )


if __name__ == "__main__":
    cli()
