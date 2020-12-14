from acme.commands import processing, instructions
import sys


def main():
    argv = sys.argv[1:]
    if len(argv) >= 1:
        processing(argv)
    else:
        instructions()


if __name__ == '__main__':
    main()
