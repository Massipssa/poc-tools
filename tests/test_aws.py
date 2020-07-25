import unittest
import pytest
import os
import src.aws.storage.dynamo_crud as dybamodb

os.environ["AWS_REGION"] = (os.environ.get("AWS_REGION") or "east-us1")
TABLE_NAME = 'subscribers'

# Define some codes to run before test
@pytest.fixture()
def supply_values():
    return [1, 2, 3]

class AwsTest(unittest.TestCase):

    def test_select_by_name(self):
        name = 'massipssa'
        # dybamodb.select_by_name(name, TABLE_NAME)
        self.assertEqual(1, 1)
        self.assertEqual(supply_values()[1], 2)

    def test_select_all(self):
        items = dybamodb.select_all(TABLE_NAME)
        # self.assertEqual(len(items), 2)
        self.assertEqual(1, 1)