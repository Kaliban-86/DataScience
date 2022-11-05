from statistics import mean
from typing import List
from scipy import linalg
import math

# ВАРИАЦИЯ -  мера разброса данных

# 1) размах - разница между максимальными и минимальными размерами данных
data_list: List[int] = [1, 2, 3, 5, 8, 23, 59, 23, 700]


def data_range(x: List[int]) -> int:
    return max(x) - min(x)


print('Разах data_list -  ', data_range(data_list))

# 2) Дисперсия -

# Среднее значение - сложить и поделить на количество элементов
print('Среднее значение data_list - ', mean(data_list))


# Из кахдого элемента вчитаем среднее значение и получается список с нулевым средним
def de_mean(xs: List[float]) -> List[float]:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


print(de_mean(data_list))

print('Получилось нулевое среднее - ', mean(de_mean(data_list)))


#
# Расчет самой дисперсии
def variance(xs: List[float]) -> float:
    assert len(xs) >= 2, 'Дисперсия требует не менее двух элементов'
    n = len(xs)
    deviation = de_mean(xs)
    sum_of_squares = sum([x ** 2 for x in deviation]) / (n - 1)
    return sum_of_squares


print(variance(data_list))
# корень из дисперсии - стандартное отклонение
print(math.sqrt(variance(data_list)))
