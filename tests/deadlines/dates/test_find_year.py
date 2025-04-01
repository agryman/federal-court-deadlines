
import pytest
import calendar
from deadlines.dates import Month, Weekday
from deadlines.dates import find_year

@pytest.mark.parametrize(
    "month, day, weekday, max_year, expected",
    [
        (Month.MAY, 1, Weekday.TUESDAY, 2024, 2018),
        (Month.MAY, 2, Weekday.WEDNESDAY, 2024, 2018),
        (Month.MARCH, 14, Weekday.FRIDAY, 2025, 2025),
        (Month.MARCH, 16, Weekday.SUNDAY, 2025, 2025),
        (Month.MARCH, 14, Weekday.FRIDAY, 1997, 1997),
    ]
)
def test_find_year(month, day, weekday, max_year, expected):
    year = find_year(month, day, weekday, max_year)
    assert year == expected
