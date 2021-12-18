import random

def ferma(n):
    if n > 2:
        for i in range(25):
            a = random.randint(2, n - 1)
            if pow(a, n-1, n) != 1:
                return False
    return True

print("Введите число: ")
a = int(input())
print(ferma(a))
