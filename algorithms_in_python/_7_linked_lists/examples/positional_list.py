from doubly_linked_list import _DoublyLinkedList

__author__ = 'Junior Teudjio'


class PositionalList(_DoublyLinkedList):

    class Position(object):
        __slots__ = '_container', '_node'

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def node(self):
            return self._node

        def __eq__(self, other):
            return type(self) == type(other) and self._node == other._node

        def __ne__(self, other):
            return not (self == other)


    # HELPERS
    def _validate_position(self, p):
        if not (p._container is self):
            raise ValueError('Position does not belong to this container')

        if not isinstance(p, self.Position):
            raise TypeError('Not of type Position')

        if p._node.next is None:
            raise ValueError('position no more valid')

        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None # header and trailer are not part of the list
        return self.Position(self, node)


    # ACCESSORS
    def head(self):
        return self._make_position(self._header.next)

    def tail(self):
        return self._make_position(self._trailer.prev)

    def before(self, position):
        node = self._validate_position(position)
        prev = node.prev
        return self._make_position(prev)

    def after(self, position):
        node = self._validate_position(position)
        nnext = node.next
        return  self._make_position(nnext)

    def __iter__(self):
        cursor = self.head()
        while cursor is not None:
            yield cursor.node().value
            cursor = self.after(cursor)

    def __str__(self):
        res= []
        for el in self:
            res.append(str(el))

        return '->'.join(res)

    # mutators
    def _insert_between(self, prev, nnext, value):
        node = super(PositionalList, self)._insert_between(prev, nnext, value)
        return self._make_position(node)

    def insert_head(self, value):
        return self._insert_between(self._header, self._header.next, value)

    def insert_tail(self, value):
        return self._insert_between(self._trailer.prev, self._trailer, value)

    def insert_after(self, value, prev_position):
        prev = self._validate_position(prev_position)
        nnext = prev.next
        return self._insert_between(prev, nnext, value)


    def insert_before(self, value, next_position):
        nnext = self._validate_position(next_position)
        prev = nnext.prev
        return self._insert_between(prev, nnext, value)


    def delete(self, position):
        node = self._validate_position(position)
        super(PositionalList, self)._delete(node)

    def update(self, position, new_value):
        node = self._validate_position(position)
        old_value = node.value
        node.value = new_value
        return old_value
    

if __name__ == '__main__':
    l = PositionalList()
    l.insert_head(12)
    l.insert_head(1)
    print l
    l.insert_tail(170)
    _45 = l.insert_tail(45)
    l.insert_tail(-23)
    l.insert_before(44, _45)
    print l
    l.insert_after(0, _45)
    print l