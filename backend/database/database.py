from pymongo import MongoClient

mongo = None
db = None


def init_db(app):
    global mongo
    global db

    mongo = MongoClient(app.config["MONGO_URI"])

    db = mongo[app.config["DATABASE_NAME"]]


def get_db():
    return db