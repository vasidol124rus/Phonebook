# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., 
# где a0= 0, a1= 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13
# Задание необходимо решать через рекурсию

# def fib(num):
#     if num == 1 or num == 2:
#         return 1
#     return fib(num - 1) + fib(num - 2)        

# n = int(input('Введите число: '))
# print(fib(n))

# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# import random

# def max_2min(numbers):

#     max_num = max(numbers)
#     min_num = min(numbers)
#     while max_num in numbers:
#         i_max_num = numbers.index(max_num)
#         numbers[i_max_num] = numbers.index(max_num)
#         numbers[i_max_num] = min_num
# n = int(input('Введите количетво оценок: '))

# marks = [random.randint(1, 5) for _ in range(n)]
# print(marks)
# max_2min(marks)

# print(marks)


# import random

# n = int(input('Введите количетво оценок: '))
# first_number = random.randint(1, 5)
# min_num = first_number
# max_num = first_number
# i_max_num = [0]

# marks = [first_number]

# for i in range(1, n):
#     num = random.randint(1, 5)
#     marks.append(num)
#     if min_num > num:
#         min_num = num
#     if max_num < num:
#         max_num = num
#         i_max_num = [i]
#     elif max_num == num:
#         i_max_num.append(i)     
# print(marks)
# for i in i_max_num:
#     marks[i] = min_num
# print(marks)


# Та же задача со счетчиком времени import time
# import random
# import time

# n = int(input('Введите количетво оценок: '))
# first_number = random.randint(1, 5)
# min_num = first_number
# max_num = first_number
# i_max_num = [0]

# start = time.time()
# marks = [first_number]

# for i in range(1, n):
#     num = random.randint(1, 5)
#     marks.append(num)
#     if min_num > num:
#         min_num = num
#     if max_num < num:
#         max_num = num
#         i_max_num = [i]
#     elif max_num == num:
#         i_max_num.append(i)     
# print(marks)
# for i in i_max_num:
#     marks[i] = min_num
# print(marks)

# end = time.time()
# dif = end - start
# print(dif)

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def prime(n):
#     for div in range(2, n // 2 + 1):
#         if n % div == 0:
#             return 'no'
#         return 'yes'
    
# num = int(input('Введите число: '))
# print(prime(num))
# 
# ускореный вариант
# def prime(n):
#     if n != 2 and n % 2 == 0:
#         return 'no'
#     for div in range(2, int(n ** 0.5) + 1):
#         if n % div == 0:
#             return 'no'
#     return 'yes'
    
# num = int(input('Введите число: '))
# print(prime(n))

# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# Задача №39.  1) Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива

# 2) (пользовательский ввод можно заменить на рандомный ввод)
# Пользователь вводит  размер первого массива – N
# и элементы первого массива. 
# затем размер второго массива M  
# и элементы второго массива
# Нужно вывести те элементы первого массива, которых нет во втором массиве,
# при этом порядок последовательности сохранить исходный
# Ввод: 			Вывод:
# 7			3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

# from random import randint

# n = int(input("Введите длину 1-го массива: "))
# m = int(input("Введите длину 1-го массива: "))
# # list_1 = []
# # list_2 = []
# # for _ in range(n):
# #     list_1.append(randint(1, 10))
# list_1 = [randint(1, 50) for _ in range(n)]
# print(list_1)
# # for _ in range(n):
# #     list_2.append(randint(1, 10))
# set_2 = {randint(1, 50) for _ in range(m)}
# print(set_2)

# # res_list = []
# # for num in list_1:
# #     if num not in set_2:
# #         res_list.append(num)
# #         print(num, end = ' ')

# res_list = [num for num in list_1 if num not in set_2] #Если появляется else тогда блоки if и for меняем местами

# # res_list = [num if num not in set_2 else 0 for num in list_1 ]
# print()
# print(*res_list)        

'''# Задача №41.  1) Дан массив, состоящий из целых чисел. Напишите программу, 
# которая в данном массиве выведет количество элементов, у которых два соседних и, при этом,
# оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. 
# 2) (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит  размер массива – N
# и элементы массива (целые числа). 
# нужно из этого массива вывести количество элементов, 
у которых ближайшие соседние элементы меньше самого элемента.

# Ввод: 			Ввод:
# 5			5
# 1 2 3 4 5			1 5 1 5 1

# Вывод:			Вывод:
# 0			2'''

# import random

# n = int(input("ВВедите количество элементов массива: "))
# list_1 = [random.randint(1, 5) for _ in range(n)] 
# print(list_1)

# count = 0
# for i in range(1, len(list_1) - 1):
#     if list_1 [i-1] < list_1[i] > list_1[i + 1]:
#         count += 1
# print(count)        
# print(sum([1 for i in range(1, len(list_1) - 1) if list_1 [i-1] < list_1[i] > list_1[i + 1]])) #list comprehension


'''# Задача №43.  Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# 2) (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит  размер массива – N
# и элементы массива (целые числа). 
# нужно посчитать сколько повторений у каждого числа
# посчитанные числа можно посчитать повторно в паре с другими числами

# Ввод:			Вывод:
# 1 2 3 2 3 2 2 2		11'''


# import random

# n = int(input("ВВедите количество элементов массива: "))
# my_list = [random.randint(1, 5) for _ in range(n)]
# count= 0
# for i in range(len(my_list)):
#     count += my_list[i+1:]. count(my_list[i])
# print(my_list)
# print(count)


# import random

# n = int(input("ВВедите количество элементов массива: "))
# my_list = sorted([random.randint(1, 5) for _ in range(n)])
# count= 0
# el = my_list[0]
# for num in my_list:
#     if el == num:   ;;;;;;;;;;;;;;;;;   ПОД ВОПРОСОМ   $$$$$$$$$$$$$$$$$$$
#         count += 1
#     else:
#         el = num    
# print(my_list)
# print(count)


''' Задача №45.  Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит  натуральное число  – k
# В диапазоне от 0 до k нужно вывести все пары чисел N и M, в которых сумма делителей N равняется M, 
# а сумма делителей M равняется N (число само на себя делить нельзя)
# Пары необходимо выводить по одной паре в строке, разделяя числа пробелами.
# Каждая пара выводится только один раз, без повторов. 

# Пример: Возьмём 2 числа 220 и 284. Найдём их делители 
# Делители 220 – (1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110)
# 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110  = 284
# Делители 284 – (1, 2, 4, 71, 142 )
# 1 + 2 + 4 + 71 + 142 = 220
# 			Ввод:			Вывод:
# 			300			220 284
'''
# def sum_div(num):
#     summa = 1
#     for div in range(2, num // 2 + 1):
#         if num % div == 0:
#             summa += div
#     return summa
#     # return sum(div for div in range(1, num) if num % div == 0)

# k = int(input("Введите число: "))

# for num_1 in range(2, k + 1):
#     num_2 = sum_div(num_1)
#     if num_1 < num_2 and num_1 == sum_div(num_2) and num_2 < k:
#         print(num_1, num_2)


# x=int(input())
# if x % 7 == 0 or x % 17 == 0:
#     print("YES")
# else:
#     print("NO")

# data = [1, 2, 3, 5, 8, 15, 23,38]
# res = list()
# for i in data:
#     if i % 2 == 0:
#        res.append((i, i ** 2))

# print(res)

# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

# res_list = filter(lambda x: x % 2 == 0, my_list)
# print(*res_list)
# print(list(res_list))

# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

# res_list = list(filter(lambda x: x % 2 == 0, my_list))
# print(res_list)

# res_list=[]
# f = lambda x: x % 2 == 0
# for el in my_list:
#     if f(el):
#         res_list.append(el)
# print(res_list)

# f = lambda x: x % 2 == 0
# [el for el in my_list if f(el)]
# print(res_list)

# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

# res_list = map(lambda x: x % 2 == 0, my_list)
# print(*res_list)
# print(list(res_list))

# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

# res_list = list(map(lambda x: x % 2 == 0, my_list))
# print(res_list)
# #2
# res_list=[]
# f = lambda x: x % 2 == 0
# for el in my_list:
#     res_list.append(f(el))
# print(res_list)
# #3
# f = lambda x: x % 2 == 0
# [f(el) for el in my_list]
# print(res_list)

'''
Задача №47.  1) У вас есть код, который вы не можете менять 
(так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать): 

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))

Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, 
а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

2) Есть код:

transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transformed_values = list(map(transformation, values))
if values == transformed_values:
         print(‘ok’)
else:
         print(‘fail’)

- В переменную transformation нужно прописать такую функцию, 
что бы в переменной transformed_values получилась копия списка values
'''

# transformation = lambda x: x**2
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')



'''Задача №49.  1) Планеты вращаются вокруг звезд по эллиптическим орбитам. 
Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, 
по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, 
что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. 
Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
 Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
 При решении задачи используйте списочные выражения.
 Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, 
 а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна

2) - Дан список размеров(длина, ширина) эллипсов 
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
Напишите функцию find_farthest_orbit(list_of_orbits), 
которая находит площадь самого большого эллипса и возвращает кортеж с его размерами.
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
-   Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
При решении задачи используйте списочные выражения.
Гарантируется, что самый большой эллипс всего один.
'''

# 2
# def find_farthest_orbit(list_of_orbits):
#     list_of_ellips = [a_b for a_b in list_of_orbits if a_b[0] != a_b[1]]
#     list_of_areas = [a * b * pi for a, b in list_of_ellips]
#     max_area = max(list_of_areas)
#     i_max_area = list_of_areas.index(max_area)
#     return list_of_ellips[i_max_area]
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

# def find_farthest_orbit(list_of_orbits):
#     s_max = 0
#     for a, b in list_of_orbits:
#         if a != b:
#             s = pi * a * b
#             if s > s_max:
#                 s_max = s
#                 a_b = a, b
#     return a_b
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))


'''Задача №51.  Напишите функцию same_by(characteristic, objects), которая проверяет, 
все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. 
Если значение характеристики для разных объектов отличается - то False. 
Для пустого набора объектов, функция должна возвращать True. 
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод:							Вывод:
values = [1, 21, 101, 61]		same
'''
# ВАРИАНТ 1

# def same_by(characteristic, object):
# 	return len(set(map(characteristic, object))) < 2
# values = [10, 210, 11, 610]

# if same_by(lambda x: x % 2 == 0, values):
# 	print("same")
# else:
# 	print("different")

# Вариант 2

# def same_by(characteristic, object):
#     new_list = list(filter(characteristic, object))
#     print(f"{object = }")
#     print(f"{new_list = }")
#     return object == new_list or not new_list

# values = [1, 21, 11, 61]

# if same_by(lambda x: x % 2 == 0, values):
# 	print("same")
# else:
# 	print("different")


def same_by(characteristic, object):
    new_list = list(map(characteristic, object))
    print(f"{new_list = }")
    return object == new_list or not new_list

values = [1, 21, 10, 61]

if same_by(lambda x: x % 2 == 0, values):
	print("same")
else:
	print("different")