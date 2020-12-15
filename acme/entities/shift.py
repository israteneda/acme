from acme.entities.working_hours import WorkingHours


class Shift(WorkingHours):

    def __init__(self, name: str, start_time: str, end_time: str):
        super().__init__(start_time, end_time)
        self.name = name
