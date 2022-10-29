"# -- coding: utf-8 --"
n = int(input('Введите N: '))
a, b, c = 0, 0, 1

for foo in range(n):
    b, c = b + c, b
    a += b

print(a)