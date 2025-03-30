"""
This module computes Canadian Federal holidays.

The definition of *holiday* is given by: https://laws-lois.justice.gc.ca/eng/acts/I-21/page-3.html
which states that:

**holiday** means any of the following days, namely,
* Sunday;
* New Year’s Day;
* Good Friday;
* Easter Monday;
* Christmas Day;
* the birthday or the day fixed by proclamation for the celebration of the birthday of the reigning Sovereign;
* Victoria Day;
* Canada Day;
* the first Monday in September, designated Labour Day;
* National Day for Truth and Reconciliation, which is observed on September 30;
* Remembrance Day;
* any day appointed by proclamation to be observed as a day of general prayer or
mourning or day of public rejoicing or thanksgiving;
* and any of the following additional days, namely,
    * (a) in any province, any day appointed by proclamation of the lieutenant governor of the province
    to be observed as a public holiday or as a day of general prayer or mourning or day of public rejoicing or
    thanksgiving within the province, and any day that is a non-juridical day by virtue of
    an Act of the legislature of the province, and
    * (b) in any city, town, municipality or other organized district, any day appointed to be observed
    as a civic holiday by resolution of the council or other authority charged with the administration of the civic or
    municipal affairs of the city, town, municipality or district; (jour férié)
"""

import calendar
import datetime
from functools import cache
from holidays import country_holidays, HolidayBase

# days listed at https://www.canada.ca/en/revenue-agency/services/tax/public-holidays.html
NEW_YEARS_DAY: str = "New Year's Day"
GOOD_FRIDAY: str = "Good Friday"
EASTER_SUNDAY: str = "Easter Sunday"
EASTER_MONDAY: str = "Easter Monday"
VICTORIA_DAY: str = "Victoria Day"
SAINT_JEAN_BAPTISTE_DAY: str = "Saint-Jean-Baptiste Day"
CANADA_DAY: str = "Canada Day"
CIVIC_HOLIDAY: str = "Civic Holiday"
LABOUR_DAY: str = "Labour Day"
NATIONAL_DAY_FOR_TRUTH_AND_RECONCILIATION: str = "National Day for Truth and Reconciliation"
REMEMBRANCE_DAY: str = "Remembrance Day"
THANKSGIVING_DAY: str = "Thanksgiving Day"
CHRISTMAS_DAY: str = "Christmas Day"
BOXING_DAY: str = "Boxing Day"

PUBLIC_HOLIDAYS: list[str] = [
    NEW_YEARS_DAY,
    GOOD_FRIDAY,
    EASTER_SUNDAY,
    EASTER_MONDAY,
    VICTORIA_DAY,
    SAINT_JEAN_BAPTISTE_DAY,
    CANADA_DAY,
    CIVIC_HOLIDAY,
    LABOUR_DAY,
    NATIONAL_DAY_FOR_TRUTH_AND_RECONCILIATION,
    THANKSGIVING_DAY,
    REMEMBRANCE_DAY,
    CHRISTMAS_DAY,
    BOXING_DAY,
]

QUEBEC_ONLY: list[str] = [SAINT_JEAN_BAPTISTE_DAY]

EXCLUDING_QUEBEC: list[str] = [CIVIC_HOLIDAY]

# these are the only holidays defined for Canada in the `holidays` package
HOLIDAYS_PACKAGE: list[str] = [
    NEW_YEARS_DAY,
    GOOD_FRIDAY,
    CANADA_DAY,
    LABOUR_DAY,
    CHRISTMAS_DAY,
]


def calc_first_monday(year:int, month:int) -> datetime.date:
    """
    Calculate the first Monday of a given month and year.

    Args:
        year: the year
        month: the month

    Returns:
        the date of the first Monday of the given month and year
    """

    # Calculate the first day of the month
    first_day_date: datetime.date = datetime.date(year, month, 1)

    # recall that weekdays are numbered from 0 (Monday) to 6 (Sunday)
    first_weekday: int = first_day_date.weekday()

    # Calculate the day of the month of the first Monday
    first_monday_day: int = 1 if first_weekday == calendar.MONDAY else 8 - first_weekday
    first_monday_date: datetime.date = datetime.date(year, month, first_monday_day)

    # assert that the first Monday is indeed a Monday
    assert first_monday_date.weekday() == calendar.MONDAY

    return first_monday_date


def calc_new_years_day(year:int) -> datetime.date:
    """
    Calculate New Year's Day for a given year.

    Args:
        year:

    Returns:
        the date of New Year's Day for the given year
    """
    # New Year's Day is celebrated on January 1
    return datetime.date(year, calendar.JANUARY, 1)


def calc_good_friday(year:int) -> datetime.date:
    """
    Calculate Good Friday for a given year.

    Args:
        year: the year

    Returns:
        the date of Good Friday for the given year
    """

    ca_holidays: HolidayBase = country_holidays('CA', years=year)
    matches:list[datetime.date] = ca_holidays.get_named(GOOD_FRIDAY, lookup='exact')

    # assert that there is exactly one match for Good Friday
    assert len(matches) == 1

    # assert that Good Friday is indeed a Friday
    assert matches[0].weekday() == calendar.FRIDAY

    return matches[0]


def calc_easter_sunday(year:int) -> datetime.date:
    """
    Calculate Easter Sunday for a given year.

    Args:
        year: the year

    Returns:
        the date of Easter Sunday for the given year
    """

    # Easter Sunday is 2 days after Good Friday
    return calc_good_friday(year) + datetime.timedelta(days=2)


def calc_easter_monday(year:int) -> datetime.date:
    """
    Calculate Easter Monday for a given year.

    Args:
        year: the year

    Returns:
        the date of Easter Monday for the given year
    """

    # Easter Monday is 3 days after Good Friday
    return calc_good_friday(year) + datetime.timedelta(days=3)


def calc_victoria_day(year:int) -> datetime.date:
    """
    Calculate Victoria Day for a given year.

    Args:
        year: the year

    Returns:
        the date of Victoria Day for the given year
    """

    # Victoria Day is celebrated on the last Monday before May 25
    may_25_date: datetime.date = datetime.date(year, calendar.MAY, 25)

    # recall that weekdays are numbered from 0 (Monday) to 6 (Sunday)
    may_25_weekday: int = may_25_date.weekday()

    # Calculate the gap between Victoria Day and May 25
    gap: int = may_25_weekday if may_25_weekday > calendar.MONDAY else 7
    victoria_day_date: datetime.date = may_25_date - datetime.timedelta(days=gap)

    # assert that Victoria Day is a Monday
    assert victoria_day_date.weekday() == calendar.MONDAY

    return victoria_day_date


def calc_saint_jean_baptiste_day(year:int) -> datetime.date:
    """
    Calculate Saint-Jean-Baptiste Day for a given year.

    Args:
        year: the year

    Returns:
        the date of Saint-Jean-Baptiste Day for the given year
    """

    # Saint-Jean-Baptiste Day is celebrated on June 24
    return datetime.date(year, calendar.JUNE, 24)


def calc_canada_day(year:int) -> datetime.date:
    """
    Calculate Canada Day for a given year.

    Args:
        year: the year

    Returns:
        the date of Canada Day for the given year
    """

    # Canada Day is normally celebrated on July 1
    july_1_date: datetime.date = datetime.date(year, calendar.JULY, 1)

    # If July 1 is a Sunday, Canada Day is celebrated on July 2
    if july_1_date.weekday() == calendar.SUNDAY:
        return datetime.date(year, calendar.JULY, 2)

    return july_1_date


def calc_civic_holiday(year:int) -> datetime.date:
    """
    Calculate Civic Holiday for a given year.

    Args:
        year: the year

    Returns:
        the date of Civic Holiday for the given year
    """

    # Civic Holiday is celebrated on the first Monday in August
    return calc_first_monday(year, calendar.AUGUST)


def calc_labour_day(year:int) -> datetime.date:
    """
    Calculate Labour Day for a given year.

    Args:
        year: the year

    Returns:
        the date of Labour Day for the given year
    """

    # Labour Day is celebrated on the first Monday in September
    return calc_first_monday(year, calendar.SEPTEMBER)


def calc_national_day_for_truth_and_reconciliation(year:int) -> datetime.date:
    """
    Calculate National Day for Truth and Reconciliation for a given year.

    Args:
        year: the year

    Returns:
        the date of National Day for Truth and Reconciliation for the given year
    """

    # National Day for Truth and Reconciliation is celebrated on September 30
    return datetime.date(year, calendar.SEPTEMBER, 30)

def calc_remembrance_day(year:int) -> datetime.date:
    """
    Calculate Remembrance Day for a given year.

    Args:
        year: the year

    Returns:
        the date of Remembrance Day for the given year
    """

    # Remembrance Day is celebrated on November 11
    return datetime.date(year, calendar.NOVEMBER, 11)

def calc_thanksgiving_day(year:int) -> datetime.date:
    """
    Calculate Thanksgiving Day for a given year.

    Args:
        year: the year

    Returns:
        the date of Thanksgiving Day for the given year
    """

    first_monday_date: datetime.date = calc_first_monday(year, calendar.OCTOBER)

    # Thanksgiving Day is celebrated on the second Monday in October
    return first_monday_date + datetime.timedelta(days=7)


def calc_christmas_day(year:int) -> datetime.date:
    """
    Calculate Christmas Day for a given year.

    Args:
        year: the year

    Returns:
        the date of Christmas Day for the given year
    """

    # Christmas Day is celebrated on December 25
    return datetime.date(year, calendar.DECEMBER, 25)


def calc_boxing_day(year:int) -> datetime.date:
    """
    Calculate Boxing Day for a given year.

    Args:
        year: the year

    Returns:
        the date of Boxing Day for the given year
    """

    # Boxing Day is celebrated on December 26
    return datetime.date(year, calendar.DECEMBER, 26)


@cache
def calc_holidays(year: int, is_quebec: bool = False) -> dict[str, datetime.date]:
    """
    Calculate the Canadian public holidays for a given year.
    Cache the results to avoid recomputing them.

    Args:
        year: the year
        is_quebec: if True, include Quebec holidays

    Returns:
        the dictionary of Canadian public holidays for the given year
    """

    all_holidays: dict[str, datetime.date] = {
        NEW_YEARS_DAY: calc_new_years_day(year),
        GOOD_FRIDAY: calc_good_friday(year),
        EASTER_SUNDAY: calc_easter_sunday(year),
        EASTER_MONDAY: calc_easter_monday(year),
        VICTORIA_DAY: calc_victoria_day(year),
        CANADA_DAY: calc_canada_day(year),
        LABOUR_DAY: calc_labour_day(year),
        NATIONAL_DAY_FOR_TRUTH_AND_RECONCILIATION: calc_national_day_for_truth_and_reconciliation(year),
        THANKSGIVING_DAY: calc_thanksgiving_day(year),
        REMEMBRANCE_DAY: calc_remembrance_day(year),
        CHRISTMAS_DAY: calc_christmas_day(year),
        BOXING_DAY: calc_boxing_day(year),
    }

    if is_quebec:
        all_holidays[SAINT_JEAN_BAPTISTE_DAY] = calc_saint_jean_baptiste_day(year)
    else:
        all_holidays[CIVIC_HOLIDAY] = calc_civic_holiday(year)

    return all_holidays
