""" Урок 3, завдання 6
Написати програму визначення днів тижня. Дані про день тижня вводяться користувачем з
клавіатури. Якщо будній день - виводити на екран повідомлення "Сьогодні на роботу", у вихідні
дні - "Сьогодні вихідний", в інших випадках - "Такого дня не існує".
"""

print("""Select day number:
1. Monday
2. Tuesday
3. Wednesday
4. Thursday
5. Friday
6. Saturday
7. Sunday""")
day_number = input('Enter day number: ')
if day_number in ('1', '2', '3', '4', '5'):
    print('Going to work today')
if day_number in ('6', '7'):
    print('Today is weekend')
if day_number not in ('1', '2', '3', '4', '5', '6', '7'):
    print('There is no such day in the week')
