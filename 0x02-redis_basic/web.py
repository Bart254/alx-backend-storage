#!/usr/bin/env python3
""" tracks how many times a url is visited
"""
import redis
import requests
from functools import wraps
from typing import Callable


def get_page_decorator(method: Callable) -> Callable:
    """ wrapper function"""
    @wraps(method)
    def get_url(url: str) -> None:
        """ Updates when a url is visited"""
        client = redis.Redis()
        key = f'count:{url}'
        response = method(url)
        if response.status_code == 200:
            if not client.get(key):
                client.setex(key, 10, 1)
            else:
                client.incr(key)
    return get_url


@get_page_decorator
def get_page(url: str) -> str:
    """ returns url response"""
    return requests.get(url)
