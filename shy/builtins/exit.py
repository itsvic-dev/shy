import sys


def builtin_exit(exit_code=0):
    exit_code = int(exit_code)

    sys.exit(exit_code)
