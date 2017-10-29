from abstract_binary_tree import  AbstractBinaryTree

__author__ = 'Junior Teudjio'

class LinkedBinaryTree(AbstractBinaryTree):
    def __init__(self):
        self._root = None
        self._size = 0

    class _Node(object):
        __slots__ = '_element', '_left', '_right', '_parent'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._left = left
            self._right = right
            self._parent = parent

    class Position(AbstractBinaryTree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) == type(other) and self._node is other._node


    def _validate_position(self, p):
        if not isinstance(p, LinkedBinaryTree.Position):
            raise TypeError('Must be a correct Position type object')
        if not self is p._container:
            raise ValueError('Position object is unknown')
        if p._node._parent is p._node: # the delete convention is to set the parent of the node the the node itself
            raise ValueError('Position no more valid')

    def _get_node(self, p):
        self._validate_position(p) #raise error if not valid
        return p._node

    def _get_position(self, node):
        if node is None:
            return None
        return LinkedBinaryTree.Position(self, node)


    ###### ACCESSORS #######
    def __len__(self):
        return self._size

    def root(self):
        return self._get_position(self._root)

    def left(self, p):
        node = self._get_node(p)
        return self._get_position(node._left)

    def right(self, p):
        node = self._get_node(p)
        return self._get_position(node._right)

    def parent(self, p):
        node = self._get_node(p)
        return self._get_position(node._parent)


    def num_children(self, p):
        node = self._get_node(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1

        return count


    def __iter__(self):
        for p in self.positions():
            yield p


    ##### MUTATORS #####
    def _add_root(self, element):
        if self._root is not None:
            raise ValueError('Root already exists')
        self._size += 1
        self._root = LinkedBinaryTree._Node(element, None, None, None)

        return self._get_position(self._root)


    def _add_left(self, p, element):
        node = self._get_node(p)
        if node._left is not None:
            raise ValueError('left child already exists')
        node._left = LinkedBinaryTree._Node(
            element=element,
            left=None,
            right=None,
            parent=node
        )
        self._size += 1
        return self._get_position(node._left)



    def _add_right(self, p, element):
        node = self._get_node(p)
        if node._right is not None:
            raise ValueError('right child already exists')
        node._right = LinkedBinaryTree._Node(
            element=element,
            left=None,
            right=None,
            parent=node
        )
        self._size += 1
        return self._get_position(node._right)


    def _replace(self, p, new_element):
        node = self._get_node(p)
        old_element = node._element
        node._element = new_element
        return old_element

    def _delete(self, p):
        node = self._get_node(p)
        if self.num_children(p) == 2 :
            raise ValueError('Can not delete a node with more than one child')

        child = node._left if node._right is None else node._right

        if child is not None:
            child._parent = node._parent # child grandparent becomes parent

        if node is self._root:
            self._root = child
        else:
            if node is node._parent._left:
                node._parent._left = child
            elif node._parent._right:
                node._parent._right = child

        # deprecate the node
        node._parent = node # convention use in node validation procedure
        self._size -= 1

        return node._element


    def _attach(self, p, tree1, tree2):
        node = self._get_node(p)
        if not self.is_leaf(p):
            raise ValueError('node must be leaf to allow attach operation')
        if not (type(self) is type(tree1) is type(tree2)):
            raise TypeError('trees to attach must be of type : LinkedBinaryTree')
        if self is tree1 or self is tree2:
            raise ValueError('all trees to attach must be different than attaching tree')

        self._size += (len(tree1) + len(tree2))
        if not tree1.is_empty():
            node._left = tree1._root
            tree1._root._parent = node

            #kill tree1 if not self
            tree1._root = None
            tree1._size = 0
        if not tree2.is_empty():
            node._right = tree2._root
            tree2._root._parent = node

            # kill tree2 if not self
            tree2._root = None
            tree2._size = 0

if __name__ == '__main__':
    tree = LinkedBinaryTree()
    print tree.is_empty()
    tree._add_root(2)
    print tree.is_empty()
    left = tree._add_left(tree.root(), 1)
    left_left = tree._add_left(left, -2)
    left_right = tree._add_right(left, 0)

    right = tree._add_right(tree.root(), 5)
    right_left = tree._add_left(right, 3)
    right_right = tree._add_right(right, 7)

    print len(tree)
    print len(tree)
    #tree._attach(left, tree, tree)
    print len(tree)

    print 'tree elements - preorder :'
    for p in tree.preorder():
        print p.element()

    print 'tree elements - postorder :'
    for p in tree.postoder():
        print p.element()

    print 'tree elements - bread_first :'
    for p in tree.bread_first():
        print p.element()

    print 'tree elements - inorder :'
    for p in tree.inorder():
        print p.element()




