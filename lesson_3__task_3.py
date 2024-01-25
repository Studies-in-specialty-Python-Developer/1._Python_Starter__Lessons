""" Урок 3, завдання 3
Напишіть програму, яка розв'язує квадратне рівняння 𝑎𝑥 2 + 𝑏𝑥 + 𝑐 = 0 у дійсних числах.
На відміну від аналогічної вправи з минулого уроку, програма повинна видавати повідомлення
про відсутність дійсних коренів, якщо значення дискримінанта 𝐷 = 𝑏2 − 4𝑎𝑐 негативне, єдине
рішення 𝑥 = − 𝑏 / 2𝑎 , якщо він дорівнює нулю, або два корені 𝑥1,2 = −b±D−−√/2a, якщо він позитивний.
"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
d = (b ** 2) - (4 * a * c)
print('D = ', d)
if d < 0:
    print('No real roots')
elif d == 0:
    print('One real root')
    print('x = ', -b / (2 * a))
else:
    print('Two real roots')
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('x1 =', x1, '\nx2 =', x2)
