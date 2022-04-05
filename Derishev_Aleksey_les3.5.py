from random import choice


def get_jokes(num, repeat):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    big_joke = []
    i = 0
    if repeat == 1:
        while i < num:
            one_joke = choice(nouns)
            nouns.remove(one_joke)
            two_joke = choice(adverbs)
            adverbs.remove(two_joke)
            three_joke = choice(adjectives)
            adjectives.remove(three_joke)
            big_joke.append(one_joke +' ' + two_joke + ' ' + three_joke)
            i += 1
    else:
        while i < num:
            one_joke = choice(nouns)
            two_joke = choice(adverbs)
            three_joke = choice(adjectives)
            big_joke.append(one_joke +' ' + two_joke + ' ' + three_joke)
            i += 1
    return big_joke


number = int(input('Введите количество шуток: '))
rep = int(input('Если хотите чтоб слова не повторялись введите 1: '))
print(get_jokes(number, rep))
