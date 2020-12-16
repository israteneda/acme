from acme.domain.working_hours import WorkingHours


class Shift(WorkingHours):

    def __init__(self, name: str, hours: str):
        super().__init__(hours)
        self.name = name
