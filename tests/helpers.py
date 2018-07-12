from pymongo import MongoClient


def purge_db():
    c = MongoClient()
    c.db.links.delete_many({})
    c.close()


def insert_in_db(link_object):
    c = MongoClient()
    c.db.links.insert_one(link_object)
    c.close()
