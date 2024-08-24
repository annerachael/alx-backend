#!/usr/bin/python3

"""implementing FIFO Caching"""

from base_caching import BaseCaching
""" importing from base class BaseCaching"""

class FIFOCache(BaseCaching):
    """ class for FIFO Caching"""

    def __init__(self):
        """Initializing __init__ for FIFOCache class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """cache new items onto dictionary"""

        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.cache_data[key] = item

        else:

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:

                fifo_key = self.order.pop(0)
                del self.cache_data[fifo_key]
                print("DISCARD: {}".format(fifo_key))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Get cache data"""

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)



