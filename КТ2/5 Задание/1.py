"# -- coding: utf-8 --"
   N = int(input("Введите N: "))
    counter = 1
    result = 1
    while(True):
        result = counter*counter
        counter+=1
        if(result > N):
            break
        else:
            print(f'{result}')