#!/usr/bin/env python3
""" Pymongo usage module
Module creats a mongodb connection and returns all documents

Modules:
    pymongo: imports MongoDbClient

Functions:
    list_all: returns all documents in a collection
"""


def list_all(mongo_collection):
    """ Returns all documnets of collections passed as parameter

    Args:
        mongo_collection: MongoDb collection to be used

    Returns:
        list(documents): List of all documnets in mongo_collection
    """
    return mongo_collection.find()
