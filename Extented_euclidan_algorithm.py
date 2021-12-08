def gcd(a, b, x, y):
    if a == 0:
        x = 0
        y = 1
        return b, x, y

    x1 = 0
    y1 = 0
    d, x1, y1 = gcd(b % a, a, x1, y1)
    x = y1 - int(b / a) * x1
    y = x1
    return d, x, y

print("Введите a и b: ")
a = int(input())
b = int(input())
d, x, y = gcd(a, b, 0, 0)
if y < 0:
    y = "(" + str(y) + ")"
print(d, " = ", x, " * ", a, " + ", y, " * ", b)
