import unittest
import calendar

from monthinfo import monthinfo


class Test_WEEK(unittest.TestCase):
    def test_setfirstweekda(self):
        monthinfo.setfirstweekday("tuesday")
        self.assertEqual(monthinfo.WEEK.first_day, 1)
        monthinfo.setfirstweekday("friday")
        self.assertEqual(monthinfo.WEEK.first_day, 4)

class Test_DayOfWeek(unittest.TestCase):
    def setUp(self) -> None:
        calendar = monthinfo.Month(2022, 12)
        self.day_of_week = monthinfo.DayOfWeek(calendar)

    def test_first_week_day(self) -> str:
        self.assertEqual(self.day_of_week.first_week_day, "Thursday")

    def test_is_day_in_weekday(self):
        self.assertTrue(self.day_of_week.is_day_in_weekday(3, "Saturday"))
        self.assertFalse(self.day_of_week.is_day_in_weekday(5, "Saturday"))

    def test_is_in_first_weekday(self):
        self.assertTrue(self.day_of_week.is_in_first_weekday(3, "Saturday"))

    def test_list_of_weekday(self):
        self.assertEqual(self.day_of_week.list_of_weekday("saturday"), [3, 10, 17, 24, 31])


    def test_number_of_weekday(self):
        self.assertEqual(self.day_of_week.number_of_weekday("saturday"), 5)
        self.assertEqual(self.day_of_week.number_of_weekday("monday"), 4)

    def test_number_of_weekends(self):
        self.assertEqual(self.day_of_week.number_of_weekends, 4.5)


    def test_is_weekend(self):
        self.assertTrue(self.day_of_week.is_weekend(3))
        self.assertFalse(self.day_of_week.is_weekend(2))














class Test_Month(unittest.TestCase):
    def setUp(self) -> None:
        monthinfo.setfirstweekday("saturday")
        self.month = monthinfo.Month(2022, 12)

    def test_list_of_days(self):
        self.assertEqual(self.month.list_of_days[0], 1)
        self.assertEqual(self.month.list_of_days[29], 30)

    def test_list_of_weeks(self):
        self.assertEqual(self.month.list_of_weeks[0], [0, 0, 0, 0, 0, 1, 2])
        self.assertEqual(self.month.list_of_weeks[
                         1], [3, 4, 5, 6, 7, 8, 9])

    def test_calendar(self):
        self.assertEqual(self.month.calendar[0][6], 2)

    def test_number_of_days(self):
        self.assertEqual(self.month.number_of_days, 31)

    def test_number_of_weeks(self):
        self.assertEqual(self.month.number_of_weeks, 6)
