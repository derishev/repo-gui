"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
   return [i for i in nums if i % 2 ==0]

# Заполняем масив
nums = []
for i in range(1000):
    nums.append(i)




print(timeit(stmt="func_1(nums)", setup="from __main__ import func_1, nums", number=1000))
print(timeit(stmt="func_2(nums)", setup="from __main__ import func_2, nums", number=1000))