import unittest

from src.sql.session import provide_session


class TestSession(unittest.TestCase):

    def fun(self):
        print("hello")

    def test_provide_session(self):
        provide_session("func")
