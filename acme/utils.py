import math
from typing import List


def get_times(hours):

    start_time, end_time = hours.split('-')

    # print(start_time, end_time)

    return start_time, end_time


def get_hours(day):

    day = day[2:]

    return day


def get_day_abbrev(day):

    day_abbrev = day[:2]

    return day_abbrev


def get_days(time_worked: str) -> List[str]:

    days = time_worked.split(',')

    return days


def get_lines(file_content):

    lines = file_content.split('\n')

    return lines


def get_employee_name(text_line):

    employee_name = text_line.split('=')[0]

    return employee_name


def get_week_worked(text_line):

    week_worked = text_line.split('=')[1]

    return week_worked


def to_hours(time: str) -> float:
    """Pass hours from string format HH:MM to hours in decimal"""

    h, m = time.split(':')
    hours = int(h) + int(m) / 60

    return hours


def truncate(number, digits) -> float:
    """Truncate decimal number"""

    stepper = 10.0 ** digits

    return math.trunc(stepper * number) / stepper
