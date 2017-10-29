from abc import abstractmethod, ABCMeta
from abstract_tree import AbstractTree

__author__ = 'Junior Teudjio'


class AbstractBinaryTree(AbstractTree):
    __metaclass__ = ABCMeta

    @abstractmethod
    def left(self, p):
        pass

    @abstractmethod
    def right(self, p):
        pass

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None

        # if p is the left child of parent return right
        if self.left(parent) == p:
            return self.right(parent)

        # if p is the right child of parent return left
        elif self.right(parent) == p:
            return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


    def inorder(self):
        def _subtree_inorder(p):
            if self.left(p) is not None:
                for l in _subtree_inorder(self.left(p)):
                    yield l

            yield p

            if self.right(p) is not None:
                for r in _subtree_inorder(self.right(p)):
                    yield r

        if not self.is_empty():
            return _subtree_inorder(self.root())
