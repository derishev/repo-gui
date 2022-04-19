import os
my_dict = {
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0
}
folder = '.'
#folder = os.path.join('.', 'some_data')
#отказывалась работать совсем, пока не перешел в саму папку some_data
for item in os.listdir(folder):
    if os.stat(item).st_size < 100:
        value = my_dict[100]
        my_dict[100] = value + 1
    elif os.stat(item).st_size < 1000:
        value = my_dict[1000]
        my_dict[1000] = value + 1
    elif os.stat(item).st_size < 10000:
        value = my_dict[10000]
        my_dict[10000] = value + 1
    else:
        value = my_dict[100000]
        my_dict[100000] = value + 1

print(my_dict)
