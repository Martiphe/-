import random

class Field:
     def __init__(self, p):
         self.p = p % 3


     def __str__(self):
         return str(self.p)


     def __add__(self, other):
         return (self.p + other.p) % 3


     def __mul__(self, other):
         return (self.p * other.p) % 3

     def __sub__(self, other):
         return (self.p - other.p) % 3


     def __truediv__(self, other):
         return (self.p / other.p) % 3




a = Field(random.randint(0, 2))
b = Field(random.randint(0, 2))
c = Field(random.randint(0, 2))
e_add = Field(0)                     # Нейтральное по сложению
e_sub = Field(1)                     # Нейтральное по умножению
print(a, b, c)


print("Ассоциативность сложения")
print(a + Field(b + c))
print(Field(a + b) + c)


print("Нейтральный элемент по сложению")
print(a + e_add)
print(e_add + a)


print("Обратимость сложения")
print(a - a)
print(a - a)


print("Коммутативность сложения")
print(a + b)
print(b + a)


print("Ассоциативность умножения")
print(a * Field(b * c))
print(Field(a * b) * c)


print("Нейтральный элемент по умножению")
print(a * e_sub)
print(e_sub * a)


print("Коммутативность по умножению")
print(a * b)
print(b * a)


print("Дистрибутивность")
print(a * Field(b + c))
print(Field(a + b) * c)


print("Обратимость умножения")
if a != 0:
   print(a * a)
   print(a * a)
print("У нуля нет обратного")


print("{0, 1, 2} - Поле\n")
