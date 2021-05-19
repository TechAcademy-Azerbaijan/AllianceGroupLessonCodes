import random
import time
import sys

# def square(my_list):
#     for i in my_list:
#         yield 

def gen_random_array(n):
    for i in range(n):
        yield random.randint(0, 10) ** 2
    
t1 = time.time()

b = gen_random_array(10000000)

print(sys.getsizeof(b))

# for i in range(100000000):
#     print(next(b))

for i in range(10000000):
    next(b)

t2 = time.time()


print(t2-t1)