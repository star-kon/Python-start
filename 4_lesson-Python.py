#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:45:45 2022

@author: konstantinx
"""

print('задача 1')

from sys import argv
print(argv)
script_addres, first_param, second_param, third_param = argv

print("Адрес и аргументы: ", argv)
print("Выработка в часах: ", first_param)
print("Зарплата в час: ", second_param)
print("Премия: ", third_param)
try:
    print(float(first_param)*float(second_param)+float(third_param))
except ValueError:
    print('запустите заново и введите числовые положительные параметры')


print('задача 2')
init_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for i, el in enumerate(init_list[1:], 1) if el > init_list[i-1]]
print(new_list)

print('задача 3')
new_list = [i for i in range(20, 241) if (i%20 == 0 or i%21 == 0)]
print(new_list)

print('задача 4')
init_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in init_list if init_list.count(i) == 1 ]
print(new_list)

print('задача 5')
from functools import reduce

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el + el
init_list = reduce(my_func, [i for i in range(100,1001,2)])
print(init_list)



print('задача 6')
from itertools import cycle
from itertools import count
from sys import argv

script_name, first_number = argv

print("Адрес и аргументы: ", argv)
print("Первое число: ", first_number)
num_list = []
try:
    for i in count(int(first_number)):
        if i > int(first_number)+20:
            break
        num_list.append(i)
    print(num_list)

    s = 0
    for el in cycle(num_list):
        if s > 100:
            break
        print(el)
        s += int(el)
        print(s)
except ValueError:
    print('запустите заново и введите числовые целые параметры')


print('задача 7')


def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
        yield(s)

try:
    n=int(input('введите n: '))
    for el in fact(n):
        print(el)
except ValueError:
    print('запустите заново и введите числовые целые параметры')
