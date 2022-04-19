import os
dir_name_list = ['my_project', 'settings', 'mainapp', 'adminapp', 'authapp']
for dir_name in dir_name_list[1:]:
    full_dir_name = os.path.join(dir_name_list[0], dir_name)
    if not os.path.exists(full_dir_name):
        os.makedirs(full_dir_name)
