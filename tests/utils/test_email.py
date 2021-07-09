import unittest

import mock

from src.utils import email_sender

EMAILS = ["test1@email.com", "test2@email.com"]

send_email_test = mock.MagicMock()


class TestEmail(unittest.TestCase):

    def test_get_email_list_from_str_col_sep(self):
        email_colon_sep = "test1@email.com, test2@email.com"
        self.assertEqual(email_sender.get_email_list_from_str(email_colon_sep), EMAILS)

    def test_get_email_list_from_str_semi_col_sep(self):
        email_semi_colon_sep = "test1@email.com; test2@email.com"
        self.assertEqual(email_sender.get_email_list_from_str(email_semi_colon_sep), EMAILS)

    def test_get_email_address_list(self):
        email_colon_sep = "test1@email.com, test2@email.com"
        email_semi_colon_sep = "test1@email.com; test2@email.com"
        self.assertEqual(email_sender.get_email_address_list(email_colon_sep), EMAILS)
        self.assertEqual(email_sender.get_email_address_list(email_semi_colon_sep), EMAILS)
        self.assertEqual(email_sender.get_email_address_list(EMAILS), EMAILS)

    def test_get_email_address_list_invalid_type(self):
        emails_list = ["test1@email.com", 1]
        self.assertRaises(
            TypeError, email_sender.get_email_address_list, emails_list)

    """
    @mock.patch('src.utils.email')
    def test_send_email_once(self, mock_send_email):
        res = email_sender.send_email('to', 'subject', 'content')
        mock_send_email.assert_called_once_with('to', 'subject', 'content')
        self.assertEqual(mock_send_email.return_value, res)
    """
