""" Урок 4, завдання 4
Дано числа a і b (a < b). Виведіть на екран суму всіх натуральних чисел від a до b (включно), які
є кратними середньому арифметичному цього проміжку.
"""

a = 1
b = 9
average = sum(range(a, b + 1)) / (b - a + 1)
summa = 0
for i in range(a, b + 1):
    if i % average == 0:
        summa += i
print('a =', a, '\nb =', b, '\naverage =', average, '\nsumma =', summa)
