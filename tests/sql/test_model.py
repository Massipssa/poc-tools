import unittest
from sql.model import Variable


class TestModel(unittest.TestCase):

    def test_select_all(self):
       list = Variable.select_all()
       #print(len(list))