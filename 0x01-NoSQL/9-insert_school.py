#!/usr/bin/env python3
""" Pymongo usage module
Module is about inserting a document

Modules:
    pymongo: imports MongoDbClient

Functions:
    insert_school: inserts a document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """ Creates mongo_collection document

    Args:
        mongo_collection: MongoDb collection to be used
        kwargs: a dictionary to insert into mongo_collection

    Returns:
        str(_id): id of the inserted document
    """
    # insert the document
    insert_object = mongo_collection.insert_one(kwargs)

    # return the id
    return insert_object.inserted_id
