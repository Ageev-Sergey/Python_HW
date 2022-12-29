# def postive_fib(n):
# postive_list = [0,1]
# for i in range(n-1):
# postive_list.append(postive_list[-2]+postive_list[-1])
# return postive_list
#
# def negative_fiv(n):
# negative_list = [0,1]
# for i in range(n-1):
# negative_list.append(negative_list[-2]-negative_list[-1])
# return negative_list
#
#
# print(negative_fiv(8)[::-1] + postive_fib(8)[1:])

# 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

vulue_str = str(input("введитестроку чисел: "))
value_list = vulue_str.split(" ")
print(value_list)
for i in value_list:
    if i.isdigit():
        value_list[value_list.index(i)] = int(value_list[value_list.index(i)])
    else:
        value_list.remove(i)
print(value_list)
for i in value_list:
    i = i*2
    print(i)
print(value_list)


# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения

# 2) с помощью дополнительных библиотек Python

# 29. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
