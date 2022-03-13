import time
import os, sys, subprocess
import prime

time_1 = time.time()
a = int(input("Введите число: "))

def open_file(file):
    if sys.platform == "win32" or "win64":
        os.startfile(file)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, file])

if prime.is_prime(a) is True:
    open_file(r'p1.jpg')
else:
    open_file(r'p2.jpg')

print(time.time() - time_1)