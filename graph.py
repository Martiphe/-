#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  # Импорт из бибилиотеки 'math'
import numpy  # Импорт из бибилиотеки 'numpy'
import matplotlib.pyplot as mpp # Импорт из бибилиотеки 'matplotlib.pyplot' и присвоил название 'mpp' библиотеке 'matplotlib.pyplot'

# Эта программа рисует график функции, заданной выражением ниже''
if __name__=='__main__':  # проверяет, что модуль был запущен интерпретатором, а не импортирован
    arguments = numpy.arange(0, 200, 0.1)  # присваивает переменной "arguments" массив значений от 0 (включая) до 200 (не включая) с шагом 0.1
    mpp.plot(  # построение графика
        arguments, # аргумент функции принимает значения переменой "arguments"
        [math.sin(a) * math.sin(a/20.0) for a in arguments]  # значения функции для каждого значения аргумента из массива "arguments" задаются уравнением sin(a)*sin(a/20), где a принимает все значения переменной "arguments"
    )
    mpp.show() # Показать график


