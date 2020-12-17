import sys
import math
import logging
from typing import List
from acme.data import constants
from acme.expections import MalformedFileError


def get_day_abbrev(day):

    try:
        day_abbrev = day[:2]
    except:
        raise MalformedFileError('Error obtaining day name')

    return day_abbrev

def get_datetimes(day):

    try:
        day = day[2:]
    except:
        raise MalformedFileError('Error obtaining datetimes')

    return day


def get_employee_name(text_line):

    try:
        employee_name = text_line.split('=')[0]
    except:
        raise MalformedFileError('Error obtaining employee name')

    return employee_name


def get_week_worked(text_line):

    try:
        week_worked = text_line.split('=')[1]
    except:
        print('week worked')
        raise MalformedFileError
    return week_worked

def get_times(hours):
    
    try:
        start_time, end_time = hours.split('-')
    except ValueError as e:
        raise MalformedFileError('Error obtaining day times')

    return start_time, end_time

def to_decimal_hours(time: str) -> float:
    """Pass hours from string format HH:MM to hours decimal"""

    try:
        h, m = time.split(':')
        hours = int(h) + int(m) / 60
    except:
        logging.error(constants.MALFORMED_FILE)
        sys.exit(1)

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
