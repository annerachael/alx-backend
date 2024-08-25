#!/usr/bin/python3
""" LRU Caching """

from base_caching import BaseCaching
from typing import Dict, Optional, Any

class LRUCache(BaseCaching):
    """class LRU Caching"""

    def __init__(self):
        """Initializing LRU Cache"""
        super().__init__()
        self.order = []

    def put(self, key: Any, item: Any)->None:
        """Method to put item on cache"""

        if key is None or item is None:
            return 

        self.cache_data[key] = item

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.order:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))
        
        if key not in self.order:
            self.order.append(key)

        else:
            if self.order[-1] != key:
                self.order.remove(key)
                self.order.append(key)


    def get(self, key: Any)->Optional[Dict]:
        """returns value of cache dictionary"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data
    

