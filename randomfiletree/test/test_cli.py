#!/usr/bin/env python3

import unittest
import subprocess
import tempfile

# ours
from randomfiletree.cli import parser, cli


class TestCli(unittest.TestCase):
    def test_cli(self):
        with tempfile.TemporaryDirectory() as dirname:
            subprocess.run(["randomfiletree", dirname])

    def test_cli_module(self):
        with tempfile.TemporaryDirectory() as dirname:
           subprocess.run(["python3", "-m", "randomfiletree", dirname])

    def test_parser(self):
        p = parser()
        with tempfile.TemporaryDirectory() as dirname:
            cli(p.parse_args([dirname]))
            cli(p.parse_args([dirname, "-f", "0.5", "-d", "3", "-r", "3"]))
            cli(p.parse_args([dirname, "-f", "0.5", "-d", "3", "--maxdepth", "2"]))
