from bson import json_util
from flask import json
from pymongo import MongoClient

from models.users import User


def __get_database():
    client = MongoClient(
        "mongodb+srv://admin-jumpy:jumpyBugs2123@cryk.nnzlsve.mongodb.net/?retryWrites=true&w=majority")
    print(client.list_database_names())
    db = client.CryK
    return db


def get_users_collection():
    db = __get_database()
    return db.Users


def insert_user(user: User):
    users = get_users_collection()
    id = find_id(user.email)
    if id == -1:
        users.insert_one(json.loads(user.__str__()))
        return find_id(user.email)
    return id


def find_id(email):
    users = get_users_collection()
    user = users.find_one({"email": email})
    return json.loads(json_util.dumps(user.get('_id'))) if user is not None else -1
