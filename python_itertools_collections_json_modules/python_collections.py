import collections
import itertools

# Point = namedtuple("Point", "x,y,z,d")

# point = Point(1,2,3,4)

# print(point.x)
# print(point.y)

#
# d = collections.OrderedDict()

# d['ad1'] = 'Kenan'
# d['ad2'] = 'Kamal'
# d['ad3'] = 'Kerim'
# d['ad4'] = 'Yusif'
# d['ad4'] = 'Kerim'

# print(d)

# ###########################
# s = 'sdfsdbfsbdfkbk2bjkdsbdfkjbsdkfjb12e2hiuqhwdsadij'

# d = collections.Counter(['a', 'a', 'b', 'c'])
# print(dict(d.most_common(2)).keys())
# print(d.values())

# sub = {
#     'a': 2
# }

# new_d = d.subtract(sub)
# print(new_d)

##########################

# d = collections.defaultdict(lambda: 404)

# d["a"] = 1
# d["b"] = 2
  
# print(d["a"])
# print(d["b"])
# print(d["c"])

# d = dict()
# d['a'] = 1
# d['b'] = 2

# print(d.get('a'))
# print(d.get('b'))
# print(d.get('c', 404))


# d = collections.deque()

# d.append(1)
# d.append(2)
# d.append(3)
# d.appendleft(4)
# print(d.rotate(-1))
# print(d)

# d1 = {
#     'a': 1
# }
# d2 = {
#     'a': 1,
#     'd': 2,
#     'c': 3
# }
# d = {
#     **d1,
#     **d2
# }
# d = collections.ChainMap(d1, d2)
# print(dict(d))