import unittest
import tempfile
import os
from Repository import Repository, Logger, TerminalOutput


class TestRepository(unittest.TestCase):
    def test_stdout(self):
        logger = Logger(TerminalOutput())
        logger.open("Logger works!")

    def test_repository(self):
        _, path = tempfile.mkstemp()
        repo = Repository(path)
        self.assertEqual(repo.add_card("John", "abc"), True)
        self.assertEqual(repo.add_card("John", "abc"), False)
        self.assertEqual(repo.add_card("John", "cde"), False)
        self.assertEqual(repo.add_card("Ivan", "abc"), False)
        self.assertEqual(repo.is_authorized("abc"), True)
        self.assertEqual(repo.is_authorized("cde"), False)
        self.assertEqual(repo.get_name("abc"), "John")
        repo.disconnect()
        os.remove(path)
