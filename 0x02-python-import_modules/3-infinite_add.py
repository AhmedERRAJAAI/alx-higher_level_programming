#!/usr/bin/python3

import sys

def sum_arguments(args):
    try:
        return sum(int(arg) for arg in args[1:])
    except ValueError:
        print("Error: All arguments must be integers.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    result = sum_arguments(sys.argv)
    print(result)
