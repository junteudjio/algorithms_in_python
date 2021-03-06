from abc import abstractmethod, ABCMeta
from algorithms_in_python._7_linked_lists.examples.linked_list_queue import LinkedListQueue

__author__ = 'Junior Teudjio'


class AbstractTree(object):
    __metaclass__ = ABCMeta

    class Position(object):
        __metaclass__ = ABCMeta

        @abstractmethod
        def element(self, p):
            pass

        @abstractmethod
        def __eq__(self, other):
            pass

        def __ne__(self, other):
            return not (self == other)

    @abstractmethod
    def root(self):
        pass

    @abstractmethod
    def parent(self, p):
        pass

    @abstractmethod
    def num_children(self, p):
        pass

    @abstractmethod
    def children(self, p):
        pass

    @abstractmethod
    def __len__(self):
        pass


    def is_root(self, p):
        return p  is self.root()

    def is_leaf(self,p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def _height(self, p):
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height(child) for child in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height(p)


    def preorder(self):
        def _subtree_preoder(p):
            yield p
            for c in self.children(p):
                for other in _subtree_preoder(c):
                    yield other

        if not self.is_empty():
            return _subtree_preoder(self.root())

    def postoder(self):
        def _subtree_postorder(p):
            for c in self.children(p):
                for other in _subtree_postorder(c):
                    yield other
            yield p

        if not self.is_empty():
            return _subtree_postorder(self.root())

    def bread_first(self):
        if self.is_empty():
            return
        q = LinkedListQueue()
        q.enqueue(self.root())
        while not q.is_empty():
            p = q.dequeue()
            yield p
            for c in self.children(p):
                q.enqueue(c)