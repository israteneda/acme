import os
from acme.entities import *
from acme.utils import *
from acme.data.shiftwork import shiftwork
from acme.data.rates import rates
from pathlib import Path

ONE_MINUTE = 1 / 60


def run(param):
    print(show_salary(param))
    return 1


def demo():
    f = open("data.txt", "w+")
    f.write('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n'
            'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')
    f.close()
    print(show_salary('data.txt'))

    return 1


def file_path(relative_path: str) -> str:
    dir: str = os.path.dirname(os.path.abspath(__file__))
    root_dir = Path(dir).parent
    split_path = relative_path.split("/")
    new_path: str = os.path.join(root_dir, *split_path)
    return new_path


def read_file_lines(path: str) -> str:
    with open(path) as file:
        lines: str = ''
        for line in file:
            lines += line
    return lines


def calculate_day_cost(day: str, hours: str) -> float:
    day = Day(day)
    start_time, end_time = hours.split('-')
    working_hours = WorkingHours(start_time, end_time)

    cost: float = 0
    total_hours: float = working_hours.get_total()

    while True:
        for shift in shiftwork:
            if(working_hours.start_time > 24):
                working_hours.start_time -= 24
            if(working_hours.end_time > 24):
                working_hours.end_time -= 24

            if truncate(working_hours.start_time, 1) >= truncate(shift.start_time, 1) and truncate(working_hours.end_time, 1) <= truncate(shift.end_time, 1):
                if working_hours.start_time <= working_hours.end_time:
                    cost += working_hours.get_total() * \
                        rates[shift.name][day.get_week()]
                    working_hours.start_time = working_hours.end_time
                else:
                    cost += (shift.end_time - working_hours.start_time +
                             ONE_MINUTE) * rates[shift.name][day.get_week()]
                    working_hours.start_time = shift.end_time + ONE_MINUTE

            if truncate(working_hours.start_time, 1) >= truncate(shift.start_time, 1) and \
                    truncate(working_hours.start_time, 1) <= truncate(shift.end_time, 1) and \
                    truncate(working_hours.end_time, 1) > truncate(shift.end_time, 1):
                cost += (shift.end_time - working_hours.start_time) * \
                    rates[shift.name][day.get_week()]
                working_hours.start_time = shift.end_time

            if working_hours.get_total() == 0:
                break

        if working_hours.get_total() == 0:
            break

    return cost


def calculate_salary(time_worked: str) -> float:
    days = time_worked.split(',')
    salary: float = 0.0
    for day in days:
        hours = day[2:]
        day = day[:2]
        salary += calculate_day_cost(day, hours)

    return salary


def show_salary(file):
    path: str = file_path(file)
    lines = read_file_lines(path).split('\n')
    output: str = '\n'
    for line in lines:
        name: str = line.split('=')[0]
        amount: float = calculate_salary(line.split('=')[1])
        output += f'The amount to pay {name} is: {amount} USD\n'

    return output


calculate_day_cost('MO', '20:00-21:00')
