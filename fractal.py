import turtle as tl

def f(n):
    tl.forward(n)
    tl.left(75)
    tl.forward(n)
    tl.right(10)
    f(n+0.2)

tl.shape('turtle')
tl.speed(10000000000000)
tl.pensize(2)
n=0.1

f(n)

tl.done()
