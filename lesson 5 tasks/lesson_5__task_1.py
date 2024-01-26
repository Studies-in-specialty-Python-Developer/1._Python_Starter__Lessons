""" Урок 5, завдання 1
Створіть програму, яка зчитує рядок, в якому знаходиться ПІБ користувача і перевіряє, чи складається рядок з
літер, при чому кожне слово має бути записане з великої літери. Вивести результат на екран.
"""

full_name = input('Enter your full name: ')
full_name_error = 0
if len(full_name.split()) != 3:
    print('Full name must consist of 3 parts')
    full_name_error += 1
if not full_name.replace(' ', '').isalpha():
    print('Full name must consist of letters and spaces')
    full_name_error += 1
if not full_name.istitle():
    print('All parts must start with a capital letter')
    full_name_error += 1
if full_name_error:
    print(f'Full name is incorrect. You made {full_name_error} errors')
else:
    print('Full name is correct')
