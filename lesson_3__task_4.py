""" Урок 3, завдання 4
Напишіть програму-калькулятор, в якій користувач зможе обрати операцію, ввести необхідні
числа та отримати результат. Операції, які необхідно реалізувати: додавання, віднімання,
множення, ділення, зведення в ступінь, квадратний корінь, кубічний корінь, синус, косинус та
тангенс числа.
"""

from math import sin, cos, tan

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
10. Tan""")
operation = input('Enter operation number: ')
if operation not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
    print('Invalid operation')
    exit()
arg_1 = 0
arg_2 = 0
result = 0
if operation in ('1', '2', '3', '4', '5'):
    arg_1 = float(input('Enter first argument: '))
    arg_2 = float(input('Enter second argument: '))
if operation in ('6', '7', '8', '9', '10'):
    arg_1 = float(input('Enter argument: '))
if operation == '1':
    result = arg_1 + arg_2
elif operation == '2':
    result = arg_1 - arg_2
elif operation == '3':
    result = arg_1 * arg_2
elif operation == '4':
    result = arg_1 / arg_2
elif operation == '5':
    result = arg_1 ** arg_2
elif operation == '6':
    result = arg_1 ** (1 / 2)
elif operation == '7':
    result = arg_1 ** (1 / 3)
elif operation == '8':
    result = sin(arg_1)
elif operation == '9':
    result = cos(arg_1)
elif operation == '10':
    result = tan(arg_1)
print('Result =', result)
