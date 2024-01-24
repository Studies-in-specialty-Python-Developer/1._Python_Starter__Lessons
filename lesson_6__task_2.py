""" Урок 6, завдання 2
Є два списки, які наповнюються користувачем з клавіатури. Сформувати список, в якому будуть міститися унікальні
значення першого відносно другого списку та навпаки без повторень. Роздрукувати підсумковий об'єкт на екран в прямій
послідовності, зворотній, а також виконати сортування за зростанням та спаданням.
"""

first_list = list(map(int, input('Enter the elements of the first list separated by space: ').split()))
second_list = list(map(int, input('Enter the elements of the second list separated by space: ').split()))
first_second_unique = []
for _ in first_list:
    if not any([_ in second_list, _ in first_second_unique]):
        first_second_unique.append(_)
second_first_unique = []
for _ in second_list:
    if not any([_ in first_list, _ in second_first_unique]):
        second_first_unique.append(_)
summary_unique = first_second_unique + second_first_unique
print('First-second unique:', first_second_unique)
print('Second-first unique:', second_first_unique)
print('Summary unique:', summary_unique)
print('Reversed:')
print(list(reversed(first_second_unique)))
print(list(reversed(second_first_unique)))
print(list(reversed(summary_unique)))
print('Sorted in ascending order:')
print(sorted(first_second_unique))
print(sorted(second_first_unique))
print(sorted(summary_unique))
print('Sorted in descending order:')
print(sorted(first_second_unique, reverse=True))
print(sorted(second_first_unique, reverse=True))
print(sorted(summary_unique, reverse=True))
