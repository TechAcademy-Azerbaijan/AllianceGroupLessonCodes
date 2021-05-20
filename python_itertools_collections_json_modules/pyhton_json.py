import json

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
persons = {
        'ad': 'Idris',
        'city': 'Baki',
        'a': [1,2,32,3454,
        {'ad': 'Idris',
        'city': 'Baki',}
        ],
}

# print(dict(str(persons)))
print(json.dumps(persons))

s = """
{"ad": "Idris", "city": "Baki", "a": [1, 2, 32, 3454, {"ad": "Idris", "city": "Baki"}]}
"""

d = json.loads(s)
print(d)
print(type(d))
# with open('persons.json', 'w') as f:
#     json.dump(persons, f)

with open('persons.json', 'r') as f:
    data = json.load(f)
    print(data)
    print(type(data))