Домашняя работа Деришева Алексея к 3 занятию
Попрежнему дублирую архив и githab

Так и не получилось решить 4 задачу. Вложенный словарь создать получилось а наполнить вложеный список вложенного словаря нет

На всякий случай прикладываю НЕ РАБОЧИЙ код 4 го задания на чем я остановился

def thesaurus_adv(*args):
    diction = {}
    for name in args:
        number_lette = name.find(' ')
        first_letter_surname = name[number_lette + 1]
        first_letter_name = name[0]
       # if diction.get(first_letter_surname):
        #    diction[first_letter_surname] = diction[first_letter_surname][first_letter_name] + {first_letter_name: [name]}
        #else:
        diction[first_letter_surname] = {first_letter_name: [name]}
    print(diction)

thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
