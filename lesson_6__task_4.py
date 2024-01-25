""" Урок 6, завдання 4
Створіть список, введіть кількість його елементів і самі значення. Передбачити меню, в якому:
після натискання клавіші 1 ці значення виведуться на екран у зворотному порядку, а після
натискання клавіші 2 – за зростанням.
"""

my_list = []
len_my_list = int(input('Enter the length of the list: '))
for i in range(len_my_list):
    my_list.append(int(input(f'Enter the integer number {i + 1}: ')))
print('The list is: ', my_list)
operation = input(
    """Enter the operation:
    1 - print list in reverse order
    2 - print list in ascending order """)
if operation == '1':
    print('In reverse order: ', list(reversed(my_list)))
elif operation == '2':
    print('In ascending order: ', sorted(my_list))
else:
    print('Wrong operation')
