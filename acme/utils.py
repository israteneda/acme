import math

def to_seconds(time: str) -> int:
    
    h, m = time.split(':')
    seconds = int(h) * 3600 + int(m) * 60

    return seconds

def to_hours(time: int) -> float:

    h, m = time.split(':')
    hours = int(h) + int(m) / 60

    return hours

def hours_to_string(hours: float) -> str:

    h = int(hours)
    m = hours - h * 60

    return f'{h}:{m}'

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper