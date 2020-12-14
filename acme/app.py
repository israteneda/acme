import os
from acme.working_hours import WorkingHours
from pathlib import Path

workweek = ['MO', 'TU', 'WE', 'TH', 'FR']
weekend = ['SA', 'SU']

def run():
    print(show_salary())
    return 1

def demo():
    f = open("data.txt", "w+")
    f.write('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n'
    'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')
    f.close()
    print(show_salary())
    
    return 1


def file_path(relative_path: str) -> str:
    dir: str = os.path.dirname(os.path.abspath(__file__))
    root_dir = Path(dir).parent
    split_path = relative_path.split("/")
    new_path: str = os.path.join(root_dir, *split_path)
    return new_path


def read_file_lines(path: str) -> str:
    with open(path) as file:
        lines: str = ''
        for line in file:
            lines += line
    return lines


def calculate_day_cost(day: str, hours: str) -> float:
    time_worked = hours.split('-')
    seconds_worked = []
    cost: float = 0.00
    for time in time_worked:
        (h, m) = time.split(':')
        seconds_worked.append(int(h) * 3600 + int(m) * 60)

    if day in workweek:
        early_morning = WorkingHours(initial_time=3600, final_time=32459, cost=25.00)
        day = WorkingHours(initial_time=32460, final_time=64859, cost=15.00)
        night = WorkingHours(initial_time=64860, final_time=86400, cost=20.00)
    else: 
        early_morning = WorkingHours(initial_time=3600, final_time=32459, cost=30.00)
        day = WorkingHours(initial_time=32460, final_time=64859, cost=20.00)
        night = WorkingHours(initial_time=64860, final_time=86400, cost=25.00)
        
    
    working_hours = [early_morning, day, night]

    for stage_day in working_hours:
        if seconds_worked[0] >= stage_day.initial_time and seconds_worked[1] <= stage_day.final_time:
            cost = abs(seconds_worked[1] - seconds_worked[0]) / 3600 * stage_day.cost

    return cost


def calculate_salary(time_worked: str) -> float:
    days = time_worked.split(',')
    salary:float = 0.0
    for day in days:
        hours = day[2:]
        day = day[:2]
        salary += calculate_day_cost(day, hours)

    return salary


def show_salary():
    path: str = file_path('data.txt')
    lines = read_file_lines(path).split('\n')
    output: str = '\n'
    for line in lines:
        name: str = line.split('=')[0]
        amount: float = calculate_salary(line.split('=')[1])
        output += f'The amount to pay {name} is: {amount} USD\n'

    return output
