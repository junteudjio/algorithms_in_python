from collections import deque

from base_abstract_pq_class import AbstractPriorityQueue

__author__ = 'Junior Teudjio'

#TODO: implement a second version with positional array
class UnsortedPriorityQueue(AbstractPriorityQueue):
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        item = UnsortedPriorityQueue._Item(key, value)
        self._data.append(item)

        # return self to enable add chaining
        return self

    def min(self):
        if self.is_empty():
            raise UnsortedPriorityQueue._EmptyPQException('Priority Queue is empty')
        min_idx = self._find_min_idx()
        min_item = self._data[min_idx]
        return min_item._key, min_item._value

    def remove_min(self):
        # since we use a deque instead of a positional list like in the book
        # we need to call the method remove() of the deque() class after having look for the min element
        # hence we traverse the deque twice: one time to get the min and the other to remove it.
        # with the positional array version we get the element preceding the min so we can remove without a
        # second traversal
        if self.is_empty():
            raise UnsortedPriorityQueue._EmptyPQException('Priority Queue is empty')
        min_idx = self._find_min_idx()
        min_item = self._data[min_idx]
        min_item_key, min_item_value = min_item._key, min_item._value
        self._data.remove(min_item)
        return min_item_key, min_item_value

    def _find_min_idx(self):
        if self.is_empty():
            raise UnsortedPriorityQueue._EmptyPQException('Priority Queue is empty')
        i = 1
        min_idx = 0
        min_item = self._data[min_idx]
        while i < len(self):
            if self._data[i] < min_item:
                min_item = self._data[i]
                min_idx = i
            i += 1
        return min_idx


if __name__ == '__main__':
    pq = UnsortedPriorityQueue()
    pq.add(6, 'blabla')
    pq.add(2, 'bobo')
    pq.add(4, 'bibi')
    pq.add(3, 'bubu')
    pq.add(5, 'bebe')
    pq.add(1, 'byby')
    pq.add(3, 'beba')


    print pq._data
    print pq.min()
    print pq.remove_min()
    print pq._data
    print pq.min()

