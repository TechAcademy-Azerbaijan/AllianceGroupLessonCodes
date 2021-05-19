import random

b = (random.randint(0, 10) for i in range(10000000))

print(next(b))
print(next(b))
print(next(b))
print(next(b))
