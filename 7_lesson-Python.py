#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


"""
Created on Tue Feb 22 20:16:52 2022

@author: konstantinx
"""


print('Задача 1')

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        matrix = ' '+str('\n '.join(['\t '.join([str(i) for i in n]) for n in self.data]))
        return(matrix)

    def __add__(self, other):
        #print('данные', self.data, '\n', other.data)
        result = Matrix(map(lambda a, b: map(lambda x, y: x + y, a, b), self.data, other.data))
        return result

m1 = [[3, 5, 8, 3], [8, 3, 7, 1]]
m2 = [[1,2,3,8], [4,5,6,7]]
data1=Matrix(m1)
data2=Matrix(m2)
print(data1)
s=data1+data2
print('===============')
print(data2)
print('===============')
print(s)



print('Задача 2')


class Clothes(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def spending(self):
        pass


class Coat(Clothes):
    
    def spending(self, size):
        spend = round(size/6.5 + 0.5, 3)
        return (spend)
    
    @property
    def coat_spend(self):
        coat_spend = self.spend
        return(self.coat_spend)


class Costum(Clothes):
    def spending(self, height):
        return(round(height*2 + 0.3, 3))


x = Coat.spending(0, 48)
y = Costum.spending(0, 48)
print(x, y)

# =============================================================================
# print('Задача 3')
# 
# class Cito:
#     def __init__(self, number):
#         self.number = '#'*number
#         print(self.number)
# 
#     def __add___(self, other):
#         result = Cito(self.number+other.number)
#         return(result)
#     
# x = 23
# y = 23
# x = Cito(23)
# y = Cito(23)
# a = x+y
# print(a)
# 
# =============================================================================
