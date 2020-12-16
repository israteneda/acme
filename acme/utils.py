import sys
import math
from typing import List
from acme.data.constants import *


def get_times(hours):
    try:
        start_time, end_time = hours.split('-')
    except:
        print(MALFORMED_FILE)
        sys.exit()

    return start_time, end_time


def get_hours(day):

    try:
        day = day[2:]
    except:
        print(MALFORMED_FILE)
        sys.exit()

    return day


def get_day_abbrev(day):

    try:
        day_abbrev = day[:2]
    except:
        print(MALFORMED_FILE)
        sys.exit()

    return day_abbrev


def get_days(time_worked: str) -> List[str]:

    try:
        days = time_worked.split(',')
    except:
        print(MALFORMED_FILE)
        sys.exit()

    return days


def get_lines(file_content):

    try:
        lines = file_content.split('\n')
    except:
        print(MALFORMED_FILE)
        sys.exit()

    return lines


def get_employee_name(text_line):

    try:
        employee_name = text_line.split('=')[0]
    except:
        print(MALFORMED_FILE)
        sys.exit()

    return employee_name


def get_week_worked(text_line):

    try:
        week_worked = text_line.split('=')[1]
    except:
        print(MALFORMED_FILE)
        sys.exit()

    return week_worked


def to_hours(time: str) -> float:
    """Pass hours from string format HH:MM to hours in decimal"""

    try:
        h, m = time.split(':')
        hours = int(h) + int(m) / 60
    except:
        print(MALFORMED_FILE)
        sys.exit()

    return hours


def truncate(number, digits) -> float:
    """Truncate decimal number"""

    stepper = 10.0 ** digits

    return math.trunc(stepper * number) / stepper
