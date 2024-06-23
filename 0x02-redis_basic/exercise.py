#!/usr/bin/env python3
""" Creates cache class
"""
import redis
from typing import Union, Optional, Callable, List, Dict
from functools import wraps


def count_calls(func: Callable) -> Callable:
    """ function decorator"""
    @wraps(func)
    def incr(self, *args: List, **kwargs: Dict) -> Callable:
        """ increments count for func key"""
        key = func.__qualname__
        self._redis.incr(key)
        return func(self, *args, **kwargs)
    return incr


class Cache:
    """ Cache class for redis database

    Attributes:
        _redis: private instance attribute that stores redis client

    Methods:
        store: takes a data argument and returns a key
    """
    def __init__(self):
        """ stores an instance of Redis client in a private attribute
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generates a key and stores data passed as argument

        Args:
            data(str, byte, int, float): data to be stores in Redis

        Returns:
            key(str): key to data stored
        """
        import uuid
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[
     Union[str, bytes, int]]:
        """ Returns data from redis

        Args:
            key(str): key of data in redis
            fn(Callable): function to covert byte str to required type

        Returns:
            Union[str, bytes, int]: value returned from redis
        """
        value: Optional[bytes] = self._redis.get(key)
        if not value or not fn:
            return value
        return fn(value)

    def get_str(self, key: str) -> Union[str, bytes, int, None]:
        """ Passes str function to get method"""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Union[str, bytes, int, None]:
        """ Passes int function to get method"""
        return self.get(key, int)
