import os
from acme.data.constants import *
from acme.utils import *
from acme.domain.employee import Employee


def get_employees_from_file(file):
    path: str = get_file_path(file)
    file_content = read_file_lines(path)
    employees = []
    if file_content:
        text_lines = get_lines(file_content)
        for text_line in text_lines:
            employee_name: str = get_employee_name(text_line)
            week_worked = get_week_worked(text_line)
            employee = Employee(employee_name)
            employee.calculate_salary(week_worked)
            employees.append(employee)

    return employees


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
        print(FILE_NOT_FOUND)

    return lines


def write_employees_data():
    try:
        dirname = os.path.dirname(os.path.realpath(__file__))
        employess_file_path = os.path.join(dirname, "data/employees.txt")
        with open(employess_file_path, "r") as base_file:
            content = base_file.read()
            with open("employess.txt", "w+") as file:
                file.write(content)
    except FileNotFoundError:
        print('Demo data not found')
        completed = -1
