import random
import time
import sys

def square(my_list):
    a = []
    for i in my_list:
        a.append(i**2)
    return a

t1 = time.time()
b = [random.randint(0, 10) for i in range(10000000)]

print(sys.getsizeof(b))
c = square(b)

t2 = time.time()

print(t2-t1)