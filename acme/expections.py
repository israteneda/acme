import logging
from acme.data.constants import MALFORMED_FILE, WRONG_TIME_RANGE
from acme.utils import hours_to_string

class MalformedFileError(Exception):

    def __init__(self, message):
        self.message = message
        logging.error(self.message)
        logging.error(MALFORMED_FILE)
        exit(1)
    
class WrongTimeRangeError(Exception):

    def __init__(self, start_time, end_time):
        first_time = hours_to_string(start_time)
        second_time = hours_to_string(end_time)
        logging.error(f'{constants.WRONG_TIME_RANGE}: {first_time}-{second_time}')
        sys.exit(1)