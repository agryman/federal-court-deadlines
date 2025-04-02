import pytest
import datetime
from deadlines.dates import format_date, parse_date
from deadlines.due_dates import deadline, dl
from deadlines.examples import guideline_examples


@pytest.mark.parametrize("example", guideline_examples)
def test_deadline_guideline_example(example):
    """
    Test the deadline function with a Guideline example.
    """
    event_date: datetime.date = example.event_date
    number_of_days: int = example.number_of_days
    after_event: bool = example.after_event
    expected_deadline_date: datetime.date = example.deadline_date

    deadline_date: datetime.date = deadline(event_date, number_of_days, after_event)

    assert  deadline_date == expected_deadline_date


@pytest.mark.parametrize("example", guideline_examples)
def test_dl_guideline_example(example):
    """
    Test the dl function with a Guideline example.
    """
    event_date: datetime.date = example.event_date
    number_of_days: int = example.number_of_days
    after_event: bool = example.after_event
    expected_deadline_date: datetime.date = example.deadline_date

    event_date_str: str = format_date(event_date)
    signed_number_of_days: int = number_of_days if after_event else -number_of_days

    deadline_date_str: str = dl(event_date_str, signed_number_of_days)
    deadline_date: datetime.date = parse_date(deadline_date_str)

    assert deadline_date == expected_deadline_date
