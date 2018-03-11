from pymongo import MongoClient
from env import var

client = MongoClient()
client = MongoClient(var.link)
db = client['sm_medikit']

name = raw_input('Enter name : ').strip()
password = raw_input('Enter password : ').strip()
uid = int(input('Enter uid : '))

db.doc_details.insert({"name": name, "password": password, "uid": uid})
