# -*- coding: utf-8 -*-

def zadacha1(x, n, x0 = 0):
    if x0 == 0:
        x0 = x
    if n == 1:
        return x
    return zadacha1(x * x0 / n, n - 1, x0 = x)

x = int(input('X: '))
n = int(input('N: '))
print(zadacha1(x, n))
