import unittest

from src.sql.model import Variable


class TestVariable(unittest.TestCase):

    def test_select_all(self):
        #variable = Variable("key-1", "value-1")
        Variable.create("key_2", "value", True)
