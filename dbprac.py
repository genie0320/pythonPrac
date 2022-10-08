from pymongo import MongoClient
client = MongoClient(
    'mongodb+srv://genie:sparta@cluster0.blce7zu.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

db.users.delete_one({'name': 'bob'})

people = list(db.users.find({}, {'_id': False}))

print(people)
