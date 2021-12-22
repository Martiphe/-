import random
import math

def is_prime(n):
    if n < 2:
        return False
    if n > 3:
        for i in range(25):
            if pow(random.randint(2, n - 1), n-1, n) != 1:
                return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True


print("Введите число: ")
a = int(input())
print(is_prime(a), '\n')
