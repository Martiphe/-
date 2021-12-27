import math
import matplotlib.pyplot as plt
import numpy as np

ITERATIONS = 35

x1 =np.arange(0, 25, 0.1)

def my_cos(x):

    x_pow = 1
    sign = 1
    partial_sum = 1
    for n in range(1, ITERATIONS):
        x_pow *= x ** 2
        sign *= -1
        partial_sum += x_pow * sign/math.factorial(2*n)

    return partial_sum


help(math.cos)
help(my_cos)

print(math.cos(0.2))
print(my_cos(0.2))

a = np.cos(x1)
plt.subplot(121)
plt.plot(x1, a, color = 'r', label = '$cos(x)$')

vs = np.vectorize(my_cos)
print(my_cos, vs)

angles = np.r_[0:25:0.01]
plt.subplot(122)
plt.plot(angles, vs(angles), color = 'g', label = 'Мой $cos(x)$')

plt.legend()
plt.show()