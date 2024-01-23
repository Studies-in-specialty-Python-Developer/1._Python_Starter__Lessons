""" Урок 5, завдання 3
Напишіть програму, яка на вхід отримує параметри кольору (в діапазоні від 0 до 255 для кожного кольору) у
форматі RGB і виводить на екран кортеж, у якому зберігається колір.
"""

print('Enter color values in RGB format')
red, green, blue = -1, -1, -1
while not all([red in range(256), green in range(256), blue in range(256)]):
    if red not in range(256):
        red = int(input('Enter red color value (0-255): '))
    if green not in range(256):
        green = int(input('Enter green color value (0-255): '))
    if blue not in range(256):
        blue = int(input('Enter blue color value (0-255): '))
print('Your RGB color is', (red, green, blue))
