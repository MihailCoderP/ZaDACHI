# -*- coding: utf-8 -*-

def zadacha3(a):
    if len(a) <= 1:
        return a
    return a[-1] + zadacha3(a[:-1])

a = int(input('A: '))
print(zadacha3(str(a)))
