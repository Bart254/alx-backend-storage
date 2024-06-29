#!/usr/bin/env python3
""" Module provides stats about nginx logs stored in MongoDB
"""


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017')
    coll = client.logs.nginx

    # print x logs where x is number of documents
    print(f'{coll.count_documents({})} logs')

    # Print 5 lines with no of documents with methods
    # get, post, put, patch, delete
    print('Methods:')
    print(f'\tmethod GET: {coll.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {coll.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {coll.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {coll.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {coll.count_documents({"method": "DELETE"})}')

    # print number of documents with status path and get method
    number = coll.count_documents({"method": "GET", "path": "/status"})
    print(f'{number} status check')

    # print the top 10 visited ips
    pipeline = [
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1},
            },
        },
        {
            "$sort": {
                "count": -1
            }
        },
        {
            "$limit": 10
        }
    ]
    ips = coll.aggregate(pipeline)
    print("IPs:")
    for ip in ips:
        print(f'\t{ip["_id"]}\t{ip["count"]}')
