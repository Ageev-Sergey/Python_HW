# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

N = int(input('Вевидите число: '))
lst = []
summ = 0
for i in range(1, 1 + N):
    lst.append((1 + 1 / i)**i)
    summ += lst[i-1]
print(lst)
print(summ)