#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 21:33:27 2022

@author: konstantinx
"""



print('задача 1')
q = '1'
with open('file.txt', 'a', encoding=('utf-8')) as f:
    while q != '0':
        f.write(input('введите значение: '))
        f.write('\n')
        q = input('для выхода нажмите 0: ')
        if q == '0':
            f.writelines(' ')

print('задача 2')
with open('file.txt', 'r', encoding=('utf-8')) as f:
    line = f.readlines()
    print('количество строк', len(line))
    for num, i in enumerate(line, 1):
        x = i.split(' ')
        print(f'в строке {num} ', len(x), ' слов')

print('задача 3')
s = 0
with open('file3.txt', 'r', encoding=('utf-8')) as f:
    line = f.readlines()
    for num, i in enumerate(line, 1):
        x = i.split(' ')
        print('x', x)
        if int(x[1]) < 20000:
            print(f'у {x[0]} зарплата меньше 20к')
        s += int(x[1])
    print('средняя з/п = ', s/num)

print('задача 4')
dictionary = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
# print(dictionary.get(i[0]))
with open('4task.txt', 'r', encoding=('utf-8')) as f:
    line = f.readlines()
    for i in line:
        i = i.split(' ')
        i[0] = dictionary.get(i[0])
        i = ' '.join(i)
        i.replace('\n', '')
        print(i, file=open("output.txt", "a"))

print('задача 5')
from random import randint
with open('5task.txt', 'w+', encoding=('utf-8')) as f:
    f.write(' '.join(str(randint(1, 100)) for i in range(1, 20)))
    f.seek(0)
    # print(result)
    result = sum(map(int, f.readline().split()))
print(result)

print('задача 6')
with open('6task.txt', 'r', encoding=('utf-8')) as f:
    data = f.readlines()
    print(data[0], type(data[0]))
    dictionary = {}
    for i in data:
        try:
            ind = i.index(':')
            new_dict = {i[:ind]: i[ind+2:].split()}
            dictionary.update(new_dict)
        except ValueError:
            pass
    print(dictionary)

print('Задача 7')
import json
with open('output_task7.json', 'w', encoding=('utf-8')) as output:
    with open('7task.txt', encoding=('utf-8')) as f:
        print(f, type(f))
        profit = {line.split()[0]:
                  int(line.split()[2])-int(line.split()[3]) for line in f}
        average_profit = sum([i for i in profit.values() if i > 0]) / \
            len([i for i in profit.values() if i > 0])

    json.dump([profit, average_profit], output, ensure_ascii=False, indent=4)
    print(average_profit)
