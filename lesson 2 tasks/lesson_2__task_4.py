""" Урок 2, завдання 4
Напишіть програму, в якій користувач вводить фразу з клавіатури, яка складається з 10
символів. На екрані виведіть суму ASCII-кодів символів введеного рядка.
"""

string_len_10 = ''
while len(string_len_10) != 10:
    string_len_10 = input('Enter a string 10 characters long: ')
ascii_sum = 0
for i in string_len_10:
    ascii_sum += ord(i)
print('string =', string_len_10)
print('ASCII Sum =', ascii_sum)
