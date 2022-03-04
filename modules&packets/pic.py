import os
import prime

a = int(input("Введите число: "))

if prime.is_prime(a) is True:
    os.startfile(r'C:\Users\artem\PycharmProjects\pythonProject1\p1.jpg')
else: os.startfile(r'C:\Users\artem\PycharmProjects\pythonProject1\p2.jpg')
