""" Урок 2, завдання 8
Створіть змінну name, age, в якій зберігатиметься ім'я та вік користувача, введене з клавіатури.
Виведіть у консоль “My name is <name> and I am <age>”, але зробіть рішення таким, щоб
використовувалася конкатенація рядків (через +) та приведення типу числа до рядка (str(...)).
Тобто, щоб якщо замінити змінні name і age, то в методі print() нічого не потрібно було би
змінювати. Наприклад, a = 15, print(“Value =” + str(a)) і буде “Value = 15”.
"""

name = input('Your name: ')
age = int(input('Your age: '))
print('My name is ' + name + ' and I am ' + str(age) + ' years old')