import os
with open('config.yaml', 'r') as f:
    for line in f:
        num = line.find('|')
        name = line[num+3:-1]
        if num == 0:
            if name.__contains__('.'):
                with open(name, 'w') as f_1:
                    pass
            else:
                file_way = name
                if not os.path.exists(name):
                    os.mkdir(name)
        elif num == 3:
            name_way = os.path.join(file_way, name)
            if name.__contains__('.'):
                with open(name_way, 'w') as f_1:
                    pass
            else:
                file_way_1 = name_way
                if not os.path.exists(name_way):
                    os.makedirs(name_way)
        elif num == 6:
            name_way = os.path.join(file_way_1, name)
            if name.__contains__('.'):
                with open(name_way, 'w') as f_1:
                    pass
            else:
                file_way_2 = name_way
                if not os.path.exists(name_way):
                    os.makedirs(name_way)
        elif num == 9:
            name_way = os.path.join(file_way_2, name)
            if name.__contains__('.'):
                with open(name_way, 'w') as f_1:
                    pass
            else:
                file_way_3 = name_way
                if not os.path.exists(name_way):
                    os.makedirs(name_way)
        elif num == 12:
            name_way = os.path.join(file_way_3, name)
            if name.__contains__('.'):
                with open(name_way, 'w') as f_1:
                    pass
            else:
                if not os.path.exists(name_way):
                    os.makedirs(name_way)
