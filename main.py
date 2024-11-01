import math

#
def find_roots(a, b, c):
    if a == b == c == 0:
        raise ValueError("Все коэффициенты равны нулю")

    if a == 0:
        raise ValueError("Коэффициент a не может быть равен нулю")

    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)
        return root1, root2
