#!/usr/bin/python3

"""implementing FIFO Caching"""

from typing import Any, Optional, Dict
from base_caching import BaseCaching
""" importing from base class BaseCaching"""

class FIFOCache(BaseCaching):
    """ class for FIFO Caching"""

    def __init__(self):
        """Initializing __init__ for FIFOCache class"""
        super().__init__()
        self.order = []

    def put(self, key: Any, item: Any)-> None:
        """cache new items onto dictionary"""

        if key is None or item is None:
            return
        
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
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


    def get(self, key):
        """Get cache data"""

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)



