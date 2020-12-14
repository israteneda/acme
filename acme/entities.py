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

    def __init__(self, start_time: str, end_time: str):
        self.start_time = start_time
        self.end_time = end_time


class Shift(WorkingHours):

    def __init__(self, name: str, start_time: str, end_time: str):
        super().__init__(start_time, end_time)
        self.name = name
