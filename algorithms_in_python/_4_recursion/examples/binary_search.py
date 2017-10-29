__author__ = 'Junior Teudjio'


def binary_search(data, target):
    "Return the index if found, return None else"
    if len(data) == 0:
        return None

    def binary_search_helper(left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            return binary_search_helper(mid + 1, right)
        else:
            return binary_search_helper(left, mid - 1)

    return binary_search_helper(0, len(data))


def binary_search_iterative(data, target):
    if len(data) == 0:
        return None

    left, right = 0, len(data)
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    #if we reach here, it means target is not in data
    return None



if __name__ == '__main__':
    print binary_search(range(0, 40, 3), 10)
    print binary_search(range(0, 40, 3), 9)
    print binary_search(range(0, 40, 3), 3)

    print binary_search_iterative(range(0, 40, 3), 10)
    print binary_search_iterative(range(0, 40, 3), 9)
    print binary_search_iterative(range(0, 40, 3), 3)

