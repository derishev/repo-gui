def my_gen():
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена']
    klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
    while True:
        if len(tutors) > len(klasses):
            klasses.append('None')
        elif len(tutors) < len(klasses):
            tutors.append('None')
        else:
            break
    for tutor, klass in zip(tutors, klasses):
        my_tuple = (tutor, klass)
        yield my_tuple


for my_tuple in my_gen():
    print(my_tuple)
print(my_gen()) # проверяем генератор ли это

