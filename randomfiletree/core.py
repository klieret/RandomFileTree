#!/usr/bin/env python3

from typing import List, Tuple, Callable, Optional, Union
import os
import random
import string
from pathlib import Path, PurePath


def random_string(min_length=5, max_length=10) -> str:
    """
    Get a random string.

    Args:
        min_length: Minimal length of string
        max_length: Maximal length of string

    Returns:
        Random string of ascii characters
    """
    length = random.randint(min_length, max_length)
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )


def iterative_tree(
    basedir: Union[str, PurePath],
    nfolders_func: Callable,
    nfiles_func: Callable,
    repeat=1,
    maxdepth=None,
    filename=random_string,
    payload: Optional[Callable[[Path], Path]] = None
) -> Tuple[List[Path], List[Path]]:
    """
    Create a random set of files and folders by repeatedly walking through the
    current tree and creating random files or subfolders (the number of files
    and folders created is chosen by evaluating a depth dependent function).

    Args:
        basedir:  Directory to create files and folders in
        nfolders_func: (depth) that returns the number of folders to be
            created in a folder of that depth.
        nfiles_func: Function(depth) that returns the number of files to be
            created in a folder of that depth.
        repeat: Walk this often through the directory tree to create new
            subdirectories and files
        maxdepth: Maximum depth to descend into current file tree. If None,
            infinity.
        filename: Callable to generate filename. Default returns short
            random string
        payload: Use this argument to generate files with content: Specify a
            function that takes a directory ``dir`` (``Path`` object) as
            argument, picks a name ``name``, creates the corresponding file
            ``dir/name`` and returns ``name``. Overrides ``filename`` argument
            if both are passed. Takes Path object as catalog where to create
            file and returns Path of created file.
            If this option is not specified, all created files will be empty.

    Returns:
        (List of dirs, List of files), all as pathlib.Path objects.
    """
    alldirs = []
    allfiles = []
    basedir = Path(basedir)
    basedir.mkdir(parents=True, exist_ok=True)
    for i in range(repeat):
        for root, dirs, files in os.walk(str(basedir)):
            depth = os.path.relpath(root, str(basedir)).count(os.sep)
            if maxdepth and depth >= maxdepth - 1:
                del dirs[:]
            n_folders = nfolders_func(depth)
            n_files = nfiles_func(depth)
            for _ in range(n_folders):
                p = Path(root) / random_string()
                p.mkdir(exist_ok=True)
                alldirs.append(p)
            if not payload:
                for _ in range(n_files):
                    p = Path(root) / filename()
                    p.touch(exist_ok=True)
                    allfiles.append(p)
            else:
                payload_generator = payload(Path(root))
                for _ in range(n_files):
                    p = next(payload_generator)
                    allfiles.append(p)

    alldirs = list(set(alldirs))
    allfiles = list(set(allfiles))
    return alldirs, allfiles


def iterative_gaussian_tree(
    basedir: Union[str, PurePath],
    nfiles=2,
    nfolders=1,
    repeat=1,
    maxdepth=None,
    sigma_folders=1,
    sigma_files=1,
    min_folders=0,
    min_files=0,
    filename=random_string,
    payload: Optional[Callable[[Path], Path]] = None
):
    """
    Create a random set of files and folders by repeatedly walking through the
    current tree and creating random files or subfolders (the number of files
    and folders created is chosen from a Gaussian distribution).

    Args:
        basedir: Directory to create files and folders in
        nfiles: Average number of files to create
        nfolders: Average number of folders to create
        repeat: Walk this often through the directory tree to create new
            subdirectories and files
        maxdepth: Maximum depth to descend into current file tree. If None,
            infinity.
        sigma_folders: Spread of number of folders
        sigma_files: Spread of number of files
        min_folders: Minimal number of folders to create. Default 0.
        min_files: Minimal number of files to create. Default 0.
        filename: Callable to generate filename. Default returns short
            random string
        payload: Use this argument to generate files with content: Specify a
            function that takes a directory ``dir`` (``Path`` object) as
            argument, picks a name ``name``, creates the corresponding file
            ``dir/name`` and returns ``name``. Overrides ``filename`` argument
            if both are passed. Takes Path object as catalog where to create
            file and returns Path of created file.
            If this option is not specified, all created files will be empty.

    Returns:
       (List of dirs, List of files), all as :class:`pathlib.Path` objects.
    """
    # noinspection PyUnusedLocal
    def nfolders_func(*args):
        return max(min_folders, int(random.gauss(nfolders, sigma_folders)))

    # noinspection PyUnusedLocal
    def nfiles_func(*args):
        return max(min_files, int(random.gauss(nfiles, sigma_files)))

    return iterative_tree(
        basedir=basedir,
        nfiles_func=nfiles_func,
        nfolders_func=nfolders_func,
        repeat=repeat,
        maxdepth=maxdepth,
        filename=filename,
        payload=payload
    )


def choose_random_elements(basedir, n_dirs, n_files, onfail="raise"):
    """
    Select random files and directories. If all directories and files must be
    unique, use sample_random_elements instead.

    Args:
        basedir: Directory to scan
        n_dirs: Number of directories to pick
        n_files: Number of files to pick
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
    if n_dirs and not alldirs:
        if onfail == "raise":
            raise ValueError(
                "{} does not have subfolders, so cannot select directories."
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
