"# -- coding: utf-8 --"
a = int(input('Введите A: '))
b = int(input('Введите B: '))

if a < b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)