def fact(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def gcd(a, b):
    if a and b == 0:
        return 0
    elif a == 0:
        return abs(b)
    elif b == 0:
        return abs(a)
    else:
        while b != 0:
            a, b = b, a % b
        return a
