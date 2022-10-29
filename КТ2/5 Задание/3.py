"# -- coding: utf-8 --"
N = int(input("Введите N: "))
result = 1
counter = 1
while (True):
    if (result < N):
        result *= 2
        if (result > N):
            result /= 2
            counter -= 1
            break
        else:
            counter += 1
print(f'Показатель степени {result}')
print(f'Степень {counter}')