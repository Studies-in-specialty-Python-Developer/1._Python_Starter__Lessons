""" Урок 2, завдання 3
Напишіть програму, яка розв'язує квадратне рівняння 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0 за формулами 𝑥1,2 =
−𝑏±√𝑏2−4𝑎𝑐
2𝑎
. Значення a, b та c вводяться з клавіатури. Для знаходження кореня використовуйте
оператор зведення в ступінь, а не функцію math.sqrt, щоб отримати комплексні числа у випадку,
якщо вираз під коренем негативний.
"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
d = (b ** 2) - (4 * a * c)
x1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
x2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
print('D = ', d)
print('x1 =', x1, '\nx2 =', x2)
