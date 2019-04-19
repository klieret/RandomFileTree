#!/usr/bin/env python3

import argparse
from randomfiletree.core import create_random_tree


def parser():
    _ = "Create random directory and file tree."
    parser = argparse.ArgumentParser(description=_)
    parser.add_argument(
        dest="basedir",
        help="Directory to create file/directory structure in"
    )
    parser.add_argument(
        "-d",
        "--directory-probability",
        default=1,
        dest="prob_folder",
        help="Probability to create a folder",
        type=float
    )
    parser.add_argument(
        "-f",
        "--file-probability",
        default=1,
        dest="prob_file",
        help="Probability to create a file",
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
    create_random_tree(
        basedir=args.basedir,
        prob_file=args.prob_file,
        prob_folder=args.prob_folder,
        repeat=args.repeat,
        maxdepth=args.maxdepth
    )


if __name__ == "__main__":
    cli()
