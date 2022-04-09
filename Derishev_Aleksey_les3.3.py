def thesaurus(*args):
    diction = {}
    for name in args:
        first_letter = name[0]
        if diction.get(first_letter):
            diction[first_letter] = diction[first_letter] + [name]
        else:
            diction[first_letter] = [name]
    print(diction)

thesaurus("Иван", "Мария", "Петр", "Илья", "Икра")
