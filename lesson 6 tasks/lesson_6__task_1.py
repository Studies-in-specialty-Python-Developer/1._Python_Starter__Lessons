""" Урок 6, завдання 1
Створіть список та введіть його значення. Знайдіть найбільший та найменший елемент списку,
а також суму та середнє арифметичне його значень.
"""

my_list = []
len_my_list = int(input('Enter the length of the list: '))
for i in range(len_my_list):
    my_list.append(int(input(f'Enter the integer number {i + 1}: ')))
print(f'The list is: {my_list}')
print(f'The largest number is: {max(my_list)}')
print(f'The smallest number is: {min(my_list)}')
print(f'The sum of the list is: {sum(my_list)}')
print(f'The average of the list is: {sum(my_list) / len(my_list)}')
