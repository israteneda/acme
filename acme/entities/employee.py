from acme.utils import *
from acme.entities.day import Day

class Employee:
    salary = 0

    def __init__(self, name):
        self.name = name

    def calculate_salary(self, week_worked: str) -> float:
        days = get_days(week_worked)
        salary: float = 0.0
        for day in days:
            hours = get_hours(day)
            day_abbrev = get_day_abbrev(day)
            day = Day(day_abbrev)
            salary += day.calculate_day_cost(hours)
        self.salary = salary