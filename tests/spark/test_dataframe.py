import unittest
from src.spark.dataframe import explain_df, read_csv, top_five_destinations


class TestDataframe(unittest.TestCase):

    path = "file:///E:/DEV/dev-python/learn-python/tests/data/flight-data/csv/2010-summary.csv"

    def test_explain_df(self):
        explain_df(self.path)

    def test_top_five_destinations(self):
        df = read_csv(self.path)
        top_five_destinations(df)

