""" Урок 4, завдання 6
Створіть програму авторизації, в якій користувачеві дається 3 спроби ввести свої облікові дані
(логін та пароль). Якщо користувач за меншу кількість спроб ввів вірні дані, програма
достроково припиняє своє виконання та виводить на екран повідомлення: «Авторизацію
успішно пройдено з «№» спроби».
"""

login = 'login'
password = 'password'
attempt_count = 1
while attempt_count <= 3:
    user_login = input('Enter login: ')
    user_password = input('Enter password: ')
    if user_login == login and user_password == password:
        print(f'Authorization successfully passed in {attempt_count} attempts')
        break
    else:
        print('Authorization failed!')
        attempt_count += 1
