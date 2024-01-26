""" Урок 9, завдання 2
Створіть програму, яка перевіряє, чи є паліндромом введена фраза.
"""

# original_phrase = '"Пустите!" - Летит супу миска Максиму. - "Пустите, летит суп!"'
original_phrase = 'Eva, can I see bees in a cave?'

removal_table = str.maketrans('', '', ' ,-.?!":;')
phrase = original_phrase.translate(removal_table).lower()
if phrase == phrase[::-1]:
    print('This is a palindrome')
else:
    print('This is not a palindrome')
