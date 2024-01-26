""" Урок 4, завдання 2
Факторіалом числа n називається число n!=1∙2∙3∙…∙n. Створіть програму, яка обчислює
факторіал введеного користувачем числа.
"""

number = int(input('Enter number: '))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(number, '! =', factorial)
