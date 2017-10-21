import random
import copy
from algorithms_in_python.helpers import timer

__author__ = 'Junior Teudjio'

@timer
def insertion_sort1(A):

    def _swap(i,j):
        A[i], A[j] = A[j], A[i]

    key, size = 1, len(A)

    while key < size:
        current = A[key]
        i = key - 1
        while i >= 0 and A[i] > current:
            _swap(i+1, i)
            i -= 1
        key += 1

    return A


@timer
def insertion_sort2(A):
    #this version uses binary_search to find the correct position where to insert
    #this reduces the number of compares to O(log n) whereas the number of swaps is still O(n)
    def _swap(i,j):
        A[i], A[j] = A[j], A[i]

    def binary_search(target, left, right):
        if len(A) == 0:
            return None

        #note that the recursion termination condition is different that the one for the classic binary search
        #since we are not only interested in finding the exact target but a position (t) where all the elements in
        #the array for bellow position t are less than target and elements above t are bigger than target
        #and this happens when left > right
        if left > right:
            return left

        # good way to find the middle to avoid integer overflow as oppose to (right + left) // 2
        # for which the summation of left and right could be a huge integer which can't be store in 32/64 bits
        middle = (right - left) // 2 + left
        if A[middle] == target:
            return middle
        elif A[middle] > target:
            return binary_search(target, left, middle-1)
        elif A[middle] < target:
            return binary_search(target, middle+1, right)

    key, size = 1, len(A)
    while key < size:
        current = A[key]
        i = key - 1
        index = binary_search(current, left=0, right=i)
        if index is not None:
            while i >= index >= 0:
                _swap(i+1, i)
                i -= 1
        key += 1

    return A




if __name__ == '__main__':
    A = random.sample(xrange(1000000), 10000)
    B = copy.copy(A)
    insertion_sort1(A)
    insertion_sort2(B)
    print A
    print B
