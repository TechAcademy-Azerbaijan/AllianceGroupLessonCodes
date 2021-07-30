import pymongo

myclient = pymongo.MongoClient('mongodb://db_user:12345@localhost:27017/mydatabase?authSource=admin')

mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = { "name": "John", "address": "Highway 37" }



x = mycol.insert_one(mydict)
print(mydb.list_collection_names())

