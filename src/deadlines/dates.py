"""This module contains date functions useful for computing Federal Court due dates."""

import calendar
import datetime
from deadlines.canadian_holidays import calc_holidays
from deadlines.enums import Month, Weekday


def find_year(month:int, day:int, weekday:int, max_year: int) -> int:
    """
    Find the most recent year <= max_year in which the given (month, day, weekday)
    combination occurs.

    We can safely assume that we can always find a matching year.
    In fact,we only have to check the most recent 28 years since the
    pattern of weekdays repeats every 28 years. To see this recall
    that we have a leap year every 4 years, and every year must begin on
    one of 7 weekdays. The pattern of weekdays must therefore repeat
    every 4*7=28 years.

    Args:
        month: the month number, from 1 to 12
        day: the day, from 1 to 31
        weekday: the weekday number, from 0 to 6
        max_year: the maximum year to consider

    Returns:
        the most recent year <= max_year in which (month, day, weekday) occurs
    """

    # start from max_year and work backwards for 28 years
    year:int = max_year
    min_year:int = max_year - 28
    while year > min_year:
        date:datetime.date = datetime.date(year, month, day)
        date_weekday:int = datetime.date.weekday(date)
        if weekday == date_weekday:
            break
        else:
            year -= 1

    return year


def format_date(date: datetime.date) -> str:
    """
    Format a date object as an ISO string.

    Args:
        date: A datetime.date object.

    Returns:
        A string representation of the date in ISO format.
    """

    return date.isoformat()

def parse_date(yyyymmdd: str) -> datetime.date:
    """
    Parse an ISO date string into a date object.

    Args:
        yyyymmdd: A string representation of a date in ISO format.

    Returns:
        A datetime.date object.
    """

    return datetime.date.fromisoformat(yyyymmdd)


def add_days(date: datetime.date, n_days: int) -> datetime.date:
    """
    Add a specified number of days to a date.

    Args:
        date (datetime.date): The original date.
        n_days (int): The number of days to add.

    Returns:
        datetime.date: The new date, after adding the specified number of days.
    """
    return date + datetime.timedelta(days=n_days)


def next_date(date: datetime.date) -> datetime.date:
    """
    Get the next date after the given date.

    Args:
        date: the given date

    Returns:
        the next date
    """

    return add_days(date, 1)


def previous_date(date: datetime.date) -> datetime.date:
    """
    Get the previous date before the given date.

    Args:
        date: the given date

    Returns:
        the previous date
    """

    return add_days(date, -1)


def weekday_number(date: datetime.date) -> int:
    """
    Get the weekday number for a given date.
    The weekday number is an integer from 0 (Monday) to 6 (Sunday).

    Args:
        date: the given date

    Returns:
        the weekday number

    """
    return date.weekday()


def weekday_name(date: datetime.date) -> str:
    """
    Get the weekday name for a given date.
    The weekday name is a string representing the day of the week.

    Args:
        date: the given date

    Returns:
        the weekday name
    """

    return calendar.day_name[weekday_number(date)]


def is_weekend(date: datetime.date) -> bool:
    """
    Check if a given date falls on a weekend (Saturday or Sunday).

    Args:
        date: the given date

    Returns:
        True if the date is a weekend, False otherwise
    """

    return weekday_number(date) >= Weekday.SATURDAY


def is_business_day(date: datetime.date) -> bool:
    """
    Check if a given date is a business day (Monday to Friday).

    Args:
        date: the given date

    Returns:
        True if the date is a business day, False otherwise
    """

    return weekday_number(date) < Weekday.SATURDAY


def is_holiday(date: datetime.date, is_quebec: bool = False) -> bool:
    """
    Check if a given date is a holiday.
    This function is a placeholder and should be replaced with actual
    holiday checking logic.

    Args:
        date: the given date
        is_quebec: if True, check for Quebec holidays

    Returns:
        True if the date is a holiday, False otherwise
    """

    # get the holidays for the year
    all_holidays: dict[str, datetime.date] = calc_holidays(date.year, is_quebec)

    return date in all_holidays.values()


def is_recess(date: datetime.date) -> bool:
    """
    Check if a given date is during a court recess.
    This function is a placeholder and should be replaced with actual
    recess checking logic.

    Args:
        date: the given date

    Returns:
        True if the date is during a recess, False otherwise
    """

    # the Federal Court is in summer recess during the months of July and August
    if date.month in (Month.JULY, Month.AUGUST):
        return True

    # the Federal Court is in seasonal recess from December 21 to January 7

    if date.month == Month.DECEMBER and date.day >= 21:
        return True

    if date.month == Month.JANUARY and date.day <= 7:
        return True

    # the court is not in recess
    return False


def is_court_open(date: datetime.date, is_quebec: bool = False) -> bool:
    """
    Check if the court is open on a given date.
    The court is open if the date is a business day and not a holiday
    and the court is not in recess.

    Args:
        date: the given date
        is_quebec: if True, check for Quebec holidays

    Returns:
        True if the court is open, False otherwise
    """

    if is_weekend(date):
        return False

    assert is_business_day(date)

    if is_holiday(date, is_quebec):
        return False

    if is_recess(date):
        return False


    return True
