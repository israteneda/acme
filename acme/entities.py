from acme.utils import *


class Employee:

    def __init__(self, name: str):
        self.name = name


class Day:

    _workweek = ['MO', 'TU', 'WE', 'TH', 'FR']

    def __init__(self, abbrev: str):
        self.abbrev = abbrev

    def get_week(self) -> str:
        if self.abbrev in self._workweek:
            return 'workweek'
        else:
            return 'weekend'


class WorkingHours:

    MAX_HOUR = 24

    def __init__(self, start_time: str, end_time: str):
        self.start_time = start_time
        self.end_time = self._check_max_hour(end_time)
        self._to_hours()

    def _check_max_hour(self, end_time: str) -> str:
        if end_time == '00:00':
            end_time = '24:00'

        return end_time

    def _to_hours(self):
        self.start_time = to_hours(self.start_time)
        self.end_time = to_hours(self.end_time)

    def get_total(self) -> float:
        if self.end_time < self.start_time:
            total_hours = self.MAX_HOUR - self.start_time + self.end_time
        else:
            total_hours = self.end_time - self.start_time

        return total_hours


class Shift(WorkingHours):

    def __init__(self, name: str, start_time: str, end_time: str):
        super().__init__(start_time, end_time)
        self.name = name
