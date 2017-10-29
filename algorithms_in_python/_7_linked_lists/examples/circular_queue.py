__author__ = 'Junior Teudjio'


class CircularQueue(object):
    class _EmptyQueueException(Exception):
        pass

    class _Node(object):
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, value):
        new_node = self._Node(value)
        if self.is_empty():
            self._tail = new_node
            self._tail.next = new_node #tail and head are the same
            self._size += 1
            return self

        old_tail = self._tail
        head = self._tail.next
        old_tail.next = new_node
        new_node.next = head
        # new node becomes the tail of the queue
        self._tail = new_node
        self._size += 1

        return self

    def dequeue(self):
        if self.is_empty():
            raise self._EmptyQueueException("Circular Queue is empty")

        if len(self) == 1:
            value = self._tail.value
            self._tail = None
            self._size -= 1
            return value

        old_head = self._tail.next
        tail = self._tail
        tail.next = old_head.next
        old_head.next = None
        self._size -= 1

        return old_head.value



    def rotate(self):
        if self.is_empty():
            raise self._EmptyQueueException("Circular Queue is empty")

        # no need to rotate if len is 1
        if len(self) >= 2:
            old_head = self._tail.next
            self._tail = old_head

        return self

    def top(self):
        if self.is_empty():
            raise self._EmptyQueueException("Circular Queue is empty")

        head = self._tail.next
        return head.value

    def last(self):
        if self.is_empty():
            raise self._EmptyQueueException("Circular Queue is empty")
        return  self._tail.value


    def __str__(self):
        if self.is_empty():
            return 'None'

        res = []
        cursor = self._tail
        cursor = cursor.next
        while cursor and cursor is not self._tail:
            res.append(str(cursor.value))
            cursor = cursor.next
        res.append(str(self._tail.value))
        res.append('None')
        return '->'.join(res)


if __name__ == '__main__':
    q = CircularQueue()
    q.enqueue(45).enqueue(3).enqueue(23).enqueue(2)
    print q
    print q.top()
    print q.rotate()
    print q.top()
    print q.rotate()
    print q.top()

    print q
    print q.enqueue(0)
    print q.rotate()

