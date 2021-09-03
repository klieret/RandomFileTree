# RandomFileTree: Generate random file tree
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![Build Status](https://travis-ci.org/klieret/RandomFileTree.svg?branch=master)](https://travis-ci.org/klieret/RandomFileTree)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/klieret/RandomFileTree/master.svg)](https://results.pre-commit.ci/latest/github/klieret/RandomFileTree/master)
[![Coveralls](https://coveralls.io/repos/github/klieret/RandomFileTree/badge.svg?branch=master)](https://coveralls.io/github/klieret/RandomFileTree?branch=master)
[![Documentation Status](https://readthedocs.org/projects/randomfiletree/badge/?version=latest)](https://randomfiletree.readthedocs.io/)
[![Pypi status](https://badge.fury.io/py/RandomFileTree.svg)](https://badge.fury.io/py/RandomFileTree)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Gitter](https://img.shields.io/gitter/room/RandomFileTree/community.svg)](https://gitter.im/RandomFileTree/community)
[![License](https://img.shields.io/github/license/klieret/RandomFileTree.svg)](https://github.com/klieret/RandomFileTree/blob/master/LICENSE.txt)
[![PR welcome](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg)](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project)

## Description

Create a random file and directory tree/structure for testing purposes.

## Installation

`AnkiPandas` can be installed with the python package manager:

```sh
pip3 install randomfiletree
```

For a local installation, you might want to use the `--user` switch of
`pip`. You can also update your current installation with
`pip3 install --upgrade ankipandas`.

For the latest development version you can also work from a cloned
version of this repository:

```sh
git clone https://github.com/klieret/randomfiletree/
cd randomfiletree
pip3 install --user .
```

## Usage
Take a look at the
[documentation](https://randomfiletree.readthedocs.io/) to for the
complete picture.

### Command line interface

Simple command line interface:

```sh
randomfiletree <folder> -f <file creation probability> -d <directory creation probability> -r <repeat>
```

Type `randomfiletree -h` to see all supported arguments.

If the executable is not in your path after installation, you can also
use `python3 -m randomfiletree <arguments as above>`.

## Python API

```python
import randomfiletree

randomfiletree.iterative_gaussian_tree(
    "/path/to/basedir",
    nfiles=2.0,
    nfolders=0.5,
    maxdepth=5,
    repeat=4
)
```

Randomfiletree will now crawl through all directories in
`/path/to/basedir` and create new files with the probabilities given in
the arguments.

### Advanced examples

It is possible to pass an optional function to generate the random
filenames oneself:

```python
import random
import string

def fname():
    length = random.randint(5, 10)
    return "".join(
        random.choice(string.ascii_uppercase + string.digits)
        for _ in range(length)
    ) + '.docx'

randomfiletree.core.iterative_gaussian_tree(
    "/path/to/basedir",
    nfiles=100,
    nfolders=10,
    maxdepth=2,
    filename=fname
)
```

The `payload` optional argument can be used to generate file contents
together with their names. For example, it can be used to replicate some
template files with randomized names:

```python
import itertools
import pathlib
import randomfiletree

def callback(target_dir: pathlib.Path) -> pathlib.Path:
    sourcedir = pathlib.Path("/path/to/templates/")
    sources = []
    for srcfile in sourcedir.iterdir():
        with open(srcfile, 'rb') as f:
            content = f.read()
        sources.append((srcfile.suffix, content))
    for srcfile in itertools.cycle(sources):
        path = target_dir / (randomfiletree.core.random_string() + srcfile[0])
        with path.open('wb') as f:
            f.write(srcfile[1])
        yield path

randomfiletree.core.iterative_gaussian_tree(
    "/path/to/basedir",
    nfiles=10,
    nfolders=10,
    maxdepth=5,
    repeat=4,
    payload=callback
)
```

if both `filename` and `payload` passed, the first option is ignored.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/bollwyvl"><img src="https://avatars.githubusercontent.com/u/45380?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nicholas Bollweg</b></sub></a><br /><a href="https://github.com/klieret/RandomFileTree/commits?author=bollwyvl" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/BubaVV"><img src="https://avatars.githubusercontent.com/u/2842580?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Vadym Markov</b></sub></a><br /><a href="https://github.com/klieret/RandomFileTree/commits?author=BubaVV" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## License

This software is lienced under the [MIT
license](https://github.com/klieret/ankipandas/blob/master/LICENSE.txt).
