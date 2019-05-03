#!/usr/bin/env python3

import argparse
from randomfiletree.core import iterative_gaussian_tree


def parser():
    _ = "Create random directory and file tree."
    parser = argparse.ArgumentParser(description=_)
    parser.add_argument(
        dest="basedir",
        help="Directory to create file/directory structure in"
    )
    parser.add_argument(
        "-d",
        "--directories",
        default=1,
        dest="nfolders",
        help="Average number of folders to create",
        type=float
    )
    parser.add_argument(
        "-f",
        "--files",
        default=1,
        dest="nfiles",
        help="Average number of files to create",
        type=float
    )
    parser.add_argument(
        "--files-sigma",
        default=1,
        dest="files_sigma",
        help="Spread of number of files created in each step",
        type=float
    )
    parser.add_argument(
        "--directories-sigma",
        default=1,
        dest="folders_sigma",
        help="Spread of number of folders created in each step",
        type=float
    )
    parser.add_argument(
        "-r",
        "--repeat",
        default=2,
        help="Number of times to traverse existing file/directory structure to "
             "create new elements",
        type=int
    )
    parser.add_argument(
        "--maxdepth",
        default=None,
        help="Maximal depth of file/directory structure to create",
        type=int
    )
    return parser


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
        sigma_folders=args.folders_sigma
    )


if __name__ == "__main__":
    cli()
