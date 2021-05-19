from functools import reduce

def square(element):
    yield element**2


def is_even(element):
    return not element % 2
    # if element%2 == 0:
    #     return True
    # return False

array = [4,5,6,7,8,9,10,11]
b = list(map(lambda x : x+1, array))

print(b)

cut_ededler = list(filter(lambda a : not a%2, b))
print(cut_ededler)

# def sum_of_numbers(a, b):
#     # print(a, b)
#     return a + b

s = reduce(lambda x,y : x+y, cut_ededler)

print(s)

# print(next(b))
# print(next(b))
# print(next(b))

