"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict

def func_1(dct):
    for i in range(100000):
        dct.pop(i)
    for j in range(100000):
        dct[i] = '100'

def func_2(order_dct):
    for i in range(100000):
        order_dct.pop(i)
    for j in range(100000):
        order_dct[i] = '100'

dct = {}
for i in range(10000000):
    dct[i] = i

order_dct = OrderedDict(dct)


print(timeit(stmt="func_1(dct)", setup="from __main__ import func_1, dct", number=1))
print(timeit(stmt="func_2(order_dct)", setup="from __main__ import func_2, order_dct", number=1))

"""
0.006694499999866821
0.01238540000122157
Обычный словарь работает быстрее чем OrderDict
"""