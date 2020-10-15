# print('2 + 3 =', 2 + 3)
# print('1', '2', '3', sep=' + ', end=' ') sep - заменяет пробел по умолчанию на какой либо символ end - перевод строки
# print('=', 1 + 2 + 3)
# a = 1 + 5j
# print(a, 'is complex number', isinstance((1 + 5j), complex)) isinstance() для проверки принадлежности данных определенному классу (типу данных)

# тип данных список
# arr = [43, 324.2332, 'i am love python']
# print(arr, type(arr), isinstance(arr, (int, list, dict)))
# доступ по индексу
# listTemp = [21, 24, 15, 34, 34, 56, 23, 67, 23, 86, 12, 23]
# print('listTemp[4]=', listTemp[4])
# print('listTemp[3:6]=', listTemp[3:6])
# print('listTemp[6:]=', listTemp[6:])

# кортежи те же списки но неизменяемы
# listTupl = (12, 123, 12324, 1243, 457)
# print(listTupl, listTupl[0], '- элемент кортежа с индексом 0', type(listTupl))

# строки
# str = 'the string'
# print(str[4])

# множества (set)
# set = {1, 54, 67, 342, 232, 456}
# print(type(set))
# setTemp = {1, 1, 1, 12, 1212, 2, 2, 2, }
# print(setTemp)

# словари (dict)
# inc = {1: 'hey', 22: 'Nyy'}
# print(type(inc))
# print(inc[1])
# print(inc[22])

# преобразование типов данных
# print(int(10.6))
# print(float('10.6'))
# string = 345
# print(type(str(string)))
# list = [1, 2, 3, 4]
# print(set(list))
# set = ('a,d,f', 234, 3 + 5j)
# print(tuple(set))


# world = 'hello world'
# print(list(world))
# # что бы преобразовать в строку список
# print(''.join(['h', 'e', 'l', 'l', 'o']))

# рифмитические выражения
# степень
# print(11 ** 6)
# деление
# print(11 // 6)
# выведет три раза строку
# print('hhh' * 3)
# выведет те же элементы списка
# second_list = [0, 1, 2, 3, 4]
# print(second_list * 2)

# условия
# num = int(input('Введите число'))
#
# if num % 2 == 0:
#     print('Чётное')
# else:
#     print('Не чётное')
#     print('Всё')

# run = True
#
# while run:
#     print('В цикле')
#     num = int(input('Введите число'))
#     if num == 5:
#         print('Не в цикле')
#         run = False
#         break

# for i in range(1, 5):
#     print(i)

# name = input('Enter your name')
# print('Hello', name)

# pharse = 'Hasta la vista'
# who = '"baby"'
# print(pharse, ', ', who, '!', sep='')

# num = 2 + 7
# string = '2 + 7 = '
# print(string + str(num))
# print(num + 1)

# name = str(input())
# print('Hello, ', name, '!', sep='')

# mens = int(input('Введите количество школьников'))
# appls = int(input('Введите количество яблок'))
# remains = mens // appls
#
# print('В корзине осалось', remains, 'яблок!')

# n = int(input())
#
# print(2 ** n)

# Дано натуральное число. Выведите его последнюю цифру.
# num = int(input())
# x = num % 10
#
# print(x)

# Дано положительное двузначное число. Найдите число десятков в нем.
# num = int(input())
#
# print(num // 10 % 10)

# Дано натуральное число. Найдите цифру, стоящую в разряде десятков в его десятичной записи
# (вторую справа цифру или 0, если число меньше 10).

# Дано трехзначное число. Найдите сумму его цифр.

# Запишите букву 'A' (латинскую, заглавную) 100 раз подряд.
# Сдайте на проверку программу, которая выводит эту строчку (только буквы, без кавычек или пробелов).

# print('A' * 100)

# Дано число N. С начала суток прошло N минут.
# Определите, сколько часов и минут будут показывать электронные часы в этот момент.

# Дано трёхзначное число, удалить последнюю цифру

# Пирожок в столовой стоит A рублей и B копеек. Определите, сколько рублей и копеек нужно заплатить за N пирожков.
# a = int(input())
# b = int(input())
# n = int(input())
#
# totalCount = a * 100 + b
# countCent = n * totalCount
# resultRub = countCent // 100
# resultCent = countCent % 100
#
# print(resultRub, resultCent)

# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере
# (важно в точности соблюдать вывод программы: обратите внимание на пробелы и на точки).
# Нельзя пользоваться конкатенацией строк, используйте print с несколькими параметрами.
# Вывод программы:
# The next number for the number 179 is 180.
# The previous number for the number 179 is 178.

# num = int(input())
# print('The next number for the number', num, 'is', num + 1)
# print('The previous number for the number', num, 'is', num - 1)

# Вводится число 0 или 1, необходимо вывести 1 или 0 соответственно.
# num = int(input())
# print(1 - num)

# Дано целое число N. Выведите следующее за ним четное число.

# практикум по программированию

# https://tinyurl.com/python-practice-omstu смотреть новости и лабы
# 4-21
# 24-27 + 19 изучить до следуещего занятия

# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
# Подсчитайте количество нулей среди введенных чисел и выведите это количество.
# Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
# Результат оформить в виде функции принимающей лист из N чисел, и возвращающей ответ.

# def count_zeros(num):
#     numbers = str(num)
#     num_zeroes = 0
#     for i in range(len(numbers)):
#         if numbers[i] == '0':
#             num_zeroes += 1
#     return print(num_zeroes)
# count_zeros(132654000)

# print('Введите количество чисел: ')
# N = int(input())
# kol=0
# for i in range(N):
#   print('Введите число: ')
#   n = int(input())
#   if n==0: 
#     kol+=1 
# print(kol)



