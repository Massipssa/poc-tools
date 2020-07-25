import unittest
from unittest import mock
from src.test_learn import rm


class RmTestMock(unittest.TestCase):

    filename = "../conf/test.txt"
    """
    def setUp(self):
        with open(self.filename, 'w') as file:
            file.write('Delete me')

    @mock.patch('src.test_learn.os')
    def test_rm(self, mock_os):
        rm("any path")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")
        rm(self.filename)
        self.assertFalse(os.path.isfile(self.filename), "Failed to remove the file")
    """
