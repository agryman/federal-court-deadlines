"""
This module contains enumerations for various constants used in the application.
These enums were added to the `calendar` module in Python 3.12 but are not
available in earlier versions. This module provides a workaround for compatibility
with earlier versions of Python, especially Python 3.11.11 which is the version
provided in Google Colab as of 2025-03-31.
"""

from enum import IntEnum


class Month(IntEnum):
    """
    Enum for month numbers.
    """

    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class Weekday(IntEnum):
    """
    Enum for weekday numbers.
    """

    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
