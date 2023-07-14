import unittest

from src.basics.data_struct import upper_names

class DsTest(unittest.TestCase):
    def test_upper_names(self):
        names_list = ["name1", "name2", "name3"]
        self.assertEqual(["NAME1", "NAME2", "NAME3"], upper_names(names_list))
