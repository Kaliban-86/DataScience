from statistics import mean
from typing import List

# ВАРИАЦИЯ -  мера разброса данных

# 1) размах - разница между максимальными и минимальными размерами данных
data_list: List[int] = [1, 2, 3, 5, 8, 23, 59, 123, 900]


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
