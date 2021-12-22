import random

class Field:
     def __init__(self, p):
         self.p = p % 3


     def __str__(self):
         return str(self.p)


     def __add__(self, other):
         return Field(self.p + other.p)


     def __mul__(self, other):
         return Field(self.p * other.p)


     def __sub__(self, other):
         return Field(self.p - other.p)


     def __truediv__(self, other):
         if other.p != 0:
             return Field(self.p * other.p)
         else: return 'Делить на нуль нельзя'




a = Field(random.randint(0, 2))
b = Field(random.randint(0, 2))
c = Field(random.randint(0, 2))
e_add = Field(0)                     # Нейтральное по сложению
e_sub = Field(1)                     # Нейтральное по умножению
print(a, b, c)


print("Ассоциативность сложения")
print(a + (b + c))
print((a + b) + c)


print("Нейтральный элемент по сложению")
print(a + e_add)
print(e_add + a)


print("Обратимость сложения")
print(a - a)


print("Коммутативность сложения")
print(a + b)
print(b + a)


print("Ассоциативность умножения")
print(a * (b * c))
print((a * b) * c)


print("Нейтральный элемент по умножению")
print(a * e_sub)
print(e_sub * a)


print("Коммутативность по умножению")
print(a * b)
print(b * a)


print("Дистрибутивность")
print(a * (b + c))
print(a*b + a*c)


print("Обратимость умножения")
print(a / a)


print("{0, 1, 2} - Поле\n")


