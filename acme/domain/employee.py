from acme import utils
from acme.domain.day import Day


class Employee:
    salary = 0

    def __init__(self, name):
        self.name = name

    def calculate_salary(self, week_worked: str) -> float:
        datatimes = utils.get_datatimes(week_worked)
        salary: float = 0.0
        for datatime in datatimes:
            hours = utils.get_hours(datatime)
            day_abbrev = utils.get_day_abbrev(datatime)
            day = Day(day_abbrev)
            salary += day.calculate_day_cost(hours)

        self.salary = salary

        return salary
