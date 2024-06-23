#!/usr/bin/env python3
""" Sorts a list of students depending on score
"""


def top_students(mongo_collection):
    """ Function uses aggregate pipeline to sort list of students

    Args:
        mongo_collection(Collection object): collection to be sorted

    Returns:
        Cursor object: containing sorted documents
    """
    pipeline = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$_id",
                "averageScore": {"$avg": "$topics.score"},
                "name": {"$addToSet": "$name"}
            }
        },
        {
            "$sort": {
                "averageScore": -1
                }
        },
        {
            "$project": {
                "_id": 1,
                "averageScore": 1,
                "name": {"$first": "$name"}
            }
        }
    ]
    return mongo_collection.aggregate(pipeline)
