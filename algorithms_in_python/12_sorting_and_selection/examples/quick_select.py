__author__ = 'Junior Teudjio'



def quick_select(l, k, find_largest=True):
    """
    return the k_th largest/smallest element of list l
    Parameters
    ----------
    l : list
    k : int
    find_largest : Boolean
        True if return the k_th largest element False if return the k-th smallest element
    Returns
    -------
    element of list l
    """
    def _partition(l, pivot, left, right):
        i,j = left + 1, right-1
        while i <= j:
            while i <= j:
                if l[i] <= pivot:
                    i += 1
                else:
                    break
            while i <= j:
                if pivot < l[j]:
                    j -= 1
                else:
                    break

            # if the two pointers have not cross we need to swap positions and update pointers
            if i <= j:
                l[j], l[i] = l[i], l[j]
                i += 1
                j -= 1

        return j

    def _quick_select(l, k, left, right):
        pivot = l[left]
        pivot_new_position = _partition(l, pivot, left, right)
        if pivot_new_position == k-1:
            return pivot_new_position
        elif k < pivot_new_position:
            return _quick_select(l, k, left, pivot_new_position)
        else:
            return _quick_select(l, k, pivot_new_position+1, right)


    if len(l) == 0 or k == 0 or len(l) < k:
        return None

    k_smallest_idx = _quick_select(l, k, left=0, right=len(l))
    if find_largest:
        return len(l)-1 - k_smallest_idx
    else:
        return k_smallest_idx

def find_median(l):
    return quick_select(l, len(l)//2)

if __name__ == '__main__':
    print quick_select(range(15), 1, find_largest=False)
    print quick_select(range(15), 1, find_largest=False)
    print find_median(range(101))