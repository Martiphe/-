import os
import prime

a = int(input("Введите число: "))

if prime.is_prime(a) is True:
    os.startfile(r'p1.jpg')
else: os.startfile(r'p2.jpg')
