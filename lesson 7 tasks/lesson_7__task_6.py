""" Урок 7, завдання 6
Створіть прототип програми «Бібліотека», де є можливість перегляду та внесення змін за структурою:
автор: твір. Передбачте можливість виведення на екран сортування за автором та твором.
"""

from faker import Faker

# automatic filling of the library
faker = Faker()
library = {}
for i in range(5):
    library[faker.first_name_nonbinary() + ' ' + faker.last_name_nonbinary()] = faker.sentences(1)[0]

# manually filling of the library
# author=input('Enter author: ')
# title=input('Enter title: ')
# library[author]=title

sorted_by_author = sorted(library.items())
sorted_by_title = sorted(library.items(), key=lambda x: x[1])
print('   Sorted by author:')
for item in sorted_by_author:
    print(f'{item[0]} - {item[1]}')
print('   Sorted by title:')
for item in sorted_by_title:
    print(f'{item[0]} - {item[1]}')
