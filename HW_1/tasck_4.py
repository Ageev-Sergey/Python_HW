# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

value = int(input("Введите значение четверти: "))
if value == 1:
    print("x = from 1 to positive infinity \ny = from 1 to positive infinity")
elif value == 2:
    print("x = from -1 to negative infinity \ny = from 1 to positive infinity")
elif value == 3:
    print("x = from -1 to negatine infinity \ny = from -1 to negative infinity")
elif value == 4:
    print("x = from 1 to positive infinity \ny = from -1 to negative infinity")
else:
    print("x и y должны быть равны от 1 до 4!")
