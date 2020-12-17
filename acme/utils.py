import sys
import logging
from typing import List
from acme.data import constants
from acme.expections import MalformedFileError
from acme.data.constants import WEEKEND, WORKWEEK


def get_day_abbrev(day):

    day_abbrev = day[:2]

    if day_abbrev not in WORKWEEK:
        if day_abbrev not in WEEKEND:
            raise MalformedFileError('Error obtaining day name')

    return day_abbrev


def get_employee_name(text_line):

    employee_name = text_line.split('=')[0]

    return employee_name


def get_day_times(day_worked):

    times_worked = day_worked[2:]

    return times_worked


def get_hours_minutes(hours):

    try:
        start_time, end_time = hours.split('-')
    except ValueError as e:
        raise MalformedFileError('Error obtaining hours and minutes times')

    return start_time, end_time


def get_week_worked(text_line):

    try:
        week_worked = text_line.split('=')[1]
    except IndexError:
        raise MalformedFileError('Error obtaining week worked')

    return week_worked


def to_decimal_hours(time: str) -> float:
    """Pass hours from string format HH:MM to hours decimal"""

    try:
        h, m = time.split(':')
        hours = int(h) + int(m) / 60
    except ValueError:
        print(time)
        raise MalformedFileError('Error parsing hours')

    return hours


def hours_to_string(hours: float) -> str:

    h = int(hours)
    m = int((hours - h) * 60)

    h = str(h)
    m = str(m)

    if h == '0':
        h += '0'

    if m == '0':
        m += '0'

    return f'{h}:{m}'
