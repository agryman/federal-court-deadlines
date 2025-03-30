import pytest
import datetime
from deadlines.due_dates import deadline
from deadlines.examples import *

@pytest.mark.parametrize(
    "example",
    [
        general_example_1,
        general_example_2,
        general_example_3,
        holidays_weekends_example_1,
        holidays_weekends_example_2,
        summer_recess_example_1,
        seasonal_recess_example_1,
        seasonal_recess_example_2,
        seasonal_recess_example_3,
    ]
)
def test_deadline_guideline_example(example):
    """
    Test the deadline function with a Guideline example.
    """
    event_date: datetime = example.event_date
    number_of_days: int = example.number_of_days
    after_event: bool = example.after_event
    deadline_date: datetime = example.deadline_date

    assert deadline(event_date, number_of_days, after_event) == deadline_date
