__author__ = 'Junior Teudjio'


class LinkedListQueue(object):
    class _EmptyQueueException(Exception):
        pass

    class _Node(object):
        __slots__ = 'value', 'next'

        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, value):
        new_node = self._Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return self

    def dequeue(self):
        if self.is_empty():
            raise self._EmptyQueueException('Queue is empty')

        old_head = self.head
        self.head = self.head.next
        old_head.next = None #help the garbage collector
        self.size -= 1

        if len(self) == 1:
            self.tail = self.head

        return old_head.value

    def top(self):
        if not self.is_empty():
            return self.head.value

    def last(self):
        if not self.is_empty():
            return self.tail.value

    def __str__(self):
        if self.is_empty():
            return 'None'
        res = []
        cursor = self.head
        while cursor is not None:
            res.append(str(cursor.value))
            cursor = cursor.next
        res.append('None')
        return '->'.join(res)


if __name__ == '__main__':
    q = LinkedListQueue()
    q.enqueue(45).enqueue(23).enqueue(23).enqueue(2)
    print q
    print q.dequeue()
    print q
    print q.enqueue(0)
    print q.top()
    print q.last()