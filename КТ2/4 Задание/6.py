"# -- coding: utf-8 --"
digit = int(input('Введите n: '))
fact = 1

for i in range(2, digit+1):
    fact *= i

print(fact)