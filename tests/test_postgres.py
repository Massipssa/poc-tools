import datetime as dt
import unittest

import pytest


#@pytest.mark.integration("postgres")
class TestPostgres(unittest.TestCase):

    def test_func(self):
        a = 10
        if isinstance(a, (int, float)) or a <= 10:
            print("Yes")
        date = dt.datetime.utcnow()
        print("Date: " + str(date))

    def test_list(self):
        my_list = [1, 2, 3, 4]
        if 1 in my_list:
            print("Exists " + str(my_list[0]))
            my_list.remove(1)
        print(f"Numeber {my_list.count(1)}")
        my_list.append(5)
        my_list.insert(4, 6)
        print(my_list)

    def test_uppper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_split(self):
        var = "Hello,world"
        self.assertEqual(var.split(","), ["Hello", "world"])

    @pytest.mark.integration("rabbitmq")
    @pytest.mark.backend("postgres")
    def test_select_all(self):
        pass

    @pytest.mark.parametrize("name", [
        "name1",
        "name2",
        "name3",
    ])
    def test_upper_name(self, name):
        print(name)
