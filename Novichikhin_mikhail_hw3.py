__author__ = 'Новичихин Михаил Дмитриевич'

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(listt):
    for i in range(0, len(listt)-1, 1):
        for i2 in range(0, len(listt)-1-i, 1):
            if listt[i2] < listt[i2 +1]:
                local = listt[i2]
                listt[i2] = listt[i2 +1]
                listt[i2] = local
            else: 
                pass
    listt.reverse()
    return listt

a = sort_to_max([5,4,3,2,1])
print(a)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parallel(xa, ya, xb, yb, xc, yc, xd, yd):
    # if ((xa != xb) & (ya == yb)) | ((ya != yb) & (xa = xb)) 
    if (((xa-xb) == 0) & ((xc-xd) == 0) & (ya != yb)) | ((ya-yd) == 0) & (xa !=xd):
        return True
    else:
        return False

ou = parallel(2, 2, 2, 6, 5, 9, 5, 5)
print(ou)


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    if m <= n:
        return False
    else:
        pass
    a = 0
    b = 1
    k = 1
    for i in range(1, n, 1):
        c = b 
        b = a + b
        a = c
    if n != 0: 
        k = n
    else:
        n+=1
    print(a, '  ', k)
    k+=1
    print(b, '  ', k)
    for i in range(n, (m-1), 1):
        k+=1
        print(a + b, '  ', k)
        c = b 
        b = a + b
        a = c

fibonacci(15, 18)


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, arr):
    i = 0
    arr_out = []
    while i < len(arr):
        if func(arr[i]) == True:
            arr_out.append(arr[i])
        else:
            pass
        i+=1
    return arr_out


mixed = ['мак', 'просо', 'просо', 'просо', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак', 'просо', 'просо', 'просо', 'просо', 'мак', 'просо', 'просо', 'просо', 'просо', 'просо', 'просо', 'мак']
zolushka = list(filter(lambda x: x == 'мак', mixed))
zoluska = my_filter(lambda x: x == 'мак', mixed)

print(zolushka)

print(zoluska)

