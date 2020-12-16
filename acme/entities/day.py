from acme.data.constants import *
from acme.entities.working_hours import WorkingHours
from acme.data.shiftwork import shiftwork
from acme.data.rates import rates
from acme.utils import *


class Day:
    WORKWEEK = ['MO', 'TU', 'WE', 'TH', 'FR']

    def __init__(self, day_abbrev: str):
        self.day_abbrev = day_abbrev
        self._week = self._get_week()

    def _get_week(self) -> str:
        if self.day_abbrev in self.WORKWEEK:
            week = 'workweek'
        else:
            week = 'weekend'
        return week

    def calculate_day_cost(self, hours: str) -> float:

        working_hours = WorkingHours(hours)
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
                            rates[shift.name][self._week]
                        working_hours.start_time = working_hours.end_time
                    else:
                        cost += (shift.end_time - working_hours.start_time +
                                 ONE_MINUTE) * rates[shift.name][self._week]
                        working_hours.start_time = shift.end_time + ONE_MINUTE

                if truncate(working_hours.start_time, 1) >= truncate(shift.start_time, 1) and \
                        truncate(working_hours.start_time, 1) <= truncate(shift.end_time, 1) and \
                        truncate(working_hours.end_time, 1) > truncate(shift.end_time, 1):
                    cost += (shift.end_time - working_hours.start_time) * \
                        rates[shift.name][self._week]
                    working_hours.start_time = shift.end_time

                if working_hours.get_total() == 0:
                    break

            if working_hours.get_total() == 0:
                break

        return cost
