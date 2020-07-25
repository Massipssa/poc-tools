import unittest
from src.aws.learn_python import CeleryExecutor

celery = CeleryExecutor


class CeleryTest(unittest.TestCase):

    def test_start(self):
        print("ok")
        #celery.start()
