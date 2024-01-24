""" Урок 7, завдання 2
Створіть програму, яка емулює роботу сервісу зі скорочення посилань. Повинна бути реалізована
можливість введення початкового посилання та короткої назви і отримання початкового посилання за її
назвою.
"""

from faker import Faker

faker = Faker()
# creating a list of url aliases
short_url = {}
for i in range(5):
    short_url[faker.word()] = faker.url()
for item in short_url:
    print(f'{item}: {short_url[item]}')
# getting URL by alias
alias = input('Enter alias: ')
print(short_url.get(alias, 'No such alias found!'))
