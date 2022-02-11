#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 21:44:29 2022

@author: konstantinx
"""


def correct_input(*args):
    """предполагалось, что можно сделать единую 
    проверку корректности ввода,  но не срослось"""
    for i in args[1:]:
        print(type(i), args[0])
        if type(i) == args[0]:
            return True
        else:
            return False


print('Задача 1')
def division(x, y):
    """функция деления с исключением деления на 0"""
    try:
        return round((x/y), 3)
    except ZeroDivisionError:
        return ('Ну около бесконечности, если делитель около нуля')


print(division(int(input("введите делимое ")),
                int(input("введите делитель "))))

print('Задача 2')


def dannie_users(name='не указан', surname='не указан', birth='не указан',
                 city='не указан', email='не указан', phone='не указан'):
    """функция выдаёт принятые значения одной строкой"""
    return (' '.join([name, surname, birth, city, email, phone]))

print(dannie_users(name=input('имя '), surname=input('фамилия '),
                   city=input('город проживания '),
                   birth=input('дата рождения '), email=input('почта '),
                   phone=input('телефон ')))

print('Задача 3')

def my_func(x, y, z):
    """функция складывает два наибольших значения из принятых трёх"""
    result = [x, y, z]
    result.remove((min(result)))
    return (sum(result))

try:
    x = float(input('введите число '))
    y = float(input('введите число '))
    z = float(input('введите число '))
    print(my_func(x, y, z))

except ValueError:
    """исключение, если ввели не цифры"""
    print('попробуйте ещё раз, введите просто цифры')


print('Задача 4')
def stepen(x, y):
    """возводит Х в отрицательную степень У"""
    result = 1
    for i in range(abs(y)):
        result *= x
    result = 1/result
    return(result)


try:
    x = float(input('введите число '))
    y = int(input('введите число отрицательной степени '))
    if y < 0:
        print(stepen(x, y))
    else:
        print('вообще сработает и так, но введите второе число отрицательным')

except ValueError:
    print('попробуйте ещё раз, введите просто цифры')



print('Задача 5')

def splitter(string):
    """эта функция убирает лишние пробелы"""
    while '  ' in string:
        print('внутренний цикл', string)
        string = string.replace('  ', ' ')
    return(string.split(' '))


def clearer(splited_list):
    """ эта функция убирает все нечисловые значения из списка, 
    а также обрезает список после символа q"""
    for i, el in enumerate(splited_list):
        try:
            x = int(el)
            print('x', x)
        except ValueError:
            if el != 'q':
                splited_list.pop(i)
                print('!=q')
            elif el == 'q':
                print('==q')
                splited_list = splited_list[:i]
                return(splited_list)
    return(splited_list)


my_list = ''
result = 0

"""основное тело программы, складывающей введённые целые числа"""
while 'q' not in my_list:
    print('для выхода введите q')
    my_list = input('вводите числа через пробел и нажмите enter ')
    splited_list = splitter(my_list)
    cleared_list = clearer(splited_list)
    result = sum(map(int, cleared_list))+result

print(result)


print('задача 6-7')

def capitalizer(my_list):
    """функция делает прописными первые буквы слов,
    состоящих из строчных латинских символов. 
    При иных вводах поднимает исключения"""
    for i in my_string:
        if (ord(i) >97 and ord(i) < 123) or i == ' ':
            continue
        elif i == '1':
            return('1')
        else:
            print()
            return('надо ввести строчные буквы на латинице ')
        
    return(my_list.title())
        

my_string = ''
while '1' not in my_string:
    print('для выхода введите 1')
    my_string = input('вводите слово маленькими буквами на латинице ')
    my_string = capitalizer(my_string)
    print(my_string)

