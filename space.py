import random

class Field:
     def sum(self, a, b):
         return (a + b) % 3

     def multiply(self, c, b):
         return (c * b) % 3

X = Field()
a = random.randint(0, 2)
b = random.randint(0, 2)
c = random.randint(0, 2)

print(a, b, c)

print("Ассоциативность сложения")
h = X.sum(a, X.sum(b, c))
print(h)
p = X.sum(X.sum(a, b), c)
print(p)
print(h == p)

print("Нейтральный элемент по сложению")
h = X.sum(0, a)
print(h)
p = X.sum(a, 0)
print(p)
print(h == p)

print("Обратимость сложения")
h = X.sum(a, -a)
print(h)
p = X.sum(-a, a)
print(p)
print(h == p)

print("Коммутативность сложения")
h = X.sum(a, b)
print(h)
p = X.sum(b, a)
print(p)
print(h == p)

print("Ассоциативность умножения")
h = X.multiply(a, X.multiply(b, c))
print(h)
p = X.multiply(X.multiply(a, b), c)
print(p)
print(h == p)

print("Нейтральный элемент по умножению")
h = X.multiply(1, a)
print(h)
p = X.multiply(a, 1)
print(p)
print(h == p)

print("Коммутативность по умножению")
h = X.multiply(a, b)
print(h)
p = X.multiply(b, a)
print(p)
print(h == p)

print("Дистрибутивность")
h = X.multiply(a, X.sum(b, c))
print(h)
p = X.sum(X.multiply(a, b), X.multiply(a, c))
print(p)
print(h == p)

print("Обратимость умножения")
if a != 0:
    h = X.multiply(a, a)
    print(h)
    p = X.multiply(a, a)
    print(h == p)
print("У нуля нет обратного")

print("{0, 1, 2} - Поле\n")
