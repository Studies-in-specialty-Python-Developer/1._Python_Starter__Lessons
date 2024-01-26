""" Урок 7, завдання 3
Створіть програму, яка має 2 списки цілочисельних значень та друкує список унікальних значень без
повтору, які є в 1 списку (немає в другому) і навпаки.
"""

from random import randint

list1 = []
list2 = []
for i in range(5):
    list1.append(randint(0, 10))
    list2.append(randint(0, 10))
set1 = set(list1)
set2 = set(list2)
print('list1: ', list1)
print('list2: ', list2)
print('list1 - list2: ', set1.difference(set2))
print('list2 - list1: ', set2.difference(set1))
