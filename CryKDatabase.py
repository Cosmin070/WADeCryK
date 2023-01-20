from pymongo import MongoClient


def __get_database():
    client = MongoClient(
        "mongodb+srv://admin-jumpy:jumpyBugs2123@cryk.nnzlsve.mongodb.net/?retryWrites=true&w=majority")
    print(client.list_database_names())
    db = client.CryK
    return db


def get_users_collection():
    db = __get_database()
    return db.Users


# users_collection = get_database()
    # users = collection.find()
    # user_1 = collection.find({"username": "testJumpy"})
    # collection.insert_one({"email": "test@gmail.com", "password": "somepass"})
    # for result in collection.find():
    #     print(str(result))