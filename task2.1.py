"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

# Гномья сортировка
from random import randint
from timeit import timeit

m = 5

def sort_1(m):
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
    print(orig_list)
    n = len(orig_list)
    i = 0
    while True:
        if i + 1 == n:
            break
        if orig_list[i + 1] >= orig_list[i]:
            i += 1
        else:
            orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
            if i > 0:
                i -= 1
            else:
                i += 1

    print(orig_list)
    #return orig_list[m]
    return print(f'Медиана = {orig_list[m]}')

sort_1(m)

#замеры 11
#print(timeit("sort_1(m)", globals=globals(), number=1000))

m = 50

# замеры 101
#print(timeit("sort_1(m)", globals=globals(), number=1000))


m = 500

# замеры 1001
#print(timeit("sort_1(m)", globals=globals(), number=1000))

"""
0.010530099999414233
0.5335358000002088
53.73330140000053
"""
