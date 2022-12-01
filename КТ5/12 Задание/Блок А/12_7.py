# -*- coding: utf-8 -*-

def zadacha7(a, b, s = 1):
    if a == b:
        return
    print(a)
    zadacha7(a + s * (-1 if max([a, b]) == a else 1), b, s)

a = int(input('A: '))
b = int(input('B: '))
zadacha7(a, b)
    