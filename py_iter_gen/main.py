# class PowTwo:

#     def __init__(self, max):
#         self.max = max

#     def __iter__(self):
#         self.a = 0
#         return self

#     def __next__(self):
#         if self.a < self.max:
#             x = self.a ** 2
#             self.a += 1
#             return x
#         raise StopIteration

# a = PowTwo(6)
# i_array = iter(a)
# while True:
#     try:
#         print(next(i_array))
#     except StopIteration:
#         print('Dovr bitti')
#         break

    
for i in PowTwo(6):
    print(i)


###

# i_array = iter(a)

# print(next(i_array))
# print(next(i_array))
# print(next(i_array))
# print(next(i_array))
# print(next(i_array))
