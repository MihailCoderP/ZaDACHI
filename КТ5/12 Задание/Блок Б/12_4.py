# -*- coding: utf-8 -*-

def zadacha4(n, d = 2):
    if n <= 2 or d ** 2 > n:
        return True
    if n % d == 0:
        return False
    return zadacha4(n, d = d + 1)

n = int(input('N: '))
if zadacha4(n):
    print('Yes')
else:
    print('No')
