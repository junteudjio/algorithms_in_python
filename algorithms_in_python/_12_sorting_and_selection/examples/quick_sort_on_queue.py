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


def quick_sort(q):
    if len(q) <= 1:
        return

    pivot = q.top()
    left_pivot_q = Queue()
    equal_pivot_q = Queue()
    right_pivot_q = Queue()

    while not q.is_empty():
        element = q.dequeue()
        if element < pivot :
            left_pivot_q.enqueue(element)
        elif element == pivot:
            equal_pivot_q.enqueue(element)
        else:
            right_pivot_q.enqueue(element)

    quick_sort(left_pivot_q)
    quick_sort(right_pivot_q)

    #now all we have to do is concatenate the left, equal and right sub_queues
    while not left_pivot_q.is_empty():
        q.enqueue(left_pivot_q.dequeue())

    while not equal_pivot_q.is_empty():
        q.enqueue(equal_pivot_q.dequeue())

    while not right_pivot_q.is_empty():
        q.enqueue(right_pivot_q.dequeue())


if __name__ == '__main__':
    q = Queue()
    q.enqueue(3).enqueue(0).enqueue(1).enqueue(5).enqueue(80).enqueue(0).enqueue(1).enqueue(7).enqueue(13).enqueue(-1)
    q.enqueue(31).enqueue(10).enqueue(17).enqueue(25).enqueue(8).enqueue(20).enqueue(21)

    quick_sort(q)
    while not q.is_empty():
        print q.dequeue()
