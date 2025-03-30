"""This module computes due dates for Federal Court cases."""

import datetime
from deadlines.dates import add_days, is_court_open, is_recess


def deadline(event_date: datetime.date,
             number_of_days: int,
             after_event: bool = True,
             is_quebec: bool = False) -> datetime.date:
    """
    Compute the deadline for a given event date and number of days.

    Args:
        event_date: The date of the event.
        number_of_days: The number of days between the event date and deadline.
        after_event: If True, the deadline is after the event date; otherwise, it's before.
        is_quebec: If True, the deadline is calculated according to Quebec rules.

    Returns:
        The computed deadline date.

    Raises:
        ValueError: If number_of_days is negative.
    """

    if number_of_days < 0:
        raise ValueError("number_of_days must be non-negative")

    day_step: int = 1 if after_event else -1

    # compute the candidate date for the deadline
    candidate_date: datetime.date = event_date
    cumulative_days: int = 0
    while cumulative_days < number_of_days:
        candidate_date = add_days(candidate_date, day_step)

        # never count a recess day
        if is_recess(candidate_date):
            continue

        # if the allowed number of days is less than 7 then only count days on which the court is open
        if number_of_days < 7 and not is_court_open(candidate_date, is_quebec):
            continue

        # count the day
        cumulative_days += 1

    # the deadline must be a business day
    deadline_date: datetime.date = candidate_date
    while not is_court_open(deadline_date, is_quebec):
        deadline_date = add_days(deadline_date, day_step)

    return deadline_date


def deadline_after(event_date: datetime.date, number_of_days: int, is_quebec: bool = False) -> datetime.date:
    return deadline(event_date, number_of_days, after_event=True, is_quebec=is_quebec)


def deadline_before(event_date: datetime.date, number_of_days: int, is_quebec: bool = False) -> datetime.date:
    return deadline(event_date, number_of_days, after_event=False, is_quebec=is_quebec)
