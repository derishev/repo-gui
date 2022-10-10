"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib
import uuid

salt = uuid.uuid4().hex
my_cash = {}

def my_fanc(url):
    if my_cash.get(url):
        print(f'{url} есть в кеше, его хеш {hashlib.sha512(salt.encode() + url.encode()).hexdigest()}')
    else:
        my_hash = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
        my_cash[url] = my_hash
        print(my_cash)


if __name__ == '__main__':
    my_fanc('https://www.yandex.ru')
    my_fanc('https://www.ya.ru')
    my_fanc('https://www.yandex.ru')