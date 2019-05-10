from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient(
        "mongodb+srv://ayusintyaadewi:sintya2203*@cluster0-mdyzg.gcp.mongodb.net/test?retryWrites=true")

db = client.mahasiswa
collection = db.mahasiswa
cursor = collection.find({})

for mahasiswa in cursor:
    print(dumps(mahasiswa))
    print("\n")