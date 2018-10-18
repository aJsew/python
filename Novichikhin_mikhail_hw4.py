__author__ = 'Новичихин Михаил Дмитриевич'
import re
import random
# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.



def letters1(line):
    strout = ''
    output = []
    k = 1
    i = 0

    for i in range(0, len(line), 1):
        if line[i].islower():
            strout += line[i]
        else:
            if strout:
                output.append(strout)
                strout = ''
    output.append(strout)

    return output

a = letters1('CtMmEZUOmcq')
print(a)

def lettersRE(line):
    line = 'C' + line 
    output = re.findall(r'\w([a-z]+)', line)
    return output

b = lettersRE('CtMmEZUOmcq')
print(b)



# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

def difcase(line):
    strl = 0
    strout = ''
    output = []
    k = 1
    i = 0

    for i in range(0, len(line), 1):
        if (strl == 2):
            if ((i+2) <= (len(line)-1)):
                if ((line[i].isupper()) & (line[i+1].isupper()) & (line[i+2].isupper())):
                    strout += line[i]
                else:
                    if strout:
                        output.append(strout)
                        strout = ''
                        strl = 0
                    else:
                        pass
            else:
                pass
        else:
            if line[i].islower():
                strl += 1
            else:
                strl = 0
    return output

print(difcase('GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec'))


def difcaseRE(line):
    output = re.findall(r'[a-z]{2}[A-Z]+[A-Z]{2}', line)
    for i in range(len(output)):
        output[i] = output[i][2:-2]  


    return output

print(difcaseRE('GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec'))



# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

f = open('hw.txt', 'w')
fa = []
st = ''
max = 0

for i in range(2500):
    k = str(random.randint(0, 9))
    f.write(k)
    fa.append(k)

st = fa[0]
for i in range(0, len(fa)-1, 1):
    if fa[i] == fa[i+1]:
        st += fa[i]
    else:
        if st:
            if int(max) < int(st):
                max = st
            st = ''
f.write('\n' + str(max))

f.close()
