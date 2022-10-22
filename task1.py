"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return print(lst_obj)

def bubble_sort_1(lst_obj):
    n = 1
    d = 0
    while n < len(lst_obj):
        if d == len(lst_obj) - 1:
            break
        d = 0
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
            else:
                d += 1
        n += 1
    return print(lst_obj)

#orig_list = [87, 57, 25, 24, 3, 2, -20, -86, -96, -100]
orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
bubble_sort(orig_list)
bubble_sort_1(orig_list)
# замеры 10
#print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
#print(timeit("bubble_sort_1(orig_list[:])", globals=globals(), number=1000))

#orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
#print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
#print(timeit("bubble_sort_1(orig_list[:])", globals=globals(), number=1000))

#orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
#print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
#print(timeit("bubble_sort_1(orig_list[:])", globals=globals(), number=1000))
"""
0.0037508000004891073
0.35492470000008325
37.90766269999949
"""

"""
Замеры сравнения
0.004174400000010792
0.004645899999559333
0.34218959999998333
0.018443800000568444
36.47838409999986
39.42635220000011

Делаю следующий вывод
если условия прерывания выполняется то работает быстрее
если услови не выполняется, то ресурс тратится на счетчик и слегка повышается время работы
Применение сомнительное
"""