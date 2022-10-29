"# -- coding: utf-8 --"
x = int(input("Введите x: "))
y = int(input("Введите y: "))
summ = x
counter = 1

while (True):
    if (summ <= y):
        x = x * 1.1
        summ = summ + x
        counter += 1
    else:
        break

print(f'На {counter} день пробег спортсмена составит не менее {y} км, а точнее {summ} км')