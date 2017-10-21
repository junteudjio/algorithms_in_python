from base_abstract_pq_class import AbstractPriorityQueue

__author__ = 'Junior Teudjio'


#This is a min-heap
class HeapPriorityQueue(AbstractPriorityQueue):
    def __init__(self, data=()):
        self._data = [HeapPriorityQueue._Item(key, value) for key, value in data]
        if len(self) > 1:
            self._min_heapify()

    def _min_heapify(self):
        deepest_non_leaf_level = self._parent(len(self)-1) #parent of the last node
        while deepest_non_leaf_level >= 0:
            self._downgrade(deepest_non_leaf_level)
            deepest_non_leaf_level -= 1

    def _parent(self, i):
        return (i-1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _has_left_child(self, i):
        potential_left_child = self._left_child(i)
        return potential_left_child < len(self)

    def _has_right_child(self, i):
        potential_right_child = self._right_child(i)
        return potential_right_child < len(self)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upgrade(self, i):
        parent = self._parent(i)
        if parent >= 0 and self._data[i] < self._data[parent]:
            self._swap(i, parent)
            self._upgrade(parent)

    def _downgrade(self, i):
        if self._has_left_child(i):
            left_child = self._left_child(i)
            if self._data[left_child] < self._data[i]:
                self._swap(left_child, i)
                self._downgrade(left_child)

            elif self._has_right_child(i):
                right_child = self._right_child(i)
                if self._data[right_child] < self._data[i]:
                    self._swap(i, right_child)
                    self._downgrade(right_child)


    # PUBLIC START HERE:
    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        new_item = HeapPriorityQueue._Item(key, value)
        self._data.append(new_item)
        self._upgrade(len(self)-1)


    def min(self):
        if self.is_empty():
            raise HeapPriorityQueue._EmptyPQException('Priority queue is empty')
        min_item = self._data[0]
        return min_item._key, min_item._value

    def remove_min(self):
        if self.is_empty():
            raise HeapPriorityQueue._EmptyPQException('Priority queue is empty')
        min_item = self._data[0]
        self._data[0] = self._data[len(self)-1]
        self._downgrade(0)
        self._data.pop()
        return min_item._key, min_item._value



if __name__ == '__main__':
    pq = HeapPriorityQueue([(90, 'maxim'), (-1, 'minim')])
    pq.add(6, 'blabla')
    pq.add(2, 'bobo')
    pq.add(4, 'bibi')
    pq.add(3, 'bubu')
    pq.add(5, 'bebe')
    pq.add(1, 'byby')
    pq.add(3, 'beba')


    print pq
    print pq.min()
    print pq.remove_min()
    print pq
    print pq.min()


