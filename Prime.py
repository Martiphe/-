import random

def ferma(n):
    for i in range(25):
        if pow(random.randint(2, n - 1), n-1, n) != 1:
            return False
    return rabin_miller(n)

def rabin_miller(n):
    u = n - 1
    t = 0
    while not u % 2:
        u //= 2
        t += 1
    d = []
    for i in range(t + 1):
        d.append(3**(2**i * u) % n)
        if d[i] == 1:
            if i != 0 and d[i - 1] != n - 1:
                return False
            else:
                return True
    return False



print("Введите число: ")
a = int(input())
print(ferma(a), '\n')
