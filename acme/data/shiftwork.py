from acme.entities.shift import Shift

# Working during the day
first_shift = Shift(name='first_shift', hours='09:01-18:00')

# Runs from afternoon to midnight
second_shift = Shift(name='second_shift', hours='18:01-00:00')

# Shift start at midnight and ends in the morning
third_shift = Shift(name='third_shift', hours='00:01-09:00')

# Shifts of the workday
shiftwork = [first_shift, second_shift, third_shift]
