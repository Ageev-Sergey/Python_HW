# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.

import random

N = int (input('введите N: '))
lis =[]
for i in range(N):
    lis.append(random.randrange(-N,N+1))
print(lis)

result =1
numbers = 'file.txt'
with open(numbers, 'r') as data:
    result = lis[int(data.readline())] * lis[int(data.readline())]
print(result)
