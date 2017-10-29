from collections import MutableMapping

__author__ = 'Junior Teudjio'


class MapBase(MutableMapping):
    class _Item(object):
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)
