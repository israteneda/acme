from acme.utils import *
from acme.data.constants import *


class WorkingHours:

    def __init__(self, hours: str):
        self.start_time, self.end_time = get_times(hours)
        self._to_hours()

    def _to_hours(self):
        self.start_time = to_decimal_hours(self.start_time)
        self.end_time = to_decimal_hours(self.end_time)
        self._check_hours()

    def _check_hours(self):
        if self.start_time == 0:
            wrong_time_range(self.start_time, self.end_time)

        if self.end_time == 0:
            self.end_time = 24.0

        if self.start_time > MAX_HOUR or self.end_time > MAX_HOUR:
            wrong_time_range(self.start_time, self.end_time)

        if self.start_time > self.end_time:
            if self.end_time > MIN_HOUR:
                wrong_time_range(self.start_time, self.end_time)

    def start_time_is_between(self, shift):
        ans = False

        if self.start_time >= shift.start_time:
            if self.start_time <= shift.end_time:
                ans = True

        return ans
