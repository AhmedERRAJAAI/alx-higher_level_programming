#!/usr/bin/python3

import sys

def print_arguments():
    arg_count = len(sys.argv) - 1
    
    if arg_count == 0:
        print("0 arguments.")
    else:
        print(f"{arg_count} argument{'s' if arg_count > 1 else ''}:")
        
        for index, arg in enumerate(sys.argv[1:], start=1):
            print(f"{index}: {arg}")

if __name__ == "__main__":
    print_arguments()
