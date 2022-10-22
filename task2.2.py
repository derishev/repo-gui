"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit

m = 5

def sort_1(m):
    my_lst = [randint(-100, 100) for _ in range(2 * m + 1)]
    print(my_lst)
    for _ in range(m):
        my_lst.remove(max(my_lst))
    #return max(my_lst)
    return print(f'Медиана = {max(my_lst)}')

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
0.006000100000164821
0.08404269999937242
4.28607909999937
"""