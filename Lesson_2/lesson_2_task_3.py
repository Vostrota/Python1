import math
def square(a):
    s = a * a
    if s % 1 == 0:
        print("Площадь квадрата равна:", s)
    else:
        print("Площадь квадрата равна:", math.ceil(s))

a = float(input("Введите сторону квадрата: "))
square(a)
