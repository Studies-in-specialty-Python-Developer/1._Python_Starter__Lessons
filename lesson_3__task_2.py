""" Урок 3, завдання 2
Напишіть програму, яка обчислює значення функції 𝑦 = cos(3x), де - 𝜋 <= x <= 𝜋 та вводиться з клавіатури.
Відповідь подати у радіанах.
"""

from math import pi, cos

angle = 2 * pi
while angle < -pi or angle > pi:
    angle = float(input('Enter an angle in the range -pi ... pi: '))
y = cos(3 * angle)
print(y)
