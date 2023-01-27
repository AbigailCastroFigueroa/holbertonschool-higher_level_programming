#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    length = len(sys.argv) - 1
    if length == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if operator == '+':
            print("{} + {} = {}".format(a, b, calc.add(a, b)))
        elif operator == '-':
            print("{} - {} = {}".format(a, b, calc.sub(a, b)))
        elif operator == '*':
            print("{} * {} = {}".format(a, b, calc.mul(a, b)))
        elif operator == '/':
            print("{} / {} = {}".format(a, b, calc.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
