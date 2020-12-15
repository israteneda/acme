import os
from acme.entities.working_hours import WorkingHours
from acme.entities.employee import Employee
from acme.entities.shift import Shift
from acme.entities.day import Day
from acme.data.shiftwork import shiftwork
from acme.data.rates import rates
from acme.utils import *


def run(file):
    completed = 0
    employees = get_employees(file)
    if employees:
        for employee in employees:
            print(f'The amount to pay {employee.name} is: {truncate(employee.salary, 2)} USD')
        completed = 1

    return completed


def demo():
    completed = 0
    try:
        dirname = os.path.dirname(os.path.realpath(__file__))
        employess_file_path = os.path.join(dirname, "data/employees.txt")
        with open(employess_file_path, "r") as base_file:
            content = base_file.read()
            with open("employess.txt", "w+") as file:
                file.write(content)
        completed = run('employess.txt')
    except FileNotFoundError:
        print('An error occurred in the demo execution')
        completed = -1

    return completed


def get_file_path(relative_path: str) -> str:
    current_dir = os.getcwd()
    new_path: str = os.path.join(current_dir, relative_path)
    
    return new_path


def read_file_lines(path: str) -> str:
    lines: str = ''
    try:
        with open(path) as file:
            for line in file:
                lines += line

    except FileNotFoundError:
        print('File not found.\nBe sure the file exists.')

    return lines


def calculate_day_cost(day: str, hours: str) -> float:

    ONE_MINUTE = 1 / 60

    day = Day(day)
    start_time, end_time = hours.split('-')
    working_hours = WorkingHours(start_time, end_time)

    cost: float = 0
    total_hours: float = working_hours.get_total()

    while True:
        for shift in shiftwork:
            if(working_hours.start_time > 24):
                working_hours.start_time -= 24

            if truncate(working_hours.start_time, 1) >= truncate(shift.start_time, 1) and \
                    truncate(working_hours.end_time, 1) <= truncate(shift.end_time, 1):
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


def get_employees(file):
    path: str = get_file_path(file)
    file_content = read_file_lines(path)
    employees = []
    if file_content:
        lines = file_content.split('\n')
        for line in lines:
            name: str = line.split('=')[0]
            salary: float = calculate_salary(line.split('=')[1])
            employee = Employee(name, salary)
            employees.append(employee)

    return employees
