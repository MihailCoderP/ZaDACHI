# -*- coding: utf-8 -*-

import sys
def zadacha1():
    n = int(input())
    if n == 0:
        return -sys.maxsize - 1
    return max([n, zadacha1()])

print(zadacha1())
