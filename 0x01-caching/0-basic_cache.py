#!/usr/bin/python3

"""Basic dictionary"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Basic Dictionary"""

    def put(self, key, item):
        """insert into cache"""

        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """retrieve cache items"""

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
        

