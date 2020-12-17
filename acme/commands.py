from acme.data.constants import SUCCESS, FAIL
from acme.files import get_employees_from_file, write_employees_data


def processing(argv):
    """Processing the command and check argument"""

    options = ['-d', '--demo', '-h', '--help']
    is_option = argv[0] in options or argv[0].endswith('.txt')

    completed = FAIL

    if is_option:
        completed = check(argv)

    err = {
        FAIL:  'Invalid argument.\nFor more information run: acme --help'
    }

    if completed != SUCCESS:
        print(err.get(completed))


def check(argv):
    """Check if some command is completed"""

    completed = 0

    if len(argv) == 1:
        if argv[0] == '-h' or argv[0] == '--help':
            instructions()
            completed = SUCCESS
        elif argv[0] == '-d' or argv[0] == '--demo':
            completed = demo()
        else:
            completed = run(argv[0])

    return completed


def run(file):
    completed = 0
    employees = get_employees_from_file(file)
    if employees:
        for employee in employees:
            print('The amount to pay {} is: {:.2f} USD'.format(
                employee.name, employee.salary)
            )
        completed = 1

    return completed


def demo():
    completed = 0
    write_employees_data()
    completed = run('employess.txt')

    return completed


def instructions():
    """Print the instructions"""

    info = r"""
      ______    ______   __       __  ________
     /      \  /      \ |  \     /  \|        \
    |  $$$$$$\|  $$$$$$\| $$\   /  $$| $$$$$$$$
    | $$__| $$| $$   \$$| $$$\ /  $$$| $$__
    | $$    $$| $$      | $$$$\  $$$$| $$  \
    | $$$$$$$$| $$   __ | $$\$$ $$ $$| $$$$$
    | $$  | $$| $$__/  \| $$ \$$$| $$| $$_____
    | $$  | $$ \$$    $$| $$  \$ | $$| $$     \
     \$$   \$$  \$$$$$$  \$$      \$$ \$$$$$$$$"""
    usage = """
    Usage:
        acme <file>
        
        Ensure the file is a text (.txt) file.
        In addition, that the file is in the same
        directory where the command is executed."""

    options = """
    Options:
        -d, --demo  : Create a demo file (employees.txt) 
                      and execute acme employees.txt.
        -h, --help  : Print the instructions."""

    examples = """
    Examples:
        acme data.txt
        acme --demo
        acme -h"""

    help = (
        f'{info}\n'
        f'{usage}\n'
        f'{options}\n'
        f'{examples}'
    )

    print(help)
