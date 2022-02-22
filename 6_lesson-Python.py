#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 18:16:40 2022

@author: konstantinx
"""

print('задача 1')

class Traficlight:


    def running(self):
        from itertools import cycle
        from time import sleep
        __color = [' green ',' yellow ','  red  ']
        for i in cycle((0,1,2)):
            print(f"\r light: {__color[i]}", end='')
            if i == 0 or i == 2:
                sleep(7)
            else:
                sleep(2)


this_light = Traficlight()
print(this_light.running())

print('задача 2')

class Road:

    def mass(length, width):
        _weight = 25
        _depth = 5
        try:
            return (length*width*_weight*_depth/1000)
        except ValueError:
            print('введите числовые значения длины и ширины')
            exit()

length = float(input('введите длинну дороги в метрах: '))
width = float(input('введите ширину дороги в метрах: '))
mass = Road.mass(length, width)
print(f'Нужная масса асфальта {mass} тонн')

print('задача 3')


class Worker:
    def __init__(self, name='Антон', 
                 surname='Сидоров', position='Инженер', wage=100):
        self.name = name
        self.surname = surname
        self.position = position
        _income = wage
        _income[f"{position}-бонус"] = _income[f"{position}-оклад"]*0.3
        self._income = _income


class Position(Worker):
    def get_full_name(self):
        return (f'{self.position}  {self.name} {self.surname}')

    def get_total_income(self):
        total_incom = (
            self._income[f"{position}-бонус"] + 
            self._income[f"{position}-оклад"])
        return (total_incom)


name = input('введите имя: ')
surname = input('введите фамилию: ')
position = input('введите название должности: ')
wage = {f"{position}-оклад": float(input('введите оклад: '))}
worker = Worker(name, surname, position, wage)
print(worker)
print(Position.get_full_name(worker))
print(Position.get_total_income(worker))

# =============================================================================
# print('задача 4')
# class Car:
#     direction = 'forward'
#     
#     def __init__(self, speed, color, name, is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#     
#     def go(self):
#         if speed>0:
#             return(f'движется со скоростью {speed}')
#     def stop(self):
#         if speed == 0:
#             return('стоит')
#     def turn(self, direction):
#         return(f'{direction}')
#     def ShowSpeed(self):
#         return(speed)
#     
# class TownCar(Car):
#     if speed > 60:
#         def ShowSpeed(self):
#             return(f'{speed}, помедленнее!')
#     return (self.name, go, stop, speed)
# 
# class SportCar(Car):
#     #return ()
#     
# class WorkCar(Car):
#      if speed > 40:
#         def ShowSpeed(self):
#             return(f'{speed}, помедленнее!')
# 
# class PoliceCar(Car):   
#     pass
# 
# print(TownCar(30, 'black', 'mazda'))
# =============================================================================

print('задача 5')
class Stationery:
    def __init__(self, title):
        self.title = title
        print(title)
    def draw(self):
        return('запуск отрисовки')
    
class Pen(Stationery):  
    def draw(self):
        return('запуск отрисовки ручкой')
    
class Pencil(Stationery):  
    def draw(self):
        return('запуск отрисовки карандашом')

class Handle(Stationery):  
    def draw(self):
        return('запуск отрисовки маркером')
    
print(Pen.draw('pen'))   
print(Pencil.draw('pencil'))  
print(Stationery.draw('p')) 