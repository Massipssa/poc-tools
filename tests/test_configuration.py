import unittest

from src.configuration import database_config


class TestConfiguration(unittest.TestCase):

    def test_database_config(self):
        url, username, pwd = database_config()
        self.assertEqual(url, "postgresql://admin:admin1234@localhost:5432/testdb")
        self.assertEqual(username, "admin")
        self.assertEqual(pwd, "admin1234")
