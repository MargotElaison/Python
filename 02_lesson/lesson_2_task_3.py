import math


def square(side):
    return math.ceil(float(side)) ** 2


result = square(input("Введите сторону квадрата: "))
print("Площадь квадрата равна", result)
