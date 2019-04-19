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

.. |Pypi Status| image:: https://badge.fury.io/py/randomfiletree.svg
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

Command line interface:

.. code:: sh

    randomfiletree <folder> -f <file creation probability> -d <directory creation probability> -r <repeat>

Type ``randomfiletree -h`` to see all supported arguments.

If the executable is not in your path after installation, you can also use
``python3 -m randomfiletree <arguments as above>``.

.. code:: python

    import randomfiletree

    randomfiletree.create_random_tree("/path/to/basedir", prob_file=2.0, prob_folder=0.5, maxdepth=5, repeat=10)


Take a look at the documentation_ to find out more about the additional functionality provided.

.. _documentation: https://randomfiletree.readthedocs.io/

License
-------

This software is lienced under the `MIT license`_.

.. _MIT  license: https://github.com/klieret/ankipandas/blob/master/LICENSE.txt

.. end-body

