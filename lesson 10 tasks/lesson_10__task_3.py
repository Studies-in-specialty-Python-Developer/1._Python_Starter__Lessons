""" Урок 10, завдання 3
Створіть інженерний калькулятор з використанням модуля math, в якому передбачене меню. Під
час створення дотримуйтесь правил специфікації PEP 8.
"""
import math
from math import sin, cos, tan, log, factorial


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y:
        return x / y
    else:
        return 'Error: Division by zero'


def power(x, y):
    return math.pow(x, y)


def sqrt(x):
    return x ** (1 / 2)


def cube_root(x):
    return x ** (1 / 3)


def get_sin(x):
    return sin(x)


def get_cos(x):
    return cos(x)


def get_tan(x):
    return tan(x)


def get_log(x):
    return log(x)


def get_factorial(x):
    return factorial(x)


while True:
    print("""Select operation:
 1. Add
 2. Subtract
 3. Multiply
 4. Divide
 5. Power
 6. Sqrt
 7. Cube root
 8. Sin
 9. Cos
10. Tan
11. Log
12. Factorial
 0. Exit
 """)
    operation = input('Enter operation number: ')
    arg_x = arg_y = result = None
    if operation in ('1', '2', '3', '4', '5'):
        arg_x = float(input('Enter x: '))
        arg_y = float(input('Enter y: '))
    if operation in ('6', '7', '8', '9', '10', '11', '12'):
        arg_x = float(input('Enter argument: '))
    if operation == '1':
        result = add(arg_x, arg_y)
    elif operation == '2':
        result = subtract(arg_x, arg_y)
    elif operation == '3':
        result = multiply(arg_x, arg_y)
    elif operation == '4':
        result = divide(arg_x, arg_y)
    elif operation == '5':
        result = power(arg_x, arg_y)
    elif operation == '6':
        result = sqrt(arg_x)
    elif operation == '7':
        result = cube_root(arg_x)
    elif operation == '8':
        result = get_sin(arg_x)
    elif operation == '9':
        result = get_cos(arg_x)
    elif operation == '10':
        result = get_tan(arg_x)
    elif operation == '11':
        result = get_log(arg_x)
    elif operation == '12':
        result = get_factorial(round(arg_x))
    elif operation == '0':
        break
    else:
        print()
        print('Wrong operation')
    if result:
        print('Result =', result)
    print()
