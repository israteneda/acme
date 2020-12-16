import os

from acme.data.constants import *
from acme.files import *
from acme.utils import *


def run(file):
    completed = 0
    employees = get_employees(file)
    if employees:
        for employee in employees:
            print(
                f'The amount to pay {employee.name} is: {truncate(employee.salary, 2)} USD')
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
        print('Problems running demo')
        completed = -1

    return completed
