import unittest

from monthinfo import monthinfo


class TEST_WEEK(unittest.TestCase):
    def test_setfirstweekda(self):
        monthinfo.setfirstweekday("tuesday")
        self.assertEqual(monthinfo.WEEK.first_day, 1)
        monthinfo.setfirstweekday("friday")
        self.assertEqual(monthinfo.WEEK.first_day, 4)

class Test_DayOfWeek(unittest.TestCase):
    def setUp(self) -> None:
        self.day_of_week = monthinfo.DayOfWeek(2022, 12)

    def test_first_week_day(self) -> str:
        self.assertEqual(self.day_of_week.first_week_day, "Thursday")

    def test_is_day_in_weekday(self):
        self.assertTrue(self.day_of_week.is_day_in_weekday(3, "Saturday"))
        self.assertFalse(self.day_of_week.is_day_in_weekday(5, "Saturday"))
