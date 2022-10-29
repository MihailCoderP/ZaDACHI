"# -- coding: utf-8 --"
len_char = 0
summ = 0
while (True):
    count = int(input("Введите целое неотрицательное число или введите 0, чтобы завершить программу: "))
    if (count != 0):
        summ = summ + count
        len_char += 1
    else:
        print(f'Среднее значение элементов последовательности: {summ / len_char}')
        break