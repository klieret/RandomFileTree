#!/usr/bin/env python3

import unittest
import tempfile
import pathlib
from randomfiletree.core import *
import random

random.seed(0)


class TestHelperFunctions(unittest.TestCase):
    def setUp(self):
        self.itries = 10

    def test_get_random_string(self):
        for i in range(self.itries):
            mi = random.randint(0, 10)
            ma = mi + random.randint(0, 10)
            ras = random_string(mi, ma)
            self.assertGreaterEqual(len(ras), mi)
            self.assertLessEqual(len(ras), ma)


class TestTreeCreation(unittest.TestCase):
    def setUp(self):
        self.basedir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.basedir.cleanup()

    def get_content(self):
        alldirs = []
        allfiles = []
        for root, dirs, files in os.walk(self.basedir.name):
            for d in dirs:
                alldirs.append(os.path.join(root, d))
            for file in files:
                allfiles.append(os.path.join(root, file))
        return alldirs, allfiles

    def test_create_random_tree_empty(self):
        iterative_gaussian_tree(self.basedir.name, -10, -10, 3, None)
        dirs, files = self.get_content()
        self.assertEqual(len(dirs) + len(files), 0)

    def test_create_random_files(self):
        iterative_gaussian_tree(self.basedir.name, 5, -10, 3, None)
        dirs, files = self.get_content()
        self.assertEqual(len(dirs), 0)
        self.assertGreater(len(files), 1)

    def test_create_random_dirs(self):
        iterative_gaussian_tree(self.basedir.name, -10, 2, 3, None)
        dirs, files = self.get_content()
        self.assertEqual(len(files), 0)
        self.assertGreater(len(dirs), 1)

    def test_create_both(self):
        iterative_gaussian_tree(self.basedir.name, 3, 3, 3, None)
        dirs, files = self.get_content()
        self.assertGreater(len(files), 1)
        self.assertGreater(len(dirs), 1)

    def test_limit_depth(self):
        iterative_gaussian_tree(self.basedir.name, 3, 2, 5, maxdepth=3)
        dirs, files = self.get_content()
        max_depth = \
            max(map(lambda x: x.count(os.sep), dirs)) - \
            self.basedir.name.count(os.sep)
        self.assertLessEqual(max_depth, 4)

    def test_fname(self):
        suffix = '.jpg'
        iterative_gaussian_tree(
            self.basedir.name, 3, 2, 5, maxdepth=3,
            filename=lambda: random_string()+suffix
        )
        _, files = self.get_content()
        for file in files:
            self.assertEqual(pathlib.Path(file).suffix, suffix)

    def test_payload(self):
        content = 'testtest'
        suffix = '.txt'

        def callback(target_dir: pathlib.Path) -> pathlib.Path:
            while True:
                path = target_dir / (random_string() + suffix)
                with path.open('w') as f:
                    f.write(content)
                yield path

        iterative_gaussian_tree(
            self.basedir.name, 3, 2, 5, maxdepth=3, payload=callback
        )
        _, files = self.get_content()
        for file in files:
            self.assertEqual(pathlib.Path(file).suffix, suffix)
            with open(file, 'r') as f:
                self.assertEqual(f.read(), content)


class TestChooseSample(unittest.TestCase):
    def setUp(self):
        self.basedir = tempfile.TemporaryDirectory()

    def reset(self):
        self.basedir.cleanup()
        self.basedir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.basedir.cleanup()

    def test_sample(self):
        self.reset()
        iterative_gaussian_tree(self.basedir.name, 5, 5, 4)
        dirs, files = sample_random_elements(self.basedir.name, 2, 2)
        self.assertEqual(len(set(dirs)), 2)
        self.assertEqual(len(set(files)), 2)

    def test_sample_raises(self):
        self.reset()
        with self.assertRaises(ValueError):
            sample_random_elements(self.basedir.name, 2, 2)

    def test_sample_ignore(self):
        self.reset()
        dirs, files = sample_random_elements(self.basedir.name, 2, 2, "ignore")
        self.assertEqual(len(set(dirs)), 0)
        self.assertEqual(len(set(files)), 0)
        self.reset()
        os.mkdir(os.path.join(self.basedir.name, "test"))
        dirs, files = sample_random_elements(self.basedir.name, 2, 2, "ignore")
        self.assertEqual(len(set(dirs)), 1)
        self.assertEqual(len(set(files)), 0)

    def test_choose(self):
        self.reset()
        iterative_gaussian_tree(self.basedir.name, 5, 5, 3)
        dirs, files = choose_random_elements(self.basedir.name, 5, 3)
        self.assertEqual(len(dirs), 5)
        self.assertEqual(len(files), 3)

    def test_choose_raise(self):
        self.reset()
        with self.assertRaises(ValueError):
            # noinspection PyUnusedLocal
            dirs, files = choose_random_elements(self.basedir.name, 5, 3)

    def test_choose_ignore(self):
        self.reset()
        dirs, files = choose_random_elements(self.basedir.name, 2, 2, "ignore")
        self.assertEqual(len(dirs), 0)
        self.assertEqual(len(files), 0)


if __name__ == "__main__":
    unittest.main()
