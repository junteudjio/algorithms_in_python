__author__ = 'Junior Teudjio'


class LinkedListStack(object):

    class _EmptyStackException(Exception):
        pass

    class _Node(object):
        __slots__ = 'value', 'next'
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def push(self, value):
        new_node = self._Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

        return self


    def pop(self):
        if self.is_empty():
            raise self._EmptyStackException("Stack is empty")
        old_head = self.head
        self.head = self.head.next
        old_head.next = None #help the garbage collector
        self.size -= 1
        return old_head.value

    def first(self):
        if not self.is_empty():
            return self.head.value


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
    s = LinkedListStack()
    s.push(1).push(2).push(3).push(4).push(7)
    print s
    print s.pop()
    print s