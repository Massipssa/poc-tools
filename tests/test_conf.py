import unittest

from src.configuration import database_config


class TestConf(unittest.TestCase):

    def test_database_conf(self):

        db_conf = database_config()
        self.assertEqual(db_conf[0], "postgresql://airflow:airflow@localhost:5432/testdb")
        self.assertEqual(db_conf[1], "myuser")
        self.assertEqual(db_conf[2], "mypass")
