from acme.entities import Shift

# Working during the day
first_shift = Shift(name='first_shift', start_time='09:01', end_time='18:00')

# Runs from afternoon to midnight
second_shift = Shift(name='second_shift', start_time='18:01', end_time='00:00')

# Shift start at midnight and ends in the morning
third_shift = Shift(name='third_shift', start_time='00:01', end_time='09:00')

# Shifts of the workday
shiftwork = [first_shift, second_shift, third_shift]