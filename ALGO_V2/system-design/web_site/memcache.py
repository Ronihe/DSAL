# https://www.lintcode.com/problem/memcache/description?_from=ladder&&fromId=75
"""
memcache: https://memcached.org/
in-memory key-value store for small chunks of arbitrary data

"""


class CacheNode:
    def __init__(self, value, expired):
        self.value = value
        self.expired = expired


INT_MAX = 0x7ffffff


class Memcache:
    def __init__(self):
        # init the data structure here
        self.client = {}

    def get(self, curr_time, key):
        """

        Args:
            curr_time: integer
            key: integer

        Returns: integer

        """
        if key not in self.client:
            return
        return INT_MAX


memcache = Memcache()
memcache.get(12, 23)
