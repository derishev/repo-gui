diction = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'tree': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
def num_translate(key):
    word = diction[key]
    return word

key = input('Напишите по английски число от 0 до 10: ')
if key in diction:
    print(f'Перевод {key} - {num_translate(key)}')
else:
    print('None')