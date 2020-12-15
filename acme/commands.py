from acme.app import run, demo

SUCCESS = 1
FAIL = 0
ERROR = -1

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


def processing(argv):
    """Processing the command and check argument"""
    
    options = ['-d', '--demo', '-h', '--help']
    is_option = argv[0] in options or argv[0].endswith('.txt')
    
    completed = FAIL

    if is_option:
        completed = check(argv)

    err = {
        FAIL:  'Invalid argument.\nFor more information run: acme --help',
        ERROR: 'An error ocurred',
    }

    if completed != SUCCESS:
        print(err.get(completed))

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
        
        Ensure the file is a text (.txt) file"""

    options = """
    Options:
        -d  : Create a demo file with default name (data.txt) 
              and execute the app (also --demo)
        -h  : Print the instructions (also --help)"""

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
