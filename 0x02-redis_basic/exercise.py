#!/usr/bin/env python3
""" Creates cache class
"""
import redis
from typing import Union


class Cache:
    """ Cache class for redis database

    Attributes:
        __redis: private instance attribute that stores redis client

    Methods:
        store: takes a data argument and returns a key
    """
    def __init__(self):
        """ stores an instance of Redis client in a private attribute
        """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generates a key and stores data passed as argument

        Args:
            data(str, byte, int, float): data to be stores in Redis

        Returns:
            key(str): key to data stored
        """
        import uuid
        key: str = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key
