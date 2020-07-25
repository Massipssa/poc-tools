import unittest
from src.tasks import CeleryExecutor

celery = CeleryExecutor


class CeleryTest(unittest.TestCase):

    def test_start(self):
        print("ok")
        #celery.start()
