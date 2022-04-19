import sys


def show_sales():
    price_list = []
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            line = line[line.find(" '") + 2: -3]
            price_list.append(line)
    return price_list


start_list = sys.argv
if len(start_list) == 3:
    str_list = show_sales()
    for line in str_list[int(start_list[1]) - 1: int(start_list[2])]:
        print(line)

elif len(start_list) == 2:
    str_list = show_sales()
    for line in str_list[int(start_list[1]):]:
        print(line)
else:
    str_list = show_sales()
    for line in str_list:
        print(line)
