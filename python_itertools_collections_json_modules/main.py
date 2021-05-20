import itertools

# counter = itertools.count()

# my_list = ['Idris', "Kenan", "Sebuhi"]

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# print(list(zip(itertools.count(start=1, step=2),my_list)))

# for i in itertools.count():
#     print(i)



#########################################
# my_list = [1,2,3,4,5,6]
# c = itertools.count()
# r = itertools.repeat(5)

# print(list(map(pow, my_list, c)))

# print(list(map(pow, my_list, r)))


##################
# cycle = itertools.cycle(['On', 'Off'])

# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))

################

a = ["A", "B", "C", "D"]
b = [1,2,3,4,5]
# comb = itertools.permutations(a, 2)
# print(comb)
# for i in comb:
#     print(i)
# c = itertools.chain(a, b, )
# for i in c:
#     print(i)
# comb = itertools.product(c, repeat=3)
# print(comb)
# for i in comb:
#     print(i)

# names = ["Subhan", "Murad", "Sebuhi", "Nurhan", "Gendab"]
# is_worked_list = [True, True, False, True]

# c = itertools.compress(names, is_worked_list)
# print(list(c))


###########
# import operator

# my_list = 1,2,3,4,5
# print(type(my_list))
# print(list(itertools.accumulate(my_list, operator.mul)))

###########

# def group_by_city(person):
#     return person['city']


# persons = [
#     {
#         'ad': 'Idris',
#         'city': 'Baki',
#     },
#     {
#         'ad': 'Tural',
#         'city': 'Gence',
#     },
#     {
#         'ad': 'Ferhad',
#         'city': 'Gence',
#     },
#     {
#         'ad': 'Eli',
#         'city': 'Sirvan',
#     },
#     {
#         'ad': 'Murad',
#         'city': 'Sirvan',
#     },
#     {
#         'ad': 'Idris2',
#         'city': 'Baki',
#     },
# ]

# new_persons = sorted(persons, key=lambda person : person['city'],)

# city_users = itertools.groupby(new_persons, lambda person : person['city'], )

# for city, users in city_users:
#     print(city)
#     for user in users:
#         print(user)


#############


