__author__ = 'Junior Teudjio'


class ArrayStack:
    class StackEmpty(Exception):
        pass

    def __init__(self):
        self.L = []

    def push(self, element):
        self.L.append(element)

    def pop(self):
        if self.is_empty():
            raise ArrayStack.StackEmpty('The stack is empty')
        return self.L.pop()

    def top(self):
        if self.is_empty():
            raise ArrayStack.StackEmpty('The stack is empty')
        return self.L[-1]

    def is_empty(self):
        return len(self.L) == 0

    def __len__(self):
        return len(self.L)


if __name__ == '__main__':
    stack = ArrayStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    while not stack.is_empty():
        print stack.pop()
