from bson import json_util, ObjectId
from flask import json
from pymongo import MongoClient

from models.Portfolio import Portfolio
from models.Profile import Profile
from models.users import User


def __get_database():
    client = MongoClient(
        "mongodb+srv://admin-jumpy:jumpyBugs2123@cryk.nnzlsve.mongodb.net/?retryWrites=true&w=majority")
    db = client.CryK
    return db


# <editor-fold desc="Portfolio">
def get_portfolio_collection():
    db = __get_database()
    return db.Portfolios


def insert_user_portfolio(portfolio: Portfolio):
    portfolios = get_portfolio_collection()
    user_portfolio = portfolios.find_one({"user_id": portfolio.user_id})
    if user_portfolio:
        portfolios.delete_one({"user_id": portfolio.user_id})
    portfolios.insert_one(json.loads(portfolio.__str__()))


def get_user_portfolio(user_id):
    portfolios = get_portfolio_collection()
    portfolio = portfolios.find_one({"user_id": user_id}, {"_id": 0, "user_id": 0})
    return -1 if portfolio is None else portfolio


# </editor-fold>

# <editor-fold desc="Users">
def get_users_collection():
    db = __get_database()
    return db.Users


def insert_user(user: User):
    users = get_users_collection()
    id = find_id_by_email(user.email)
    if id == -1:
        users.insert_one(json.loads(user.__str__()))
        return find_id_by_email(user.email)
    return id


def find_id_by_email(email):
    users = get_users_collection()
    user = users.find_one({"email": email})
    return json.loads(json_util.dumps(user.get('_id'))) if user is not None else -1


def find_account(user: User):
    users = get_users_collection()
    user = users.find_one({"email": user.email, "password": user.password})
    return json.loads(json_util.dumps(user.get('_id'))) if user is not None else -1


def is_user_in_database(user_id):
    users = get_users_collection()
    user = users.find_one({"_id": ObjectId(user_id)})
    return False if user is None else True


# </editor-fold>

# <editor-fold desc="Profile">
def get_profile_collection():
    db = __get_database()
    return db.Profiles


def get_user_profile(user_id):
    profiles = get_profile_collection()
    profile = profiles.find_one({"user_id": user_id})
    return -1 if profile is None else Profile(user_id=profile['user_id'],
                                              email=profile['email'],
                                              firstname=profile['firstname'],
                                              lastname=profile['lastname'],
                                              country=profile['country'],
                                              city=profile['city'],
                                              address=profile['address'],
                                              about=profile['about'])


def insert_user_profile(profile: Profile):
    profiles = get_profile_collection()
    user_portfolio = profiles.find_one({"user_id": profile.user_id})
    if user_portfolio:
        profiles.delete_one({"user_id": profile.user_id})
    profiles.insert_one(json.loads(profile.__str__()))

# </editor-fold>