import random

def Random_list():
    N = int(input('введите длину массива N: '))
    lst = []
    for i in range(N):
        lst.append(random.randint(-10, 10))
    return lst

def Fibonacci_numbers(value):
    if value == 0:
        return 0
    elif value == 1:
        return [-1, 0, 1]
    else:
        otvet = [-1, 0, 1]
        i = 2
        while i < (value)*2:
            otvet.append(otvet[i]+otvet[i-1])
            otvet.insert(0, (otvet[i]+otvet[i-1])*(-1))
            i += 2
        return otvet
