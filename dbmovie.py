from pymongo import MongoClient
client = MongoClient(
    'mongodb+srv://genie:sparta@cluster0.blce7zu.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


db.movies.update_one({'title': '시월애'}, {'$set': {'star': "0"}})

print(db.movies.find_one({'title': '시월애'})['star'])
