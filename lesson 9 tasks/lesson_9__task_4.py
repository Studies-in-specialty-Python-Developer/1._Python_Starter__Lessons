""" Урок 9, завдання 4
Напишіть рекурсивну функцію, яка обчислює суму натуральних чисел, які входять до заданого
проміжку.
"""


def nat_numbers_sum(start, end):
    if start == end:
        return start
    else:
        return start + nat_numbers_sum(start + 1, end)


print(nat_numbers_sum(1, 5))
print(nat_numbers_sum(10, 15))
