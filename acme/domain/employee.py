from acme import utils
from acme.domain.day import Day
from acme.expections import MalformedFileError


class Employee:
    salary = 0

    def __init__(self, name):
        self.name = name

    def calculate_salary(self, week_worked: str) -> float:
        salary: float = 0.0
        datetimes = week_worked.split(',')
        if '' in datetimes:
            raise MalformedFileError('Error obtaining datetimes')
        else:
            for datetime in datetimes:
                day_times = utils.get_day_times(datetime)
                day_abbrev = utils.get_day_abbrev(datetime)
                day = Day(day_abbrev)
                salary += day.calculate_day_cost(day_times)

        self.salary = salary

        return salary
