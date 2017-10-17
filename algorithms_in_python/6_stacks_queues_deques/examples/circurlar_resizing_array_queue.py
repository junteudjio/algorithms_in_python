__author__ = 'Junior Teudjio'

#TODO: implement this using only one pointer instead of two: much easier that way.
def _handle_empty_queue(func):
    def decorator(self, *pargs, **kargs):
        if self.is_empty():
            raise CircularResizingArrayQueue.QueueEmptyError('Queue is empty')
        else:
            return func(self, *pargs, **kargs)

    return decorator

class CircularResizingArrayQueue:
    
    class QueueEmptyError(Exception):
        pass
    
    def __init__(self, initial_capaticy=4):
        self.capacity = 4 if initial_capaticy<=0 else initial_capaticy
        self.data = [None] * self.capacity
        self.head = 0
        self.tail = 0
        self.number_of_elements = 0


    def enque(self, element):
        if self.capacity == self.number_of_elements:
            self._resize_queue(self.capacity*2)

        self.data[self.tail] = element
        new_tail_position = (self.tail + 1) % self.capacity
        self.tail = new_tail_position
        self.number_of_elements += 1

    @_handle_empty_queue
    def deque(self):
        element_to_pop = self.data[self.head]
        self.data[self.head] = None #help the garbage collector
        new_head_position = (self.head + 1) % self.capacity
        self.head = new_head_position
        self.number_of_elements -= 1

        # commenting this out because not sure if the code is working with it.
        # if 0 < self.number_of_elements < self.capacity // 4:
        #     self._resize_queue(self.capacity // 2)

        return element_to_pop

    @_handle_empty_queue
    def __len__(self):
        return self.number_of_elements

    def first_element(self):
        return self.data[self.head]

    @_handle_empty_queue
    def last_element(self):
        return self.data[self.tail-1]

    def is_empty(self):
        return self.number_of_elements == 0
    
    def _resize_queue(self, new_capacity):

        new_data = [None] * new_capacity

        walk = self.head

        #we handle the size increase and size decrease: in fact in case of size decrease new_capacity is lower than capacity
        number_of_elements_to_copy = min(new_capacity, self.capacity)
        for idx in xrange(number_of_elements_to_copy):
            new_data[idx] = self.data[walk]
            walk = (walk + 1) % self.capacity

        self.head = 0
        self.tail = number_of_elements_to_copy
        self.data = new_data
        self.capacity = new_capacity


if __name__ == '__main__':
    q = CircularResizingArrayQueue()
    q.enque(1)
    q.enque(2)
    q.enque('a')

    print q.data
    print q.first_element()
    print q.last_element()
    print len(q)

    q.deque()
    print q.data
    print q.first_element()
    print q.last_element()
    print len(q)

    q.enque(4)
    q.enque(5)
    q.enque(6)
    q.enque(7)
    print q.first_element()
    print q.last_element()
    print len(q)
    print q.data
    q.deque()
    q.deque()
    q.deque()
    q.deque()
    q.deque()
    print q.data
    print q.first_element()
    print q.last_element()
    print q.head
    print q.tail

    print q.data
    print q.head
    print q.tail
    print len(q)

