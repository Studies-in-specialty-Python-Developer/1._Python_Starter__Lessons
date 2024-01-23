""" Урок 5, завдання 2
Напишіть програму, в якій користувач вводить із клавіатури діапазон чисел (в діапазоні має бути не менше 5
чисел). Вивести на екран суму другого, передостаннього, а також середнього арифметичного значення даної
послідовності.
"""

numbers = []
while len(numbers) < 5:
    numbers = list(map(int, input('Enter at least 5 integer numbers separated by space: ').split()))
    if len(numbers) < 5:
        print("You entered less than 5 numbers")
print(numbers[1] + numbers[-2] + sum(numbers) / len(numbers))
