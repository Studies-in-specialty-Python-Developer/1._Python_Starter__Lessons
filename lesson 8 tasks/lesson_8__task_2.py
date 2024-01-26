""" Урок 8, завдання 2
Створіть дві функції, що обчислюють значення певних алгебраїчних виразів. На екрані виведіть
таблицю значень цих функцій від -5 до 5 з кроком 0.5.
"""

import numpy as np


def summ(arg_1, arg_2):
    return arg_1 + arg_2


def product(arg_1, arg_2):
    return arg_1 * arg_2


print('   Function of the sum of two arguments')
y = 1
for x in np.arange(-5, 5.1, 0.5):
    print(f'x = {x}, y = {y},  x + y = {summ(x, y)}')
print()
print('   Function of the product of two arguments')
y = 2
for x in np.arange(-5, 5.1, 0.5):
    print(f'x = {x}, y = {y},  x * y = {product(x, y)}')
