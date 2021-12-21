import random

def is_prime(n):
    if n > 3:
        for i in range(25):
            if pow(random.randint(2, n - 1), n-1, n) != 1:
                return False
        return rabin_miller(n)
    else:
        return True


def rabin_miller(n):
    u = n - 1
    t = 0
    while not u % 2:
        u //= 2
        t += 1
    d = []
    d.append(3**u % n)
    if d[0] == 1 or d[0] == n - 1:
        return True
    for i in range(1, t):
        d.append(3**(2**i * u) % n)
        if d[i] != n - 1:
            return False
    return True



print("Введите число: ")
a = int(input())
print(is_prime(a), '\n')
