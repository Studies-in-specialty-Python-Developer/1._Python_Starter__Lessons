""" Урок 6, завдання 5
Створіть список натуральних чисел int_list. Кожне непарне значення списку додайте до нового
списку new_list. Користувач вводить з клавіатури кількість повторів списку repeat. Здійсніть
дублювання списку new_list, repeat кількість разів. Очистіть список int_list.
"""

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for i in int_list:
    if i % 2 != 0:
        new_list.append(i)
print('int_list:', int_list)
print('new_list:', new_list)
repeat = int(input('Enter the number of repeats the list of odd numbers: '))
new_list = new_list * repeat
int_list.clear()
print('int_list:', int_list)
print('new_list:', new_list)
