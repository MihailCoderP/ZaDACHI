# -*- coding: utf-8 -*-

def zadacha5(a):
    print(a % 10, end = ' ')
    if a // 10 != 0:
        zadacha5(a // 10)
    print('', end = '')

n = int(input('N: '))
zadacha5(n)
