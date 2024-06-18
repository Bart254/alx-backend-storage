#!/usr/bin/env python3
""" Pymongo usage module
Module is about updating a document

Modules:
    pymongo: imports MongoDbClient

Functions:
    update_topics: updates a document in a collection
"""


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document based on the name

    Args:
        mongo_collection: MongoDb collection to be used
        name(string): name of the document
        topics(list of strings): the topics to be updated in the document
    """
    # update document matching the name description
    mongo_collection.update_many({"name": name}, {$set: {"topics": topics}})
