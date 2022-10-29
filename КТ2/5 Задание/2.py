"# -- coding: utf-8 --"
number = int(input("Введите число НЕ меньше 2: "))
count = 2
while (True):
    if (number % count != 0):
        count += 1
    else:
        print(f'Наименьший натуральный делитель для числа {number} это {count}')
        break