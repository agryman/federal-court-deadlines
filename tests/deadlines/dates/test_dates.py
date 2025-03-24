import pytest
import datetime
from deadlines.dates import is_business_day, is_weekend

@pytest.mark.parametrize(
    "date, expected",
    [
        (datetime.date(2023, 10, 2), True),  # Monday
        (datetime.date(2023, 10, 3), True),  # Tuesday
        (datetime.date(2023, 10, 4), True),  # Wednesday
        (datetime.date(2023, 10, 5), True),  # Thursday
        (datetime.date(2023, 10, 6), True),  # Friday
        (datetime.date(2023, 10, 7), False), # Saturday
        (datetime.date(2023, 10, 8), False)  # Sunday
    ]
)
def test_is_business_day(date, expected):
    """
    Test the is_business_day function with various dates.
    """
    assert is_business_day(date) == expected

@pytest.mark.parametrize(
    "date, expected",
    [
        (datetime.date(2023, 10, 2), False),  # Monday
        (datetime.date(2023, 10, 3), False),  # Tuesday
        (datetime.date(2023, 10, 4), False),  # Wednesday
        (datetime.date(2023, 10, 5), False),  # Thursday
        (datetime.date(2023, 10, 6), False),  # Friday
        (datetime.date(2023, 10, 7), True),   # Saturday
        (datetime.date(2023, 10, 8), True)    # Sunday
    ]
)
def test_is_weekend(date, expected):
    """
    Test the is_weekend function with various dates.
    """
    assert is_weekend(date) == expected
