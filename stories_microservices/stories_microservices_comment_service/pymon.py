import pymongo

myclient =

mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = {"name": "John", "address": "Highway 37" }



x = mycol.insert_one(mydict)
print(mydb.list_collection_names())

