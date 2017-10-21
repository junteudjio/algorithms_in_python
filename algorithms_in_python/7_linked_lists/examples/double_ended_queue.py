from doubly_linked_list import _DoublyLinkedList

__author__ = 'Junior Teudjio'


class DoubleEndedQueue(_DoublyLinkedList):
    class _EmptyQueueException(Exception):
        pass

    def head(self):
        if self.is_empty():
            raise self._EmptyQueueException("Double Ended Queue is empty")

        _head = self._header.next
        return _head.value

    def tail(self):
        if self.is_empty():
            raise self._EmptyQueueException("Double ended Queue is empty")

        _tail = self._trailer.prev
        return _tail.value

    def insert_head(self, value):
        self._insert_between(value=value, prev=self._header, nnext=self._header.next)

    def insert_tail(self, value):
        self._insert_between(value=value, prev=self._trailer.prev, nnext=self._trailer)

    def delete_head(self):
        if self.is_empty():
            raise self._EmptyQueueException("Double ended Queue is empty")
        node_to_delete = self._header.next
        self._delete(node_to_delete)

    def delete_tail(self):
        if self.is_empty():
            raise self._EmptyQueueException("Double ended Queue is empty")

        node_to_delete = self._trailer.prev
        self._delete(node_to_delete)

    def __str__(self):
        res = []
        res.append('HEADER')
        cursor = self._header.next
        while cursor is not None:
            res.append(str(cursor.value))
            cursor = cursor.next
        res[-1] = 'TRAILER'

        return '->'.join(res)


if __name__ == '__main__':
    q = DoubleEndedQueue()
    q.insert_head(12)
    q.insert_head(1)
    print q
    q.insert_tail(170)
    q.insert_tail(45)
    q.insert_tail(-23)
    print q

    q.delete_head()
    print q
    q.delete_tail()
    print q