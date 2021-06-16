import unittest
from unittest import mock

from tests.test_utils.config import conf_vars


def mock_local_file(content):
    with mock.patch(
        "src.basics.inspect_module.open", mock.mock_open(read_data=content)
    ) as file_mock, mock.patch("src.basics.inspect_module.os.path.exists", return_value=True):
        yield file_mock


class FileSecretParser(unittest.TestCase):

    @mock.patch("src.inspect_module.var_2")
    @mock.patch("src.inspect_module.var_1")
    def test_get_variables(self, mock_var_1, mock_var_2):
        """
        :param mock_var_1: first var to mock
        :param mock_var_2: second var to mock
        """
        # expected value by the mock
        mock_var_1.return_value = "expected_1"
        mock_var_2.return_value = "expected_2"

        # run test with function to test

        # called once with
        mock_var_1.assert_called_once_with(key="fak_var_key")
        # not called
        mock_var_2.not_called()

    @mock.patch.dict('os.environ', {
        'key': 'value',
    })
    def test_env_vars(self):
        pass

    @conf_vars({
        ("secrets", "backend"):
            "value1",
        ("secrets", "backend_kwargs"): '{"connections_prefix": "/value", "profile_name": null}',
    })
    def test_pass_conf_var_with_contextlib(self):
        pass