import sys
import math
from typing import List
from acme.data.constants import SUCCESS, MALFORMED_FILE, FAIL


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


def to_decimal_hours(time: str) -> float:
    """Pass hours from string format HH:MM to hours in decimal"""

    try:
        h, m = time.split(':')
        hours = int(h) + int(m) / 60
    except:
        print(MALFORMED_FILE)
        sys.exit()

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
            
def wrong_time_range(start_time, end_time):
    first_time = hours_to_string(start_time)
    second_time = hours_to_string(end_time)
    print(f'{WRONG_RANGE}: {first_time}-{second_time}')
    sys.exit()
