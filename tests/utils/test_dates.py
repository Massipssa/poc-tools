import unittest
from datetime import datetime, timedelta

import pendulum

from src.utils import dates


class TestDates(unittest.TestCase):

    """
    All possible cases must be tested
    """
    def test_days_ago(self):
        today = pendulum.today()
        today_midnight = pendulum.instance(datetime.fromordinal(today.date().toordinal()))

        assert dates.days_ago(0) == today_midnight
        assert dates.days_ago(100) == today_midnight + timedelta(days=-100)

        assert dates.days_ago(0, hour=3) == today_midnight + timedelta(hours=3)
        assert dates.days_ago(0, minute=3) == today_midnight + timedelta(minutes=3)
        assert dates.days_ago(0, second=3) == today_midnight + timedelta(seconds=3)
        assert dates.days_ago(0, microsecond=3) == today_midnight + timedelta(microseconds=3)
