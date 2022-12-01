# -*- coding: utf-8 -*-

import sys
def zadacha2():
    n = int(input())
    if n == 0:
        return [-sys.maxsize - 1]
    return sorted([n] + zadacha2())

print(zadacha2()[-2])
