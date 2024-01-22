""" Урок 4, завдання 1
Дано числа a і b (a < b). Виведіть суму всіх натуральних чисел від a до b (включно).
"""

a = 1
b = 9
summa = 0
for i in range(a, b + 1):
    summa += i
print('a =', a, '\nb =', b, '\nsumma =', summa)
