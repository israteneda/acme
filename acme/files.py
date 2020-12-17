import os
from acme.data.constants import FILE_NOT_FOUND, EMPTY_FILE
from acme.utils import get_employee_name, get_week_worked
from acme.domain.employee import Employee
from acme.expections import EmptyFileError


def get_employees_from_file(file):
    path: str = get_file_path(file)
    employees = []
    text_lines = read_file_lines(path)
    for text_line in text_lines:
        employee_name: str = get_employee_name(text_line)
        week_worked: str = get_week_worked(text_line)
        employee = Employee(employee_name)
        employee.calculate_salary(week_worked)
        employees.append(employee)

    return employees


def get_file_path(relative_path: str) -> str:
    current_dir = os.getcwd()
    new_path: str = os.path.join(current_dir, relative_path)

    return new_path


def read_file_lines(path: str) -> str:

    lines = []

    try:
        with open(path) as file:
            lines = file.readlines()

    except FileNotFoundError:
        print(FILE_NOT_FOUND)

    if not lines:
        raise EmptyFileError()

    return lines


def write_employees_data():
    dirname = os.path.dirname(os.path.realpath(__file__))
    employess_file_path = os.path.join(dirname, "data/employees.txt")
    with open(employess_file_path, "r") as base_file:
        content = base_file.read()
        with open("employees.txt", "w+") as file:
            file.write(content)