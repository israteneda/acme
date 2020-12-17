from acme import utils
from acme.domain.day import Day
from acme.expections import MalformedFileError


class Employee:
    salary = 0

    def __init__(self, name):
        self.name = name

    def calculate_salary(self, week_worked: str) -> float:
        salary: float = 0.0
        datatimes = week_worked.split(',')
        if '' in datatimes:
            print('employee')
            raise MalformedFileError
        else:
            for datatime in datatimes:
                datatimes = utils.get_datetimes(datatime)
                day_abbrev = utils.get_day_abbrev(datatime)
                day = Day(day_abbrev)
                salary += day.calculate_day_cost(datatimes)

        self.salary = salary

        return salary
