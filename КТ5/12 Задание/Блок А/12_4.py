# -*- coding: utf-8 -*-

def zadacha4(n):
    if n <= 0:
        return n
    return n % 10 + zadacha4(n // 10)

n = int(input('N: '))
print(zadacha4(n))
