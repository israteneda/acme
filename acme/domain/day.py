from acme.data.constants import WEEKEND, ONE_MINUTE
from acme.domain.working_hours import WorkingHours
from acme.data.shiftwork import shiftwork
from acme.data.rates import rates


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
        worked_hours: float = 0
        plus_one = False

        for shift in shiftwork:

            rate = rates[shift.name][self._week]

            if working_hours.start_time_is_between(shift):

                if working_hours.end_time <= shift.end_time:
                    worked_hours = working_hours.end_time - working_hours.start_time
                    cost += worked_hours * rate
                    if plus_one:
                        cost += ONE_MINUTE * rate
                        plus_one = False

                else:
                    worked_hours = shift.end_time - working_hours.start_time
                    cost += worked_hours * rate
                    working_hours.start_time = shift.end_time + ONE_MINUTE
                    plus_one = True

        return cost
