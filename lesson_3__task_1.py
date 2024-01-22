""" Урок 3, завдання 1
Напишіть програму, яка запитує у користувача його ім'я, якщо воно збігається з вашим, видає
певне повідомлення.
"""

MY_NAME = 'Ivan'
name = input('Enter your name: ')
if name == MY_NAME:
    print('Hello, my namesake!')
else:
    print('Hello, my friend!')
