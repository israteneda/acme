from acme.data.constants import *
from acme.domain.working_hours import WorkingHours
from acme.data.shiftwork import shiftwork
from acme.data.rates import rates
from acme.utils import *
from acme.data.constants import *


class Day:

    def __init__(self, day_abbrev: str):
        self.day_abbrev = day_abbrev
        self._week = self._get_week()

    def _get_week(self) -> str:
        week = 'workweek'

        if self.day_abbrev in WEEKEND:
            week = 'weekend'

        return week

    def calculate_day_cost(self, hours: str) -> float:

        working_hours = WorkingHours(hours)
        cost: float = 0
        total_hours: float = working_hours.get_total()
        accumulated_hours: float = 0
        plus_one = False

        for index, shift in enumerate(shiftwork):

            rate = rates[shift.name][self._week]

            if working_hours.start_time_is_between(shift):

                if working_hours.end_time <= shift.end_time:
                    accumulated_hours = working_hours.end_time - working_hours.start_time
                    cost += accumulated_hours * rate
                    if plus_one:
                        cost += ONE_MINUTE * rate
                        plus_one = False

                else:
                    accumulated_hours = shift.end_time - working_hours.start_time
                    cost += accumulated_hours * rate
                    working_hours.start_time = shift.end_time + ONE_MINUTE
                    plus_one = True

        return cost
