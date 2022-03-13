import random
import math
from numba import njit, prange, int64

@njit (fastmath=True)

def is_prime(n):
    if n < 2:
        return False
    if n > 3:
        for i in prange(25):
            if random.randint(2, n - 1)**(n-1) % n != 1:
                return False
        for i in prange(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True
