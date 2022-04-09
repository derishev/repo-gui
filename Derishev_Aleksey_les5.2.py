max_num = int(input('Введите максимальное число: '))
my_gen = (num for num in range(1, max_num + 1, 2))
for numer in my_gen:
    print(numer, end=' ')