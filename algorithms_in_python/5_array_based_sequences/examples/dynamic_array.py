import ctypes

__author__ = 'Junior Teudjio'

class DynamicArray:

    def __init__(self, size=0, init_value=0):
        assert size >= 0

        self._init_value = init_value
        self._size = size
        if self._size:
            self._capacity = 2 * self._size
        else:
            self._capacity = 1
        self._array = self._make_array(self._capacity)

    def __len__(self):
        return self._size


    def __getitem__(self, i):
        if 0 > i or i >= self._size:
            raise IndexError
        else:
            return self._array[i]
            
            
    def append(self, element):
        self._array[self._size] = element
        self._size += 1

        if self._size >= self._capacity:
            self._capacity = self._capacity * 2
            self._resize_array(self._capacity)

    def _resize_array(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in xrange(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

    def _make_array(self, capacity):
        init_values = [self._init_value] * capacity
        return (capacity * ctypes.py_object)(*init_values)



if __name__ == '__main__':
    dynamic_array = DynamicArray(3)
    dynamic_array.append(4)
    dynamic_array.append(5)
    dynamic_array.append(6)
    dynamic_array.append(7)

    for el in dynamic_array:
        print el