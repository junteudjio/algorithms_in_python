__author__ = 'Junior Teudjio'


class Queue:
    class _EmptyQueueException(Exception):
        pass

    class _Node:
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def enqueue(self, element):
        node = Queue._Node(element)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

        # return self so we can stack enqueue operations
        return self


    def dequeue(self):
        if self.is_empty():
            raise Queue._EmptyQueueException('Queue is empty')

        element = self.head.element

        if len(self) == 1:
            self.head = None
            self.tail = None
        else:
            old_head = self.head
            self.head = old_head.next
            old_head.element = None

        self.size -= 1
        return element

    def top(self):
        if self.is_empty():
            raise Queue._EmptyQueueException('Queue is empty')
        return self.head.element

    def last(self):
        if self.is_empty():
            raise Queue._EmptyQueueException('Queue is empty')
        return self.tail.element


def merge_sort(q):
    def merge(q, q1, q2):
        while not q1.is_empty() and not q2.is_empty():
            if q1.top() < q2.top():
                q.enqueue(q1.dequeue())
            else:
                q.enqueue(q2.dequeue())

        while not q1.is_empty():
            q.enqueue(q1.dequeue())

        while not q2.is_empty():
            q.enqueue(q2.dequeue())

    if len(q) == 1:
        return

    q1 = Queue()
    q2 = Queue()
    while not q.is_empty():
        q1.enqueue(q.dequeue())

        # we add this check in case len(q is odd
        if not q.is_empty():
            q2.enqueue(q.dequeue())

    merge_sort(q1)
    merge_sort(q2)
    merge(q, q1, q2)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(3).enqueue(0).enqueue(1).enqueue(5).enqueue(80).enqueue(0).enqueue(1).enqueue(7).enqueue(13).enqueue(-1)
    q.enqueue(31).enqueue(10).enqueue(17).enqueue(25).enqueue(8).enqueue(20).enqueue(21)

    merge_sort(q)
    while not q.is_empty():
        print q.dequeue()
