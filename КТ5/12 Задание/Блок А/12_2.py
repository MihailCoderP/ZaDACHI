# -*- coding: utf-8 -*-

def zadacha2(a, b):
    if a < b:
        return a
    return zadacha2(a - b, b)

a = int(input('A: '))
b = int(input('B: '))
print(zadacha2(a, b))

