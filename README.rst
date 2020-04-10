RandomFileTree: Generate random file tree
===========================================================================

|Build Status| |Coveralls| |Doc Status| |Pypi status| |Chat| |License|

.. |Build Status| image:: https://travis-ci.org/klieret/RandomFileTree.svg?branch=master
   :target: https://travis-ci.org/klieret/RandomFileTree

.. |Coveralls| image:: https://coveralls.io/repos/github/klieret/RandomFileTree/badge.svg?branch=master
   :target: https://coveralls.io/github/klieret/RandomFileTree?branch=master

.. |Doc Status| image:: https://readthedocs.org/projects/randomfiletree/badge/?version=latest
   :target: https://randomfiletree.readthedocs.io/
   :alt: Documentation Status

.. |Pypi Status| image:: https://badge.fury.io/py/RandomFileTree.svg
    :target: https://badge.fury.io/py/RandomFileTree
    :alt: Pypi status

.. |Chat| image:: https://img.shields.io/gitter/room/RandomFileTree/community.svg
   :target: https://gitter.im/RandomFileTree/community
   :alt: Gitter

.. |License| image:: https://img.shields.io/github/license/klieret/RandomFileTree.svg
   :target: https://github.com/klieret/RandomFileTree/blob/master/LICENSE.txt
   :alt: License

.. start-body

Description
-----------

Create a random file and directory tree/structure for testing purposes.


Installation
------------

``AnkiPandas`` can be installed with the python package manager:

.. code:: sh

    pip3 install randomfiletree

For a local installation, you might want to use the ``--user`` switch of ``pip``.
You can also update your current installation with ``pip3 install --upgrade ankipandas``.

For the latest development version you can also work from a cloned version
of this repository:

.. code:: sh

    git clone https://github.com/klieret/randomfiletree/
    cd randomfiletree
    pip3 install --user .

Usage
-----

Simple command line interface:

.. code:: sh

    randomfiletree <folder> -f <file creation probability> -d <directory creation probability> -r <repeat>

Type ``randomfiletree -h`` to see all supported arguments.

If the executable is not in your path after installation, you can also use
``python3 -m randomfiletree <arguments as above>``.

.. code:: python

    import randomfiletree

    randomfiletree.iterative_gaussian_tree("/path/to/basedir", nfiles=2.0, nfolders=0.5, maxdepth=5, repeat=4)


Randomfiletree will now crawl through all directories in ``/path/to/basedir`` and
create new files with the probabilities given in the arguments.

It is possible to pass an optional function to generate the random filenames oneself:

.. code:: python

    import random
    import string

    def fname():
        length = random.randint(5, 10)
        return "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
        ) + '.docx'

    randomfiletree.core.iterative_gaussian_tree("/path/to/basedir", nfiles=100, nfolders=10, maxdepth=2, filename=fname)

The ``payload`` optional argument can be used to generate file contents together with their names.
For example, it can be used to replicate some template files with randomized names:

.. code:: python

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
            name = target_dir / (randomfiletree.core.random_string() + srcfile[0])
            with open(name, 'wb') as f:
                f.write(srcfile[1])
            yield name

    randomfiletree.core.iterative_gaussian_tree("/path/to/basedir", nfiles=10, nfolders=10, maxdepth=5, repeat=4, payload=callback)

if both ``filename`` and ``payload`` passed, the first option is ignored.

**Take a look at the documentation_ to find out more about the additional functionality provided.**

.. _documentation: https://randomfiletree.readthedocs.io/

License
-------

This software is lienced under the `MIT license`_.

.. _MIT  license: https://github.com/klieret/ankipandas/blob/master/LICENSE.txt

.. end-body

