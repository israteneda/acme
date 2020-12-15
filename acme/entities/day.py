class Day:

    WORKWEEK = ['MO', 'TU', 'WE', 'TH', 'FR']

    def __init__(self, abbrev: str):
        self.abbrev = abbrev

    def get_week(self) -> str:
        if self.abbrev in self.WORKWEEK:
            return 'workweek'
        else:
            return 'weekend'
