import os

project_list = {'test_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def make_dir(p_list):
    for f, i in p_list.items():
        if not os.path.exists(f):
            for m in range(len(i)):
                os.makedirs(os.path.join(f, i[m]))


make_dir(project_list)
