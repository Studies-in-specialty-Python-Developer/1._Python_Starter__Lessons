""" Урок 4, завдання 3
Використовуючи вкладені цикли та функції print(‘*’, end=’’), print(‘ ‘, end=’’) та print() виведіть на
екран прямокутний трикутник.
"""

size = 5
for i in range(1, size + 1):
    for j in range(1, i + 1):
        if any([j == 1, j == i, i == size]):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
