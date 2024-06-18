#!/usr/bin/env python3
""" Pymongo usage module
Module is about finding a document

Modules:
    pymongo: imports MongoDbClient

Functions:
    schools_by_topic: finds a document in a collection
"""


def schools_by_topic(mongo_collection, topic):
    """ returns list of schools having a specific topic

    Args:
        mongo_collection: MongoDb collection to be used
        topic: the topic to be searched in the document
    """
    return mongo_collection.find({"topics": topic})
