"# -- coding: utf-8 --"
counter = 0
iteration = 1
max = 0
while (True):
    current_number = int(input("Введите целое неотрицательное число или введите 0, чтобы завершить программу: "))
    if (current_number != 0):
        if (iteration == 1):
            prev_number = current_number
            iteration += 1
            continue
        else:
            if (current_number == prev_number):
                counter += 1
                iteration += 1
                prev_number = current_number
            else:
                if (counter > max):
                    max = counter + 1
                counter = 0
                prev_number = current_number
    else:
        print(f'Количество элементов последовательности, больше предыдущего элемента: {max}')
        break