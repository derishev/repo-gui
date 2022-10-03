"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

import random

def game(number, counter = 0):
    if counter > 9:
        print('Попытки кончились. Вы проиграли!!!')
        return
    game_number = int(input('Угадайте задуманное число '))
    if game_number == number:
        print('Вы угадали!!!')
        return
    elif game_number > number:
        print('Загаданное число меньше указанного')
        counter += 1
        game(my_number, counter)
    elif game_number < number:
        print('Загаданное число больше указанного')
        counter += 1
        game(my_number, counter)


if __name__ == '__main__':
    my_number = random.randint(0, 100)
    game(my_number)