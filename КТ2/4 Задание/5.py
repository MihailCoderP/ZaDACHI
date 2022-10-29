"# -- coding: utf-8 --"
n = int(input('Введите n: '))
answer = 0

for i in range(1, n+1):
    answer += i ** 3

print(answer)
