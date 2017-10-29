__author__ = 'Junior Teudjio'


def merge_sort_BU(l):
    def _sort(l, start, middle, end):
        end = min(len(l), end) #update end since it may be greater than the real size of l

        #copy the arrays and start modifying l
        aux1 = l[start:middle]
        aux2 = l[middle:end]

        i = j = 0
        k = start
        while i < len(aux1) and j < len(aux2):
            if aux1[i] < aux2[j]:
                l[k] = aux1[i]
                i += 1
            else:
                l[k] = aux2[j]
                j += 1
            k += 1

        while i < len(aux1):
            l[k] = aux1[i]
            i += 1
            k += 1

        while j < len(aux2):
            l[k] = aux2[j]
            j += 1
            k += 1

    if len(l) <  2:
        return l

    step_size = 2
    while step_size <= len(l):
        for start in range(0, len(l), step_size):
            middle = start + step_size // 2
            end = middle + step_size // 2 #end index exclusive
            _sort(l, start, middle, end)

        step_size *= 2



if __name__ == '__main__':
    l = [2,3,1,6,3,0,0,43,34,709,65,44,2]
    print l
    merge_sort_BU(l)
    print l