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
                "_id": {"id": "$_id", "name": "$name"},
                "averageScore": {"$avg": "$topics.score"},
            }
        },
        {
            "$sort": {
                "averageScore": -1
                }
        },
        {
            "$project": {
                "_id": "$_id.id",
                "averageScore": 1,
                "name": "$_id.name"
            }
        }
    ]
    return mongo_collection.aggregate(pipeline)
