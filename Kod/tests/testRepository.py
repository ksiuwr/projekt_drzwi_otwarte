import unittest
import subprocess
import tempfile
import os
from Repository import Repository
from GlobalState import logger


class TestRepository(unittest.TestCase):
    def test_stdout(self):
        logger.open("Logger works!")

    def test_repository(self):
        file, path = tempfile.mkstemp()
        testDir = os.path.dirname(__file__)
        sql1 = testDir + "/../SQL/1-create_basic_table.sql"
        sql2 = testDir + "/../SQL/2-create_log_table.sql"
        subprocess.run(["sh", "-c", "sqlite3 %s < %s" % (path, sql1)])
        subprocess.run(["sh", "-c", "sqlite3 %s < %s" % (path, sql2)])
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
