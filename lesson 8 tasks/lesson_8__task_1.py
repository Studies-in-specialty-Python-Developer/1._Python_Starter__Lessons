""" Урок 8, завдання 1
Створіть функцію, яка відображає привітання для користувача із заданим ім'ям. Якщо ім'я не
вказано, вона повинна виводити привітання для користувача з Вашим ім'ям.
"""


def greeting(name='Ivan'):
    print(f'Hello, {name}!')


greeting('Petro')
greeting()