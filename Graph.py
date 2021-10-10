Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Graph.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math                        #  импорт бибиотеки math
import numpy                       #  импорт библиотеки numpy
import matplotlib.pyplot as mpp    #  импорт модуля pyplot из matlplotlib и присвоение ему имени mpp

if __name__=='__main__':           #  проверяет, что модуль был запущен напрямую интерпритаором, а не импортирован.
    arguments = numpy.arange(0, 200, 0.1) #  присваивает переменной "arguments" массив значений от 0 (включая) до 200 (не включая) с шагом 0.1
    mpp.plot(                      #  построение графика №1
        arguments,                 #  аргумент функции принимает значения переменой "arguments"
        [math.sin(a) * math.sin(a/20.0) for a in arguments],#  значения функции для каждого значения аргумента из массива "arguments" задаются уравнением sin(a)*sin(a/20), где a принимает все значения переменной "arguments"
        color='orange',            #  задать оранжевый цвет графика №1
        label = 'sin(x)*six(x/20)' #  имя графика №1
    )
    mpp.plot(                      #  построение графика №2
        arguments,                 #  аргумент функции принимает значения переменой "arguments"
        [ math.cos(a/6) * math.log(a+1, 10)/1.3 for a in arguments], #  значения функции для каждого значения аргумента из массива "arguments" задаются уравнением cos(x/6)*lg(x+1), где а принимает все значения переменной "arguments"
        color='purple',            #  задать фиолетовый цвет графика №2
        label = 'cos(x/6)*lg(x+1)' #  имя графика №2
    )
    mpp.xlabel('x', fontsize=15)   #  подписать ось абсцисс
    mpp.ylabel('y', fontsize=15)   #  подписать ось ординат
    mpp.grid(True, which='major', color='grey', linestyle='dashed') #  задать сетку
    mpp.legend(fontsize = 10,      #  задать легенду
          ncol = 2,                #  количество столбцов
          facecolor = '#f8f8ff',   #  цвет области
          edgecolor = 'black',     #  цвет крайней линии
          title = 'Кривые',        #  заголовок
          title_fontsize = '10')   #  размер шрифта заголовка
    mpp.show()                     #  показать график