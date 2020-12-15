import math


def to_hours(time: str) -> float:
    """Pass hours from string format HH:MM to hours in decimal"""

    h, m = time.split(':')
    hours = int(h) + int(m) / 60

    return hours


def truncate(number, digits) -> float:
    """Truncate decimal number"""

    stepper = 10.0 ** digits

    return math.trunc(stepper * number) / stepper
