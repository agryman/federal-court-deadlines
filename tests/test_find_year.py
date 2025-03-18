
import pytest
import calendar
from deadlines.dates import find_year

@pytest.mark.parametrize(
    "month, day, weekday, max_year, expected",
    [
        (calendar.MAY, 1, calendar.TUESDAY, 2024, 2018),
        (calendar.MAY, 2, calendar.WEDNESDAY, 2024, 2018),
        (calendar.MARCH, 14, calendar.FRIDAY, 2025, 2025),
        (calendar.MARCH, 16, calendar.SUNDAY, 2025, 2025),
        (calendar.MARCH, 14, calendar.FRIDAY, 1997, 1997),
    ]
)
def test_find_year(month, day, weekday, max_year, expected):
    year = find_year(month, day, weekday, max_year)
    assert year == expected
