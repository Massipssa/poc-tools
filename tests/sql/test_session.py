import unittest
from src.sql import create_session


class TestSession(unittest.TestCase):

    def test_session(self):
        self.assertIsNone(create_session())