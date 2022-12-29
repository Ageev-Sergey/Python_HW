# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from math import pi

d = float(input("Введите число для заданной точности числа Пи: "))
i = d
value_for_round = 0
while i < 1:
    i *= 10
    value_for_round += 1

print(f'число Пи c заданной точностью {d} равно {round(pi, value_for_round)}')
