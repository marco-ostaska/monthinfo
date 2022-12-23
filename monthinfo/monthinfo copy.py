import calendar
import datetime
from enum import Enum
from dataclasses import dataclass

FIRST_WEEK_DAY = calendar.SATURDAY


@dataclass()
class DayOfWeek:
    year: int
    month: int

    week_days = {0: "Monday", 1: "Tuesday", 2: "Wednesday",
                 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}


    def inverted_week_days(self) -> dict:
        return {value: key for key, value in self.week_days.items()}

    def get_first_day_from_weekday(self, weekday: str) -> int:
        for day in range(1,9):
            if self.week_days[datetime.date(self.year, self.month, day).weekday()] == weekday.capitalize():
                return day

    def get_first_week_day(self) -> str:
        """
        Returns the day of the week of the first day of the current month.

        Returns:
            A string representing the day of the week (e.g. "Monday").
        """
        return self.week_days[datetime.date(self.year, self.month, 1).weekday()]

    def is_day_in_weekday(self, day: int, weekday: str) -> bool:
        return datetime.date(self.year, self.month, day).weekday() == self.inverted_week_days()[weekday.capitalize()]


class Saturday(DayOfWeek):
    pass


class CurrentMonth(DayOfWeek):
    def __init__(self, month, year, first_week_day):
        calendar.setfirstweekday(first_week_day)
        self.month = month
        self.year = year


    def get_calendar_indexes_for_this_day(self, day):
        """
        Returns the indexes of the specified day in the month's calendar.

        The first index represents the week number (starting from 0), and the second
        index represents the day of the week (starting from 0). Days that are not
        part of the current month are represented by zeros in the calendar.

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A tuple containing two integers representing the indexes of the specified
            day in the month's calendar.

        Raises:
            ValueError: If the specified day is not in the current month.
        """
        for i, week in enumerate(self.calendar()):
            for j, d in enumerate(week):
                if d == day:
                    return i, j


    def number_of_saturdays(self) -> int:
        """
        Returns the number of Saturdays in the current month.

        Returns:
            An integer representing the number of Saturdays in the current month.
        """
        return len(self.list_of_saturdays())


    def is_first_sunday(self, day) -> bool:
        """
        Returns True if the specified day is the first Sunday of the month, False otherwise.

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A boolean indicating whether the specified day is the first Sunday of the month.

        Raises:
            ValueError: If the specified day is not in the current month.
        """
        return self.is_first_weekend(day) and self.is_sunday(day)

    def list_of_sundays(self) -> list:
        """
        Returns a list of the days in the current month that are Sundays.

        The list contains integers representing the days of the month, starting from 1.

        Returns:
            A list of integers representing the days of the month that are Sundays.
        """
        return [day for day in self.list_of_days() if self.is_sunday(day)]

    def number_of_sundays(self) -> int:
        """
        Returns the number of Sundays in the current month.

        Returns:
            An integer representing the number of Sundays in the current month.
        """
        return len(self.list_of_sundays())

    def is_weekend(self, day) -> bool:
        """
        Returns True if the specified day is a weekend day (Saturday or Sunday), False otherwise.

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A boolean indicating whether the specified day is a weekend day.

        Raises:
            ValueError: If the specified day is not in the current month.
        """
        return datetime.date(self.year, self.month, day).weekday() >= 5

    def is_first_weekend(self, day) -> bool:
        """
        Returns True if the specified day is in the first weekend of the month (Saturday or Sunday), False otherwise.

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A boolean indicating whether the specified day is in the first weekend of the month.

        Raises:
            ValueError: If the specified day is not in the current month.
        """
        return self.is_weekend(day) and day < 8



    def is_weekend(self, day) -> bool:
        """
        Returns True if the specified day is a weekend day (Saturday or Sunday), False otherwise.

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A boolean indicating whether the specified day is a weekend day.

        Raises:
            ValueError: If the specified day is not in the current month.
        """
        return datetime.date(self.year, self.month, day).weekday() >= 5

    def is_first_weekend(self, day) -> bool:
        """
        Returns True if the specified day is in the first weekend of the month (Saturday or Sunday), False otherwise.

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A boolean indicating whether the specified day is in the first weekend of the month.

        Raises:
            ValueError: If the specified day is not in the current month.
        """
        return self.is_weekend(day) and day < 8



    def is_first_monday(self, day) -> bool:
        """
        Returns True if the specified day is the first Monday of the month, False otherwise.

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A boolean indicating whether the specified day is the first Monday of the month.

        Raises:
            ValueError: If the specified day is not in the current month.
        """
        return self.is_monday(day) and day < 8

    def list_of_mondays(self) -> list:
        """
        Returns a list of days in the current month that are Mondays.

        Returns:
            A list of integers representing the days of the month that are Mondays.

        Example:
            If the current month is December 2022, the method would return [5, 12, 19, 26].
        """
        return [day for day in self.list_of_days() if self.is_monday(day)]

    def number_of_mondays(self) -> int:
        """
        Returns the number of Mondays in the current month.

        The number of Mondays is calculated by generating a list of all the days in the current month that are Mondays, and then returning the length of that list.

        Returns:
            An integer representing the number of Mondays in the current month.

        Example:
            If the current month is December 2022, the method would return 4.
        """
        return len(self.list_of_mondays())



    def is_first_tuesday(self, day) -> bool:
        """
        Returns True if the specified day is the first Tuesday of the month, False otherwise.

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A boolean indicating whether the specified day is the first Tuesday of the month.

        Raises:
            ValueError: If the specified day is not in the current month.
        """
        return self.is_tuesday(day) and day < 8

    def list_of_tuesdays(self) -> list:
        """
        Returns a list of days in the current month that are Tuesdays.

        Returns:
            A list of integers representing the days of the month that are Tuesdays.

        Example:
            If the current month is December 2022, the method would return [6, 13, 20, 27].
        """
        return [day for day in self.list_of_days() if self.is_tuesday(day)]

    def number_of_tuesdays(self) -> int:
        """
        Returns the number of Tuesdays in the current month.

        This method counts the number of occurrences of Tuesday in the current month,
        by calling the `list_of_tuesdays` method and returning the length of the
        resulting list of dates.

        Returns:
            The number of Tuesdays in the current month.
        """
        return len(self.list_of_tuesdays())


    def is_first_wednesday(self, day) -> bool:
        """Returns True if the specified day is the first Wednesday of the month, False otherwise.

        This method checks whether the specified day is both a Wednesday and the first
        Wednesday of the month. It does this by first calling the `is_wednesday` method
        to check whether the given day falls on a Wednesday, and then checking whether
        the day is before the 8th of the month (since the first week of the month always
        contains at most 7 days).

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A boolean indicating whether the specified day is the first Wednesday of the month.

        Raises:
            ValueError: If the specified day is not in the current month.
        """
        return self.is_wednesday(day) and day < 8

    def list_of_wednesdays(self) -> list:
        """
        Returns a list of days in the current month that are Wednesdays.

        Returns:
            A list of integers representing the days of the month that are Wednesdays.

        Example:
            If the current month is December 2022, the method would return [7, 14, 21, 28].
        """
        return [day for day in self.list_of_days() if self.is_wednesday(day)]

    def number_of_wednesdays(self) -> int:
        """
        Returns the number of Wednesdays in the current month.

        This method counts the number of occurrences of Wednesday in the current month,
        by calling the `list_of_wednesdays` method and returning the length of the
        resulting list of dates.

        Returns:
            The number of Wednesdays in the current month.
        """
        return len(self.list_of_wednesdays())


    def is_first_thursday(self, day) -> bool:
        """
        Returns True if the specified day is the first Thursday of the month, False otherwise.

        This method checks whether the specified day is both a Thursday and the first
        Thursday of the month. It does this by first calling the `is_thursday` method
        to check whether the given day falls on a Thursday, and then checking whether
        the day is before the 8th of the month (since the first week of the month always
        contains at most 7 days).

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A boolean indicating whether the specified day is the first Thursday of the month.

        Raises:
            ValueError: If the specified day is not in the current month.
        """
        return self.is_thursday(day) and day < 8

    def list_of_thursdays(self) -> list:
        """
        Returns a list of days in the current month that are Thursdays.

        Returns:
            A list of integers representing the days of the month that are Thursdays.

        Example:
            If the current month is December 2022, the method would return [8, 15, 22, 29].
        """
        return [day for day in self.list_of_days() if self.is_thursday(day)]

    def number_of_thursdays(self) -> int:
        """
        Returns the number of Thursdays in the current month.

        This method counts the number of occurrences of Thursday in the current month,
        by calling the `list_of_thursdays` method and returning the length of the
        resulting list of dates.

        Returns:
            The number of Thursdays in the current month.
        """
        return len(self.list_of_thursdays())



    def is_first_friday(self, day) -> bool:
        """
        Returns True if the specified day is the first Friday of the month, False otherwise.

        This method checks whether the specified day is both a Friday and the first
        Friday of the month. It does this by first calling the `is_friday` method
        to check whether the given day falls on a Friday, and then checking whether
        the day is before the 8th of the month (since the first week of the month always
        contains at most 7 days).

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A boolean indicating whether the specified day is the first Friday of the month.

        Raises:
            ValueError: If the specified day is not in the current month.
        """
        return self.is_friday(day) and day < 8

    def list_of_fridays(self) -> list:
        """
        Returns a list of days in the current month that are Fridays.

        Returns:
            A list of integers representing the days of the month that are Fridays.

        Example:
            If the current month is December 2022, the method would return [9, 16, 23, 30].
        """
        return [day for day in self.list_of_days() if self.is_friday(day)]

    def number_of_fridays(self) -> int:
        """
        Returns the number of Fridays in the current month.

        This method counts the number of occurrences of Friday in the current month,
        by calling the `list_of_fridays` method and returning the length of the
        resulting list of dates.

        Returns:
            The number of Fridays in the current month.
        """
        return len(self.list_of_fridays())

    def number_of_weekdays(self) -> int:
        """
        Returns the number of weekdays in the current month.

        This method returns the number of weekdays in the current month, by calling the
        `number_of_sundays` and `number_of_mondays` methods.

        Returns:
            The number of weekdays in the current month.
        """
        return self.number_of_days() - (self.number_of_saturdays() + self.number_of_sundays())
