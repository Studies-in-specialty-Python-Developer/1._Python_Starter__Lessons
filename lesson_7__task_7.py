""" Урок 7, завдання 7
Створіть прототип програми «Облік кадрів», в якій є можливість перегляду та внесення змін до
структури(реалізуйте інтерфейс(меню), за допомогою якого можна робити маніпуляції з даними):
прізвище:
посада: ...
досвід роботи: …
портфоліо: …
коефіцієнт ефективності: …
стек технологій: …
зарплата: …
Передбачте можливість виведення на екран сортування за прізвищем та найефективнішим
співробітником.
"""

from collections import namedtuple
from random import randint
from faker import Faker

faker = Faker()
Employee = namedtuple('Employee', 'full_name job_title experience portfolio efficiency technologies salary')
personal = {}
for i in range(5):
    personnel_number = i + 1
    personal[personnel_number] = Employee(faker.first_name_nonbinary() + ' ' + faker.last_name_nonbinary(),
                                          faker.job(),
                                          randint(0, 30),
                                          [],
                                          randint(1, 10) / 10,
                                          [faker.word(), faker.word(), faker.word()],
                                          '$' + str(randint(10000, 100000)))

for key, value in personal.items():
    print(f'{key}: {value}')
while True:
    operation = input(
        """Enter the operation:
        1 - print employee details
        2 - delete employee data
        3 - print the details of all employees by personnel number
        4 - print the details of all employees by full name
        5 - print the details of all employees by efficiency
        6 - exit 
        """)
    if operation == '1':  # print employee details
        pn = int(input('Enter personnel number: '))
        if personal.get(pn):
            print(personal[pn])
        else:
            print('No such personnel number')
    elif operation == '2':  # delete employee data
        pn = int(input('Enter personnel number: '))
        if personal.get(pn):
            print(f'Employee {personal.pop(pn).full_name} deleted')
        else:
            print('No such personnel number')
    elif operation == '3':  # print the details of all employees by personnel number
        for key, value in sorted(personal.items()):
            print(f'{key}: {value}')
    elif operation == '4':  # print the details of all employees by full name
        for key, value in sorted(personal.items(), key=lambda x: x[1].full_name):
            print(f'{key}: {value}')
    elif operation == '5':  # print the details of all employees by efficiency
        for key, value in sorted(personal.items(), key=lambda x: x[1].efficiency, reverse=True):
            print(f'{key}: {value}')
    elif operation == '6':
        exit(0)
    else:
        print('Invalid operation')
