"""
Задание 1.
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple

company = namedtuple('company', ['name', 'profit_1', 'profit_2', 'profit_3', 'profit_4', 'profit_total'])
companys = []
numbers_com = int(input("Введити кол-во компаний: "))
total = 0
for i in range(numbers_com):
    name = input(f"Название {i+1}-ого предприятия: ")
    profit_1 = int(input("Прибыль за 1 квартал: "))
    profit_2 = int(input("Прибыль за 2 квартал: "))
    profit_3 = int(input("Прибыль за 3 квартал: "))
    profit_4 = int(input("Прибыль за 4 квартал: "))
    profit_total = profit_1 + profit_2 + profit_3 + profit_4
    total += profit_total
    companys.append(company(name=name, profit_1=profit_1, profit_2=profit_2, profit_3=profit_3,
    profit_4=profit_4, profit_total=profit_total))
total_avg = total / numbers_com
print(f"Предприятия с прибылью выше средней {total_avg}: ")
for company in companys:
    if company.profit_total >= total_avg:
        print(company.name)
print(f"Предприятия с прибылью неже средней {total_avg}: ")
for company in companys:
    if company.profit_total < total_avg:
        print(company.name)


