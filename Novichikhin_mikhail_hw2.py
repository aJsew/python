__author__ = 'Новичихин Михаил Дмитриевич'

import random 
# normal
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]



number_list = []
output = []

for i in range(0, random.randint(1, 100), 1):
	number_list.append(random.randint(-1000, 1000))

print(number_list)
i = 0

for a in range(0, (len(number_list) - 1), 1):
	if (int(number_list[a])) < 0:
		pass
	else:
		if ((float((int(number_list[a])) ** 0.5)) % 1) == 0:
			output.append(int((int(number_list[a])) ** 0.5))

print(output)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
days_dict = {'1': 'первое', '2': 'второе', '3': 'третье', '4': 'четвертое', '5': 'пятое', '6': 'шестое', '7': 'седьмое', '8': 'восьмое', '9': 'девятое', '10': 'десятое', '11': 'одиинадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': '', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'}
month_dict = {'1': 'января', '2': 'февраля', '3': 'марта', '4': 'апреля', '5': 'мая', '6': 'июня', '7': 'июля', '8': 'августа', '9': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}
date = input('Введите дату в формате: dd.mm.yyyy')
a = 0
day = 0
month = 0
year = 0
day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:])

if ((int(month) == 1) | (int(month) == 3) | (int(month) == 5) | (int(month) == 7) | (int(month) == 8) | (int(month) == 10) | (int(month) == 12)):
    if (int(day) > 0) & (int(day) <= 31):
        if (int(year) > 0):
            print(days_dict[(str(day))] + ' ' +  month_dict[(str(month))] + ' ' + str(year) +' года.')
        else:
            print('Год введен некорректно ' + str(year) + '??')
    else:
        print('Дни введены некрректно' + str(day) + '??')
elif ((int(month) == 4) | (int(month) == 6) | (int(month) == 9) | (int(month) == 11)):
    if ((int(day)) > 0) & ((int(day)) <= 30):
        if (int(year) > 0):            
            print(days_dict[(str(day))] + ' ' + month_dict[(str(month))] + ' ' +  str(year) +' года.')

        else:
            print('Год введен некорректно ' + str(year) + '??')
    else:
        print('Дни введены некрректно' + str(day) + '??')
elif (int(month) == 2):
    if ((int(year) > 0) & ((int(year) % 4) == 0) & ((int(year) % 100) != 0)):
        if ((int(day) > 0) & (int(day) <= 29)):
            print(days_dict[(str(day))] + ' ' + month_dict[(str(month))] + ' ' + str(year) + ' года.')

        else: 
            print('Дни введены некрректно' + str(day) + '??')
    elif ((int(year) > 0) & ((int(year) % 400) == 0)):
        if (int(day) > 0) & (int(day) <= 29):
            print(days_dict[(str(day))] + ' ' + month_dict[(str(month))] + ' ' + str(year) + ' года.')
        else:
            print('Дни введены некрректно' + str(day) + '??')
    else: 
        print('Год введен некорректно ' + str(year) + '??')
else:
    print('Месяц введен некорректно' + str(month) + '??')
    pass


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

n = ''

#n = random.randint(-100, 100)

while not n.isdigit():
    n = input('Введите число: ')

output = []
n = int(n)
if n >= 0:
    for i in range(n):
        output.append(random.randint(-100, 100))
print(str(output))


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

n = ''
lst_local = 0
lst = []
lst_out = []
lst_out_no_similars = []
while ((n != 'n') & (n != 'N')):
    n = input('Вводите числа, чтобы выйти нажмите n/N')
    if n.isdigit():
        lst.append(int(n))


for i in range(0, len(lst), 1):
    lst_local = lst[i]
    if lst.count(lst_local) == 1:
        lst_out_no_similars.append(lst_local)


for i in range(0, len(lst), 1):
    if lst_out.count(lst[i]) >= 1:
        pass
    else:
        lst_out.append(lst[i])



print(lst_out, lst_out_no_similars)