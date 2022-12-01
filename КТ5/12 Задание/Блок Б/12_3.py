# -*- coding: utf-8 -*-

def zadacha3(c = 0, nums = []):
    n = int(input())
    if n != 0:
        c += 1
        if c & 1:
            nums.append(n)
        zadacha3(c, nums)
    else:
        for num in nums:
            print(num)

zadacha3()
