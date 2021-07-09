import unittest

from src.settings import create_session


class TestSettings(unittest.TestCase):

    def test_create_session(self):
        create_session()
