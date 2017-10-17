__author__ = 'Junior Teudjio'

def merge_sort(l):
    def _merge(l, l1, l2):
        i, j, k = 0, 0, 0

        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                l[k] = l1[i]
                i += 1
            else:
                l[k] = l2[j]
                j += 1
            k += 1

        while i < len(l1):
            l[k] = l1[i]
            i += 1
            k += 1

        while j < len(l2):
            l[k] = l2[j]
            j += 1
            k += 1

    if len(l) <= 1:
        return

    middle = len(l) // 2
    l1 = l[0:middle]
    l2 = l[middle:len(l)]
    merge_sort(l1)
    merge_sort(l2)
    _merge(l, l1, l2)


if __name__ == '__main__':
    l = [2,3,1,6,3,0,0,43,34,709,65,44,2]
    print l
    merge_sort(l)
    print l