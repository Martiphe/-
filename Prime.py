x = int(input('Введите число: '))

import random

def prime(n):
    if 2**(n-1) % n == 1:
        return True
    else:
        return False

print(prime(x))

