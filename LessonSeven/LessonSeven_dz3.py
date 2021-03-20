import os
import os.path

project_list = {'project_one': ['mainapp', 'authapp']}
file_list = ['base.html', 'index.html']
path_main = r'C:\Users\hitma\OneDrive\Документы\test\testhw\pycharm_homework\LessonSeven\project_one\mainapp'
path_aut = r'C:\Users\hitma\OneDrive\Документы\test\testhw\pycharm_homework\LessonSeven\project_one\authapp'


def make_dir(p_list):
    for f, i in p_list.items():
        if not os.path.exists(f):
            for m in range(len(i)):
                os.makedirs(os.path.join(f, i[m]))


FileF = os.path.join(path_main, 'base.html')
FileF1 = os.path.join(path_main, 'index.html')
FileF2 = os.path.join(path_aut, 'base.html')
FileF3 = os.path.join(path_aut, 'index.html')
with open(FileF1, 'w') as y:
    with open(FileF2, 'w') as a:
        with open(FileF3, 'w') as e:
            with open(FileF, 'w') as t:
                make_dir(project_list)
