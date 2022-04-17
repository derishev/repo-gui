def gen(max_num):
    for numer in range(1, max_num + 1, 2):
        yield numer

max_num = int(input('Введите максимальное число: '))
for numer in gen(max_num):
    print(numer, end=' ')