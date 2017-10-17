__author__ = 'Junior Teudjio'

def quick_sort(l):
    def _partition(l, pivot, start, end):
        i,j = start+1, end-1
        while i <= j:
            while i <= j:
                if l[i] <= pivot:
                    i += 1
                else:
                    break

            while j <= j:
                if pivot < l[j] :
                    j -= 1
                else:
                    break

            if i <= j:
                # swap i and j to maintain the invariant
                l[i], l[j] = l[j], l[i]
                #move both pointers
                i += 1
                j -= 1


        # return j because it is needed for sorting left and right subarrays to pivot
        return j

    def _quick_sort(l, start, end):
        if start >= end:
            return

        pivot = l[start]
        pivot_new_idx = _partition(l, pivot, start, end)
        l[start], l[pivot_new_idx] = l[pivot_new_idx], l[start]

        #now l[start:pivot_new_idx] <= l[pivot_new_idx] <= l[pivot_new_idx:end]
        _quick_sort(l, start, pivot_new_idx)
        _quick_sort(l, pivot_new_idx+1, end)

    #TODO: add random inplace shuffle of the list "l"
    if len(l) < 2:
        return
    _quick_sort(l, start=0, end=len(l))



if __name__ == '__main__':
    l = [2,3,1,6,3,0,0,43,34,709,65,44,2]
    print l
    quick_sort(l)
    print l