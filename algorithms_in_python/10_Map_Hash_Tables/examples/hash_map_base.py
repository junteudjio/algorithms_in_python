from map_base import MapBase
from random import randrange

__author__ = 'Junior Teudjio'


class HashMapBase(MapBase):
    def __init__(self, capacity=11, prime=109345121):
        self._table = [None] * capacity
        self._number_of_elements = 0
        self._prime = prime
        self._scale = 1 + randrange(prime - 1)
        self._shift = randrange(prime)

    def _hash_function(self, key):
        return (hash(key)* self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._number_of_elements

    def __setitem__(self, key, value):
        bucket_idx = self._hash_function(key)
        self._set_bucket_item(bucket_idx, key, value) # should be implemented by the subclass
        if self._number_of_elements >= len(self._table) // 2:
            self._resize(len(self._table) * 2 - 1)  # preferably a prime number and we know (thanks to fermat 2**p -1 are often prime)

    def __getitem__(self, key):
        bucket_idx = self._hash_function(key)
        return self._get_bucket_item(bucket_idx, key)

    def __delitem__(self, key):
        bucket_idx = self._hash_function(key)
        self._del_bucket_item(bucket_idx, key)


    def _resize(self, new_capacity):
        old = list(self.items())
        self._table = [None] * new_capacity
        self._number_of_elements = 0

        for key, value in old:
            self[key] = value


