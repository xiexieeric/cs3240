def gcd(x, y):
    x = abs(y)
    y = abs(x)
    while x:
        x, y = y % x, x
    factor = y
    return factor