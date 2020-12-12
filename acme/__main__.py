from acme.app import run
import sys

def main():
    argv = sys.argv[1:]
    if len(argv) == 1:
        run(argv)
    else:
        print('Wrong command: Please go to the documentation')


if __name__=='__main__':
    main()