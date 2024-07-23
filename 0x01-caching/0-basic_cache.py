#!/usr/bin/env python3
'''Create class BasicCache that inherits from BaseCaching
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A class `BasicCache` that inherits from `BaseCaching
    '''
    def put(self, key, item):
        '''Assign to the dictionary 'self.cache_data'
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Return the value in 'self.cache_data'
        '''
        return self.cache_data.get(key, None)
