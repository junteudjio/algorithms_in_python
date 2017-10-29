import abc

__author__ = 'Junior Teudjio'



class AbstractPriorityQueue(object):
    __metaclass__ = abc.ABCMeta

    class _EmptyPQException(Exception):
        pass

    class _Item(object):
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

        def __str__(self):
            return '(%s : %s)'%(str(self._key), str(self._value))

        def __repr__(self):
            return str(self)


    def is_empty(self):
        return len(self) == 0

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        str(self)

    @abc.abstractmethod
    def __len__(self):
        pass

    @abc.abstractmethod
    def min(self):
        pass

    @abc.abstractmethod
    def remove_min(self):
        pass

    @abc.abstractmethod
    def add(self, key, value):
        pass



