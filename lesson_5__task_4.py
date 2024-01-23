""" Урок 5, завдання 4
Ознайомтеся за допомогою документації з класами namedtuple та deque модуля collections. Створіть
фабрику іменованих кортежів оцінок для учнів однієї групи з предметів: алгебра, геометрія, історія,
інформатика, географія. Вивести дані на екран.
"""

from collections import namedtuple, deque

Scores = namedtuple('Scores', 'algebra geometry history informatics geography')
scores_1 = Scores(1, 2, 3, 4, 5)
scores_2 = Scores(5, 4, 3, 2, 1)
group = deque([scores_1, scores_2])
scores_3 = Scores(5, 4, 3, 4, 5)
group.append(scores_3)
print('scores 1 =', scores_1, '\nscores 2 =', scores_2, '\nscores 3 =', scores_3)
print('group scores:', group)
