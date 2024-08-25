#!/usr/bin/python3
""" LIFO Caching """

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """class LIFO Caching"""

    def __init__(self):
        """Initializing LIFO Cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Method to put item on cache"""

        if key is None or item is None:
            return 

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            
            lifo_key = self.order.pop()
            del self.cache_data[lifo_key]
            print("DISCARD: {}".format(lifo_key))
        
            self.order.append(key)
            self.cache_data[key] = item


    def get(self, key):
        """returns value of cache dictionary"""

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data

