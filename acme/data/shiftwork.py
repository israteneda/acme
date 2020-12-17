from acme.domain.shift import Shift

# Shift start at midnight and ends in the morning
first_shift = Shift(name='first_shift', hours='00:01-09:00')

# Working during the day
second_shift = Shift(name='second_shift', hours='09:01-18:00')

# Runs from afternoon to midnight
third_shift = Shift(name='third_shift', hours='18:01-00:00')

# Shifts of the workday
shiftwork = [first_shift, second_shift, third_shift]
