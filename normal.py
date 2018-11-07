import os
import easy

answer = ''

while answer != 'q':
    print('Перейти в папку - 1')
    print('Просмотреть содержимое текущей папки - 2')
    print('Удалить папку - 3')
    print('Создать папку - 4')
    print('для выхода - q')
    answer = input('Ваш ответ: ')

    if answer == '1':
        name = input ('наберите полный путь папки: ')
        easy.goto(name)
    elif answer == '2':
        print(easy.show_dirs())
    elif answer == '3':
        name = input('наберите полный путь папки: ')
        easy.del_dir(name)
    elif answer == '4':
        name = input('наберите полный путь папки: ')
        easy.create_dir(name)
    elif answer == 'q':
        pass
    else:
        print('Такого пункта меню нет')
