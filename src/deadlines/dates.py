"""This module contains functions relevant to Federal Court due dates."""

import datetime

def find_year(month:int, day:int, weekday:int, max_year: int) -> int:
    """
    Finds the most recent year <= max_year in which the given (month, day, weekday)
    combination occurs.

    Let's assume that we can always find a matching year.
    Then we only have to check the most recent 28 years since the
    pattern of weekdays repeats every 28 years. To see this recall
    that we have a leap year every 4 years, and every year must begin on
    one of 7 weekdays. The pattern of weekdays must therefore repeat
    every 4*7=28 years.

    :param month: the month number, from 1 to 12
    :param day: the day, from 1 to 31
    :param weekday: the weekday number, from 0 to 6
    :param max_year: the maximum year to consider
    :return: the most recent year <= max_year in which the given month and day fall on the given weekday
    """

    # start from max_year and work backwards for 28 years
    for year in range(max_year, max_year - 28, -1):
        date:datetime.date = datetime.date(year, month, day)
        date_weekday:int = datetime.date.weekday(date)
        if weekday == date_weekday:
            return year

    # we should never reach here
    assert False

    return year
