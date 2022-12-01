# -*- coding: utf-8 -*-

def zadacha6(n, d = 2):
    if n <= 2 or d ** 2 > n:
        return True
    if n % d == 0:
        return False
    return zadacha6(n, d = d + 1)

n = int(input('N: '))
print(zadacha6(n))
