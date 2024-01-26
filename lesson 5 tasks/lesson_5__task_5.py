""" Урок 5, завдання 5
Напишіть програму, яка вводить з клавіатури послідовність чисел, перетворює послідовність на кортеж і
виводить його відсортованим у порядку зростання.
"""

numbers = tuple(map(int, input('Enter integer numbers separated by space: ').split()))
print(tuple(sorted(numbers)))
