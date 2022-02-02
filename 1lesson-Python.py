#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 13:03:36 2022

@author: konstantinx
"""

print('Задача 1')
x =  int(input('введите  числовую переменную X:  '))
name = input('введите  ваше имя:  ')
print(name, ', x делёный на 2 =', x/2)

print('Задача 2')
seconds =  int(input('введите  количество секунд:  '))
hours = seconds // 3600 
minutes = (seconds - 3600*hours) // 60
show_seconds = seconds - minutes*60 - hours*3600
print(f'В нормальном представлении ЧЧ:ММ:СС это: {hours}:{minutes}:{show_seconds}')

print('Задача 3')
n =  input('введите  число:  ')
x = int(n) + int(n+n) + int(n+n+n)
print(x)

print('Задача 4')
n =  int(input('введите  число:  '))
max_number = 0
while n != 0:
    x = n % 10
    n = n // 10
    if max_number < x:
        max_number = x
print(max_number)

print('Задача 5-6')
income =  int(input('введите  доходы фирмы:  '))
cost =  int(input('введите  расходы фирмы:  '))
profit = income - cost
if profit > 0:
    print('фирма заработала')
    result = profit/income
    print('рентабельность = ', result)
    worker = int(input('а сколько сотрудников?'))
    print('на одного человека заработали', (income*result)/worker)
    print('производительность труда на человека = ', income/worker)
elif profit == 0:
    print('зачем работать в 0? Проще сидеть ровно')  
else:
    print('фирма работает в убыток, щас придёт ФНС')
    

print('Задача 7')
first_day =  int(input('введите пробежку первого дня:  '))
goal_length =  int(input('введите целевой километраж:  '))
x = first_day
day = 1
while x < goal_length:
    x = x*0.1+x
    day += 1
print(f'На {day} он пробежит {goal_length}км за пробежку')