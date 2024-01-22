""" Урок 4, завдання 5
Створіть програму, яка малює на екрані прямокутник із зірочок заданою користувачем ширини
та висоти.
"""

width = int(input('Enter width: '))
height = int(input('Enter height: '))
for i in range(height):
    for j in range(width):
        if any([i == 0, i == height - 1, j == 0, j == width - 1]):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
