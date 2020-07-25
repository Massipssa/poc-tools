import unittest
from aws.learn_python.tasks import CeleryExecutor

celery = CeleryExecutor


class CeleryTest(unittest.TestCase):

    def test_start(self):
        print("ok")
        #celery.start()
