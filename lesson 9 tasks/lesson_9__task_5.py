""" Урок 9, завдання 5
Створіть функцію quadratic_equation, яка приймає на вхід 3 параметри: a, b, c. Усередині цієї
функції створити змінні x1, x2 зі значенням None (спочатку приймаємо, що рівняння не має
коренів) та функцію calc_rezult з формальними параметрами зовнішньої функції
quadratic_equation. Всередині функції calc_rezult здійснити пошук дискримінанта, згідно з
результатом якого зробити розрахунок коренів рівняння. Зовнішня функція quadratic_equation
має повернути перелік значень коренів квадратного рівняння. Надати можливість користувачеві
ввести з клавіатури формальні параметри для передачі їх у створену функцію
quadratic_equation, результати роботи функції відобразити на екрані.
"""


def quadratic_equation(a, b, c):
    x1 = x2 = None

    def calc_rezult(a, b, c):
        nonlocal x1, x2
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
        elif d == 0:
            x1 = x2 = -b / (2 * a)
        return [x1, x2]

    return calc_rezult(a, b, c)


a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
print(quadratic_equation(a, b, c))
