""" Урок 10, завдання 4
Створіть магазин канцтоварів використовуючи списки для зберігання елементів. Для додавання
елементів створіть функцію, яка буде запитувати дані в користувача і зібрані дані у вигляді
кортежу додавати у створений список на початку. Результат вивести на екран. Під час створення
дотримуйтесь правил специфікації PEP 8.
"""


def add_stationery(stationery: list):
    add_new = []
    while True:
        new_item = input('Enter a new stationery (Enter to end): ')
        if new_item == '':
            break
        add_new.append(new_item)
    stationery.extend(tuple(add_new))
    return stationery


stationery_list = []
while True:
    print("""Select operation:
 1. Add new stationery
 2. Print stationery list
 0. Exit
 """)
    operation = input('Enter operation number: ')
    if operation == '1':
        stationery_list = add_stationery(stationery_list)
    elif operation == '2':
        for item in stationery_list:
            print(item)
    elif operation == '0':
        break
    else:
        print()
        print('Wrong operation')
