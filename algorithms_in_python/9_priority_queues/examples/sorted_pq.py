from base_abstract_pq_class import AbstractPriorityQueue

__author__ = 'Junior Teudjio'

#TODO: implement a second version with positional array
class SortedPriorityQueue(AbstractPriorityQueue):
    """
    This implementation uses a list and sort the element in decreasing order because delete (the min in this case) is
    easier at the end of lists.
    """
    def __init__(self):
        self._data = []


    def __len__(self):
        return len(self._data)

    def min(self):
        if self.is_empty():
            raise SortedPriorityQueue._EmptyPQException('Priority queue is empty')
        min_item = self._data[-1]
        return min_item._key, min_item._value

    def remove_min(self):
        if self.is_empty():
            raise SortedPriorityQueue._EmptyPQException('Priority queue is empty')
        min_item = self._data[-1]
        min_item_key, min_item_value = min_item._key, min_item._value
        self._data.pop()
        return min_item_key, min_item_value

    def add(self, key, value):
        # our implementation using list rely on sorting the elements from back to front: ie in drecreasing order when
        # viewed from left to right
        new_item = SortedPriorityQueue._Item(key, value)
        if self.is_empty():
            self._data.append(new_item)

        for i, item in enumerate(self._data):
            if item < new_item:
                #note the use of insert which is very very very inefficient since its requires to shift all the next elements
                #the coming implementatation with positional array won't have this issue.
                self._data.insert(i, new_item)
                break
        else:
            self._data.append(new_item)



if __name__ == '__main__':
    pq = SortedPriorityQueue()
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

