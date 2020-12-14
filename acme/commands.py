from acme.app import run, demo


def check(argv):
    # Check if some command is completed
    completed = 0
    if len(argv) == 1:
        if argv[0] == '-h' or argv[0] == '--help':
            instructions()
            completed = 1
        elif argv[0] == '-d' or argv[0] == '--demo':
            completed = demo()
        else:
            completed = run(argv[0])
    return completed


def processing(argv):
    # processing the command and check argument
    options = ['-d', '--demo', '-h', '--help']
    is_option = argv[0] in options or argv[0].endswith('.txt')
    completed = 0
    res = ''
    if is_option:
        completed = check(argv)
    elif not argv[0].startswith('-'):
        res += '\nCheck the file is in the same directory'
        res += '\nAlso check the correct file extension (.txt)'
    if not completed:
        res += '\nInvalid argument.'
        res += '\nFor more information run: acme --help'
    print(res)


def instructions():
    # Print the instructions

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
