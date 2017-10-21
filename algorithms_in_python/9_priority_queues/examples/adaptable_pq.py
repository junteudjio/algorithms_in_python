from heap_pq import HeapPriorityQueue

__author__ = 'Junior Teudjio'


class AdaptablePQ(HeapPriorityQueue):
    __slots__ = '_index'

    def __init__(self, data=()):
        self._data = [AdaptablePQ.Position(key, value, i) for i, (key, value) in enumerate(data)]
        if len(self) > 1:
            self._min_heapify()

    class Position(HeapPriorityQueue._Item):
        def __init__(self,key, value, index):
            super(AdaptablePQ.Position, self).__init__(key, value)
            self._index = index

    class InvalidPositionException(Exception):
        pass

    def _swap(self, i, j):
        super(AdaptablePQ, self)._swap(i, j)

        #update the index attributes of the position i/j which are now changed to j/i by _swap(i,j)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, i, position):
        # i > 0 : because we don't need to upgrade if it's the root and we are also certain it has a parent
        if i > 0 and position < self._data[self._parent(i)]:
            self._upgrade(i)
        else:
            self._downgrade(i)

    def add(self, key, value):
        new_idx = len(self)
        new_position = AdaptablePQ.Position(key, value, index=new_idx)
        self._data.append(new_position)
        self._upgrade(new_idx)

        #return it to the client
        return new_position


    def update(self, position, new_key, new_value):
        index = position._index

        # check the correctness of the position
        if 0 <= index < len(self)  and self._data[index] is position:
            self._data[index]._key, self._data[index]._value = new_key, new_value

            # reset its position
            self._bubble(index, position)
        else:
            raise AdaptablePQ.InvalidPositionException('Invalid Position')


    def remove(self, position):
        index = position._index

        # check correctness of the position
        if 0 <= index < len(self) and self._data[index] is position:
            # swap element to remove with the last of the PQ/array
            self._swap(index, len(self)-1)

            # remove the last element which is the one we want to delete
            element = self._data.pop()

            # downgrade/upgrade back the previously last element to keep the heap-order condition
            self._bubble(index, position)

            return element._key, element._value
        else:
            raise AdaptablePQ.InvalidPositionException('Invalid Position')


if __name__ == '__main__':
    pq = AdaptablePQ([(90, 'maxim'), (-1, 'minim')])
    pq.add(6, 'blabla')
    pq.add(2, 'bobo')
    bibi = pq.add(4, 'bibi')
    bubu = pq.add(3, 'bubu')
    pq.add(5, 'bebe')
    byby = pq.add(1, 'byby')
    pq.add(3, 'beba')


    print pq._data
    print pq.min()
    print pq.remove_min()
    print pq._data
    pq.remove(bibi)
    print pq._data
    pq.remove(byby)
    print pq._data
    pq.update(bubu, -2, 'BUBU')
    print pq._data
