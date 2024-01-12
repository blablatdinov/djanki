import datetime
from typing import Tuple

import pendulum


def get_last_day_of_current_month() -> pendulum:
    """Получить последнюю дату текущего месяца."""
    now = pendulum.now()
    if now.month == 12:
        next_month_date = pendulum.datetime(now.year + 1, 1, 1)
        return next_month_date.subtract(days=1)
    next_month_date = pendulum.datetime(now.year, now.month + 1, 1)
    return next_month_date.subtract(days=1)


def get_first_day_of_current_month() -> pendulum:
    """Получить первую дату текущего месяца."""
    return pendulum.now().replace(day=1)


def get_first_and_last_dates_of_current_month() -> Tuple[datetime.datetime]:
    """Получить кортеж, состоящий из первого и последнего дня текущего месяца."""
    return (
        get_first_day_of_current_month(),
        get_last_day_of_current_month(),
    )
