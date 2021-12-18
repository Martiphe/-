import math

a = int(input("Введите число: "))
k = 1
for i in range(2, int(math.sqrt(a))):
    if not a % i:
        k = 0
        break
if k:
    print("True")
else:
    print("False")