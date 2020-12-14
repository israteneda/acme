import os
from entities import *
from utils import *
from data.shiftwork import shiftwork
from acme.data.rates import rates
from pathlib import Path


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
    start_time: float = to_hours(start_time)
    end_time: float = to_hours(end_time)

    salary: float = 0
    total_hours: float = end_time - start_time

    while total_hours != 0:
        for shift in shiftwork:
            if start_time >= to_hours(shift.start_time) and start_time <= to_hours(shift.end_time):
                if end_time <= to_hours(shift.end_time):
                    total_hours -= end_time - start_time
                    salary += (end_time - start_time) * \
                        rates[shift.name][day.get_week()]
                    # print(total_hours, start_time, end_time, shift.name, day.abbrev, day.get_week(), rates[shift.name][day.get_week()])
                else:
                    total_hours -= to_hours(shift.end_time) + \
                        (1 / 60) - start_time
                    salary += (to_hours(shift.end_time) - start_time) * \
                        rates[shift.name][day.get_week()]
                    start_time = to_hours(shift.end_time) + (1 / 60)

            if total_hours == 0:
                break

    print(salary)


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


calculate_day_cost('MO', '10:00-12:00')
calculate_day_cost('MO', '05:00-11:00')
calculate_day_cost('MO', '06:00-18:00')
