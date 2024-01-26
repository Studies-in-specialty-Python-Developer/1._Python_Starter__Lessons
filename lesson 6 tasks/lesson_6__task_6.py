""" Урок 6, завдання 6
Для цього завдання вихідний список значень беремо з підсумкового списку new_list
завдання 5. Користувач вводить з клавіатури значення; якщо таке є у списку — вивести кількість
його повторів та його позицію у цьому списку.
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
print('new_list:', new_list)
value = int(input('Enter the value: '))
count = new_list.count(value)
if count == 0:
    print('The value is not in the new_list')
else:
    print(f'The value {value} occurs {count} times in the new_list at positions:')
    pos = 0
    for i in range(count):
        pos = new_list.index(value, pos)
        print(pos, end=' ')
        pos += 1
