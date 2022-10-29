"# -- coding: utf-8 --"
in_digit = int(input('Введите n: '))
ready = 0
foo = 1

for i in range(1, in_digit + 1):
    foo = foo * i
    ready += foo

print(ready)