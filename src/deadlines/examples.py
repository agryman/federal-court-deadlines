"""This module defines the examples given in the Guideline document."""

import datetime
from dataclasses import dataclass

@dataclass
class Example:
    description: str
    event_date: datetime.date
    number_of_days: int
    after_event: bool
    deadline_date: datetime.date


general_example_1: Example = Example(
    description="General Example 1 - 10 Days",
    event_date=datetime.date(2012, 5, 31),
    number_of_days=10,
    after_event=True,
    deadline_date=datetime.date(2012, 6, 11),
)

general_example_2: Example = Example(
    description="General Example 2 - 20 Days",
    event_date=datetime.date(2012, 5, 1),
    number_of_days=20,
    after_event=True,
    deadline_date=datetime.date(2012, 5, 22),
)

general_example_3: Example = Example(
    description="General Example 3 - 30 Days",
    event_date=datetime.date(2012, 5, 4),
    number_of_days=30,
    after_event=True,
    deadline_date=datetime.date(2012, 6, 4),
)

holidays_weekends_example_1: Example = Example(
    description="Holidays and Weekends Example 1 - 30 Days",
    event_date=datetime.date(2012, 5, 4),
    number_of_days=30,
    after_event=True,
    deadline_date=datetime.date(2012, 6, 4),
)

holidays_weekends_example_2: Example = Example(
    description="Holidays and Weekends Example 2 - 4 Days",
    event_date=datetime.date(2012, 4, 3),
    number_of_days=4,
    after_event=True,
    deadline_date=datetime.date(2012, 4, 11),
)

summer_recess_example_1:  Example = Example(
    description="Summer Recess Example 1 - 30 Days",
    event_date=datetime.date(2012, 6, 11),
    number_of_days=30,
    after_event=True,
    deadline_date=datetime.date(2012, 9, 11),
)

seasonal_recess_example_1: Example = Example(
    description="Seasonal Recess Example 1 - 30 Days",
    event_date=datetime.date(2012, 12, 14),
    number_of_days=30,
    after_event=True,
    deadline_date=datetime.date(2013, 1, 31),
)

seasonal_recess_example_2: Example = Example(
    description="Seasonal Recess Example 2 - 10 Days",
    event_date=datetime.date(2012, 12, 14),
    number_of_days=10,
    after_event=True,
    deadline_date=datetime.date(2013, 1, 11),
)

seasonal_recess_example_3: Example = Example(
    description="Seasonal Recess Example 3 - 4 Days",
    event_date=datetime.date(2021, 12, 16),
    number_of_days=4,
    after_event=True,
    deadline_date=datetime.date(2022, 1, 11),
)
