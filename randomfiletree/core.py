#!/usr/bin/env python3

import os
import random
import string
from pathlib import Path


def random_string(min_length=5, max_length=10):
    """
    Get a random string

    Args:
        min_length: Minimal length of string
        max_length: Maximal length of string
    Returns:
        Random string of ascii characters
    """
    length = random.randint(min_length, max_length)
    return ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for _ in range(length)
    )


def create_random_tree(basedir, prob_file=2, prob_folder=1, repeat=1,
                       maxdepth=None):
    """
    Create a random set of files and folders by repeatedly walking through the
    current tree and creating random files or subfolders with a certain kind
    of probability

    Args:
        basedir: Directory to create files and folders in
        prob_file: Probability to create a file in a directory
        prob_folder: Probability to create a
        repeat: Walk this often through the directory tree to create new
            subdirectories and files
        maxdepth: Maximum depth to descend into current file tree. If None,
            infinity.
    Returns:
        None
    """
    for i in range(repeat):
        for root, dirs, files in os.walk(str(basedir)):
            if random.random() < prob_folder:
                p = Path(root) / random_string()
                p.mkdir(exist_ok=True)
            if random.random() < prob_file:
                p = Path(root) / random_string()
                p.touch(exist_ok=True)
            if maxdepth and os.path.relpath(root, str(basedir)).count(os.sep) >= maxdepth:
                del dirs[:]


def choose_random_elements(basedir, n_dirs, n_files, onfail="raise"):
    """
    Select random files and directories. If all directories and files must be
    unique, use sample_random_elements instead.

    Args:
        basedir: Directory to scan
        n_dirs: Number of directories to pick
        onfail: What to do if there are no files or folders to pick from?
            Either 'raise' (raise ValueError) or 'ignore' (return empty list)
    Returns:
        (List of dirs, List of files), all as pathlib.Path objects.
    """
    alldirs = []
    allfiles = []
    for root, dirs, files in os.walk(str(basedir)):
        for d in dirs:
            alldirs.append(Path(root) / d)
        for file in files:
            allfiles.append(Path(root) / file)
    if n_dirs and not alldirs :
        if onfail == "raise":
            raise ValueError(
                "{} does not have subfolders, so cannot select "
                "directories."
            )
        else:
            selected_dirs = []
    else:
        selected_dirs = [random.choice(alldirs) for _ in range(n_dirs)]
    if n_files and not allfiles:
        if onfail == "raise":
            raise ValueError(
                "{} does not contain any files, so cannot select random files."
            )
        elif onfail == "ignore":
            selected_files = []
        else:
            raise ValueError("Unknown value for 'onfail' parameter.")
    else:
        selected_files = [random.choice(allfiles) for _ in range(n_files)]
    return selected_dirs, selected_files


def sample_random_elements(basedir, n_dirs, n_files, onfail="raise"):
    """
    Select random distinct files and directories. If the directories and files
    do not have to be distinct, use choose_random_elements instead.

    Args:
        basedir: Directory to scan
        n_dirs: Number of directories to pick
        n_files: Number of files to pick
        onfail: What to do if there are no files or folders to pick from?
            Either 'raise' (raise ValueError) or 'ignore' (return list with
            fewer elements)
    Returns:
        (List of dirs, List of files), all as pathlib.Path objects.
    """
    alldirs = []
    allfiles = []
    for root, dirs, files in os.walk(str(basedir)):
        for d in dirs:
            alldirs.append(Path(root) / d)
        for file in files:
            allfiles.append(Path(root) / file)
    if n_dirs and len(alldirs) < n_dirs:
        if onfail == "raise":
            raise ValueError(
                "{} does not have enough subfolders, so cannot select "
                "enough directories."
            )
        elif onfail == "ignore":
            selected_dirs = random.sample(alldirs, len(alldirs))
        else:
            raise ValueError("Unknown value for 'onfail' parameter.")
    else:
        selected_dirs = random.sample(alldirs, n_dirs)
    if n_files and len(allfiles) < n_files:
        if onfail == "raise":
            raise ValueError(
                "{} does not contain enough files, so cannot select "
                "enough random files."
            )
        elif onfail == "ignore":
            selected_files = random.sample(allfiles, len(allfiles))
        else:
            raise ValueError("Unknown value for 'onfail' parameter.")
    else:
        selected_files = random.sample(allfiles, n_files)
    return selected_dirs, selected_files
