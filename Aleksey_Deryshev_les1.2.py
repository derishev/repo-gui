max_summ = 0
nambers = []
max_summ_1 = 0
for namber in range (1, 1001):
    if namber % 2 == 1:
        nambers.append(namber**3)
        stroka = str(namber**3)
        stroka_1 = str((namber**3)+17)
        summ_1 = 0
        summ = 0
        for znach in stroka:
            summ = summ + int(znach)
        if summ % 7 == 0:
            max_summ = max_summ + int(stroka)
        for znach_1 in stroka_1:
            summ_1 = summ_1 + int(znach_1)
        if summ_1 % 7 == 0:
            max_summ_1 = max_summ_1 + int(stroka_1)

print('Ответ: ', max_summ)
print('Ответ 2: ', max_summ_1)
