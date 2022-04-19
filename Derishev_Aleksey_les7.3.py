import os
name_dir = 'templates'
old_neme_dir_1 = r'my_project\mainapp\templates\mainapp'
old_neme_dir_2 = r'my_project\authapp\templates\authapp'
new_name_dir_1 = r'.\templates\mainapp'
new_name_dir_2 = r'.\templates\authapp'
if not os.path.exists(name_dir):
    os.mkdir(name_dir)
try:
    os.rename(old_neme_dir_1, new_name_dir_1)
    os.rename(old_neme_dir_2, new_name_dir_2)
except FileNotFoundError:
    print('Файлы и папки не найдены')