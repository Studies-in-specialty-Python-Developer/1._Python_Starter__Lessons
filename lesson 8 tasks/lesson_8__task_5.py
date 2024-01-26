""" Урок 8, завдання 5
Створіть програму, яка приймає як формальні параметри зріст і вагу користувача, обчислює
індекс маси тіла і в залежності від результату повертає інформаційне повідомлення (маса тіла в
нормі, недостатня вага або слідкуйте за фігурою). Користувач з клавіатури вводить значення
росту та маси тіла та передає ці дані у вигляді фактичних параметрів під час виклику функції.
Програма працює доти, доки користувач не зупинить її комбінацією символів «off».
"""


def bmi_calc(height, weight):
    bmi = weight / (height ** 2)
    info_str = f'Your BMI is {bmi:.2f}\n'
    if bmi < 18.5:
        info_str += 'Insufficient body weight'
    elif bmi < 25:
        info_str += 'Normal body weight'
    else:
        info_str += 'Excess body weight, watch your figure'
    return info_str


while True:
    your_height = float(input('Enter your height in meters: '))
    your_weight = float(input('Enter your weight in kg: '))
    print(bmi_calc(your_height, your_weight))
    if input('Enter "off" to exit: ') == 'off':
        break
    print()
