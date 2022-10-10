"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""
import hashlib

my_set = set()
my_str = 'papa'
for i in range(len(my_str)):
    for j in range(i + 1, len(my_str) + 1):
        if my_str[i:j] != my_str:
           my_set.add(hashlib.md5(my_str[i:j].encode()).hexdigest())
print(f'во множестве {len(my_set)} элементов')