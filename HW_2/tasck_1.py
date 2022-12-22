# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11
value = float(input("Ведите число: "))
value = str(value)
summ = 0
for i in value:
    print(i)
    if i.isdigit():
        i = int(i)
        summ += i
print(summ)
