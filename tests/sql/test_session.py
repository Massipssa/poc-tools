import unittest
from sql.model import create_session


class TestSession(unittest.TestCase):

    def test_session(self):
        self.assertIsNone(create_session())