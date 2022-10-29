"# -- coding: utf-8 --"
level_digit = int(input('Введите n: '))

for i in range(1, level_digit+1):
    for y in range(i):
        print(i, sep='', end='')
    print()