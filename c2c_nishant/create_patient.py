from pymongo import MongoClient
from env import var

client = MongoClient()
client = MongoClient(var.link)
db = client['sm_medikit']

name = raw_input('Enter name : ').strip()
sex = raw_input('Enter sex : ').strip()
uid = int(input('Enter uid : '))
history = "Something"

db.pat_details.insert({"name": name, "sex": sex, "uid": uid, "history": history})
