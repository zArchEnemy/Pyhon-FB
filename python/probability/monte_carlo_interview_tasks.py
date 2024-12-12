"""Module on solving problems with monte carlo for interview."""

# +
import random
from random import shuffle

import numpy as np  # linear algebra
import pandas as pd  # data processing

# -

# Problem:1
# Определить вероятность того, что в группе из 23 человек у 2 будут соврпадать дни рождения

days_a_year = pd.Series(range(365))  # array 0...364
days_a_year

birth_date_23 = days_a_year.sample(23, replace=True)  #
birth_date_23.duplicated()  # удаляем дубликаты

rooms = []
for i in range(10000):
    sample = days_a_year.sample(23, replace=True).duplicated().max()
    rooms.append(sample)
rooms

np.mean(rooms)

# моделируем комнаты
rooms_2 = []
for i in range(10000):
    sample_2 = days_a_year.sample(23, replace=True).duplicated().max()
    rooms_2.append(sample_2)
# выборка с поаторением. Количество серий - 10 000
# Ошибка байесовского восприятия
np.mean(rooms_2)

# Problem 2:
# Экзамен проходит по следующей схеме: если билет вытянут, то после ответа экзаменатор его откладывает.Студент выучил 20 билетов из 30.Каким по счету ему идти чтобы вероятность вытянуть билет, который он знает была больше?

# list of exam_cards of 30
exam_cards = list(range(1, 31))
# student = list(range(1,21))
print(exam_cards)
print()
# print(student)

# +
# Генерация списка из 20 уникальных случайных значений
student = random.sample(range(1, 31), 20)

print(student)
# -

# shuffle the exam_cards
shuffle(exam_cards)

print(exam_cards)

5 in student  # card 5 in student?

trials = 10000
result = []
for _ in range(trials):
    shuffle(exam_cards)
    # Проверка, находится ли exam_cards[10] в student
    # Приводим булево значение к int
    result.append(int(exam_cards[10] in student))
mean_result = np.mean(result)

20 / 30, 2 / 3


#
