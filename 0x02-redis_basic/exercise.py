#!/usr/bin/env python3
""" Creates cache class
"""
import redis
from typing import Union, Optional, Callable, List, Dict
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ function decorator"""
    @wraps(method)
    def incr(self, *args: List, **kwargs: Dict) -> Callable:
        """ increments count for func key"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return incr


def replay(method: Callable):
    """ Accepts function as a parameter and prints an output to display its
    parameters, number of times called and outpus
    """
    # create redis client
    client = redis.Redis()

    name = method.__qualname__
    inputs = client.lrange(f'{name}:inputs', 0, -1)
    outputs = client.lrange(f'{name}:outputs', 0, -1)
    # print number of times method was called
    nb = client.get(name)
    nb = nb.decode("utf-8")
    print(f'{name} was called {nb} times:')

    # print the inputs and outputs
    for input, output in zip(inputs, outputs):
        input = input.decode("utf-8")
        output = output.decode("utf-8")
        print(f'{name}(*{input}) -> {output}')


def call_history(method: Callable) -> Callable:
    """ A decorator function that stores inputs and outputs to a method
    """
    @wraps(method)
    def queue_history(self, *args: List, **kwargs: Dict):
        """ adds input and output to the end of a list
        """
        input_key: str = method.__qualname__ + ":inputs"
        output_key: str = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return queue_history


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

    @call_history
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
