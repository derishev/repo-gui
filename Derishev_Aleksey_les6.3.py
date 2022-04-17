import json
name_dict = {}
name_list = []
hobby_list = []
with open('surnames.txt', 'r', encoding='utf-8') as f, open('hobby.txt', 'r', encoding='utf-8') as f_1:
    for name in f:
        name = name.replace('\n', '')
        name_list.append(name)
    for hobby in f_1:
        hobby = hobby.replace('\n', '')
        hobby_list.append(hobby)
    while True:
        if len(name_list) > len(hobby_list):
            hobby_list.append('None')
        elif len(name_list) < len(hobby_list):
            exit(1)
        else:
            break
    for name, hobby in zip(name_list, hobby_list):
        name_dict[name] = hobby
with open('dict.txt', 'w', encoding='utf-8') as f:
    dict_json = json.dumps(name_dict)
    f.write(dict_json)
print(name_dict)
