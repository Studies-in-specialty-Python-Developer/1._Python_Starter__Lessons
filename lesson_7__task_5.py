""" Урок 7, завдання 5
Є рядок, в якому зберігаються 1000 слів. Створіть словник із ключами - унікальними словами та
значеннями - кількістю повторів кожного слова у послідовності.
"""

from collections import Counter
from faker import Faker

faker = Faker()
word_list = []
for i in range(1000):
    word_list.append(faker.word())
counter = Counter(word_list)
for item, count in counter.most_common():
    print(f'{item}:\t{count}')
