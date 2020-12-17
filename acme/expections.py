import logging
from acme.data.constants import MALFORMED_FILE, WRONG_TIME_RANGE

class MalformedFileError(Exception):

    def __init__(self, message=MALFORMED_FILE):
        self.message = message
        logging.error(self.message)
        exit(1)
    
class WrongTimeRangeError(Exception):

    def __init__(self, start_time, end_time, message=WRONG_TIME_RANGE):
        first_time = hours_to_string(start_time)
        second_time = hours_to_string(end_time)
        logging.error(f'{constants.WRONG_RANGE}: {first_time}-{second_time}')
        sys.exit(1)