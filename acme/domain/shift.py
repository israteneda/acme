from acme.domain.working_hours import WorkingHours


class Shift(WorkingHours):
    """
    Shift work refers to a work schedule that is performed 
    in rotations. For example, while some employees might 
    fill a role during the day, others might work night 
    or early morning shifts. This means the company 
    operates for 24 hours each day.
    """

    def __init__(self, name: str, hours: str):
        super().__init__(hours)
        self.name = name
