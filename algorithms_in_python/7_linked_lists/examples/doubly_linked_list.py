__author__ = 'Junior Teudjio'


class _DoublyLinkedList(object):

    class _Node(object):
        __slots__ = 'value', 'next', 'prev'
        def __init__(self, value, prev, nnext):
            self.value = value
            self.next = nnext
            self.prev = prev


    def __init__(self):
        self._trailer = self._Node(None, None, None)
        self._header = self._Node(None, None, None)

        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def _insert_between(self, prev, nnext, value):
        new_node = self._Node(value, prev, nnext)
        prev.next = new_node
        nnext.prev = new_node
        self._size += 1
        return new_node

    def _delete(self, node):
        prev = node.prev
        nnext = node.next

        prev.next = nnext
        nnext.prev = prev

        value = node.value
        node.value = node.prev = node.next = None
        self._size -= 1
        return node.value
