"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from timeit import timeit
from collections import deque

my_lst = [i for i in range(10000000)]
my_deque = deque([i for i in range(10000000)])
n = 100000

# 1 задание
def func_11_lst(my_lst):
    for i in range(n):
        my_lst.append(i)
        return my_lst

def func_11_deque(my_deque):
    for i in range(n):
        my_deque.append(i)
        return my_deque


def func_12_lst(my_lst):
    for i in range(n):
        my_lst.extend([1,2])
        return my_lst


def func_12_deque(my_deque):
    for i in range(n):
        my_deque.extend([1,2])
        return my_deque


print(timeit(stmt="func_11_lst(my_lst)", setup="from __main__ import func_11_lst, my_lst", number=1000))
print(timeit(stmt="func_11_deque(my_deque)", setup="from __main__ import func_11_deque, my_deque", number=1000))
print(timeit(stmt="func_12_lst(my_lst)", setup="from __main__ import func_12_lst, my_lst", number=1000))
print(timeit(stmt="func_12_deque(my_deque)", setup="from __main__ import func_12_deque, my_deque", number=1000))
"""
Несколько раз замерял примерно равно
0.00017499999739811756
0.0001793000010366086
0.0002041000007011462
0.00022850000095786527
"""


# 2 Задание
def func_21_lst(my_lst):
    for i in range(n):
        my_lst.insert(0, i)
        return my_deque

def func_21_deque(deque):
    for i in range(n):
        my_deque.appendleft(i)
        return deque

print(timeit(stmt="func_11_lst(my_lst)", setup="from __main__ import func_11_lst, my_lst", number=1000))
print(timeit(stmt="func_11_deque(my_deque)", setup="from __main__ import func_11_deque, my_deque", number=1000))
"""
0.0001711999975668732
0.00017460000162827782

Deque чуть быстрее
"""


# 3 задание

def func_3_deque(my_deque):
    for i in range(n):
        my_deque[i] = i
        return my_deque

def func_3_lst(my_lst):
    for i in range(n):
        my_lst[i] = i
        return my_lst


#print(timeit(stmt="func_3_deque(my_lst)", setup="from __main__ import func_3_deque, my_", number=1000))
#print(timeit(stmt="func_3_lst(my_deque)", setup="from __main__ import func_3_lst, my_lst", number=1000))
"""
Deque чуть медленнее
0.00017809999917517416
0.00020169999879726674
"""