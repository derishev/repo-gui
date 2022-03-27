duration = int(input('Введите продолжительность в секуундах: '))
if duration <= 0:
    print('Ваше число меньше одного')
else:
    if duration < 60:
        print(duration, ' сек')
    elif duration < 3600:
        print(duration // 60, '  мин',duration % 60, '  сек')
    elif duration < 86400:
        min_sek = duration % 3600
        min = min_sek // 60
        sek = min_sek % 60
        print(duration // 3600, '  час', min, '  мин', sek, '  сек')
    else:
        hour_min_sek = duration % 86400
        hour = hour_min_sek // 3600
        min_sek = hour_min_sek % 3600
        min = min_sek // 60
        sek = min_sek % 60
        print(duration // 86400, '  дн',hour, '  час', min, '  мин', sek, '  сек')
