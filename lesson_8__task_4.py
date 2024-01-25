""" Урок 8, завдання 4
Створіть програму, яка складається з функції, яка приймає три числа і повертає їх середнє
арифметичне, і головного циклу, що запитує у користувача числа і обчислює їх середні
значення за допомогою створеної функції.
"""


def sum_three_numbers(x, y, z):
    return (x + y + z) / 3


while True:
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    c = float(input('Enter third number: '))
    print(f'The average of {a}, {b}, {c} = {sum_three_numbers(a, b, c)}')
    print('Enter "off" to exit')
    if input() == 'off':
        break
