#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

def validate_args(args):
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    operator = args[2]
    if operator not in {'+', '-', '*', '/'}:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

def calculate(a, operator, b):
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    return operations[operator](a, b)

if __name__ == "__main__":
    validate_args(sys.argv)
    
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    
    result = calculate(a, operator, b)
    print(f"{a} {operator} {b} = {result}")
