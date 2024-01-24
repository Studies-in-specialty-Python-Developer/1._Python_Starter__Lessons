""" Урок 6, завдання 3
Простим називається число, яке ділиться націло лише на одиницю і на саме себе. Число 1 не
вважається простим. Напишіть програму, яка знаходить усі прості числа в заданому проміжку,
виводить їх на екран, а потім на вимогу користувача виводить їхню суму або добуток.
Рішення не використовувало рекурсію і не обчислювало всі проміжні кількості варіантів шляхів багато разів
(що вкрай неефективно), а зберігало їх у списку.
"""
from functools import reduce

lower_limit = int(input('Enter the lower limit of the range (natural number > 1): '))
upper_limit = int(input('Enter the upper limit of the range (natural number): '))
# calculate prime numbers that do not exceed the upper limit
prime_numbers_list = []
for i in range(2, upper_limit + 1):
    for pn in prime_numbers_list:
        if i % pn == 0:
            break
    else:
        prime_numbers_list.append(i)
# take prime numbers that are in a given range lower_limit - upper_limit
result = []
for i in prime_numbers_list:
    if i >= lower_limit:
        result = prime_numbers_list[prime_numbers_list.index(i):]
        break
print('The prime numbers in range are: ', result)
operation = input(
    """Enter the operation:
    1 - sum
    2 - product """)
if operation == '1':
    print('The sum of the prime numbers in range is: ', sum(result))
elif operation == '2':
    print('The product of the prime numbers in range is: ', reduce(lambda x, y: x * y, result))
else:
    print('Invalid operation')
