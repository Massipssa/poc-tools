import unittest
from src.spark.basics import odds_numbers, count_word


class TestBasics(unittest.TestCase):

    def test_odd_numbers(self):
        rdd = odds_numbers(range(0, 1000))
        self.assertEqual(rdd.count(), 500)

    def test_count_word(self):
        file_path = "file:///E:/DEV/dev-python/learn-python/tests/data/test.txt"
        self.assertEqual(count_word(file_path, "python"), 1)
