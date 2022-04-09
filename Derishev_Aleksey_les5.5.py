# решение "в лоб"

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
resalt = []
for i in src:
    if src.count(i) == 1:
        resalt.append(i)

print(resalt)

#оптимизация (делаем генератором, и записываем ответ в картеж (меньше места занимает),
# хотя про кортеж спорно, т.к. ответ требуется в списке
res_gen = {}
res_gen = {src_num for src_num in src if src.count(src_num) == 1}
print(res_gen)


