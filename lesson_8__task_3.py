""" Урок 8, завдання 3
Створіть програму-калькулятор, яка підтримує наступні операції: додавання, віднімання,
множення, ділення, зведення в ступінь, зведення до квадратного та кубічного коренів. Всі дані
повинні вводитися в циклі, доки користувач не вкаже, що хоче завершити виконання програми.
Кожна операція має бути реалізована у вигляді окремої функції. Функція ділення повинна
перевіряти дані на коректність та видавати повідомлення про помилку у разі спроби поділу на
нуль.
"""


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
    return x ** y


def sqrt(x):
    return x ** (1 / 2)


def cube_root(x):
    return x ** (1 / 3)


while True:
    print("""Select operation:
 1. Add
 2. Subtract
 3. Multiply
 4. Divide
 5. Power
 6. Sqrt
 7. Cube root
 0. Exit
 """)
    operation = input('Enter operation number: ')
    if operation not in ('1', '2', '3', '4', '5', '6', '7', '0'):
        print('Wrong operation')
        continue
    arg_x = 0
    arg_y = 0
    result = 0
    if operation in ('1', '2', '3', '4', '5'):
        arg_x = float(input('Enter x: '))
        arg_y = float(input('Enter y: '))
    if operation in ('6', '7'):
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
    elif operation == '0':
        break
    print('Result =', result)
    print()
