"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""

def counter(number, number_sum = 0, index = 1):
    if number == 0:
        print(number_sum)
        return
    number_sum = number_sum + index
    index = index / -2
    counter(number - 1, number_sum, index)

if __name__ == '__main__':
    counter(3)