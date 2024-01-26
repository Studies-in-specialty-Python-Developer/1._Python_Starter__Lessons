""" Урок 7, завдання 1
Дано два рядки. Виведіть на екран символи, які є в обох рядках.
"""

str1 = 'First string'
str2 = 'Second string'
set1 = set(str1)
set2 = set(str2)
print('Characters in both strings: ', set1.intersection(set2))
