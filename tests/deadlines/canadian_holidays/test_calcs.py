import pytest
import calendar
import datetime
from deadlines.canadian_holidays import *

def test_calc_good_friday():
    good_friday: datetime.date = calc_good_friday(2012)
    assert good_friday == datetime.date(2012, calendar.APRIL, 6)

def test_calc_easter_sunday():
    easter_sunday: datetime.date = calc_easter_sunday(2012)
    assert easter_sunday == datetime.date(2012, calendar.APRIL, 8)

def test_calc_easter_monday():
    easter_monday: datetime.date = calc_easter_monday(2012)
    assert easter_monday == datetime.date(2012, calendar.APRIL, 9)
