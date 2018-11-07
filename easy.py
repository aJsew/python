import shutil
import os

def show_dirs():
    return os.listdir(path=".")

def copy_file(file,to):
    shutil.copy(file,to)

def create_dirs():
    dir_names = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7,', 'dir_8', 'dir_9']
    for i in range(0, len(dir_names)-1, 1):
        os.mkdir(dir_names[i])

def del_dirs():
    dir_names = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7,', 'dir_8', 'dir_9']
    for i in range(0, len(dir_names)-1, 1):
        os.rmdir(dir_names[i])

def del_dir(path):
    path = os.path.join(os.getcwd(), path)
    try:
        os.rmdir(path)
    except:
        print('Tакой директории нет')

def create_del_dirs(y):
    dir_names = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7,', 'dir_8', 'dir_9']
    if y == 1:
        for i in range(0, len(dir_names)-1, 1):
            os.mkdir(dir_names[i])
    elif y == 0:
        for i in range(0, len(dir_names)-1, 1):
            os.rmdir(dir_names[i])
    else:
        return False

def create_dir(path):
    path = os.path.join(os.getcwd(),path)
    try:
        os.mkdir(path)
    except:
        print('Tакая директория уже есть')

def goto(path):
    try:
        os.chdir(path)
    except:
        print('Tакой директории нет')