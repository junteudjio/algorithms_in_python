__author__ = 'Junior Teudjio'

def myreverse(data):
    result = []
    #handle corner case
    if len(data) == 0:
        return []

    def helper(index):
        #handle recursion stop condition
        if index == len(data) - 1:
            result.append(data[index])
        #handle recursion step
        else:
            helper(index+1)
            result.append(data[index])

    helper(0)
    return result



def myreverse_2(data):
    if len(data) == 0:
        return []

    def helper(index):
        if index == len(data)-1:
            return [data[index]]
        else:
            partial_reverse = helper(index+1)
            partial_reverse.append(data[index])
            return partial_reverse

    return helper(0)


#in place version
def myreverse_3(data):
    if len(data) == 0:
        return []

    def helper(left, right):
        if left < right:
            helper(left+1, right-1)
            data[left], data[right] = data[right], data[left]
            return data

    return helper(0, len(data)-1)










if __name__ == '__main__':
    print myreverse(range(10))
    myreverse(range(0))
    myreverse(range(998))
    # stack exceeded exception at 999 myreverse(range(999))
    print

    print myreverse_2(range(10))
    myreverse_2(range(0))
    myreverse_2(range(998))
    # stack exceeded exception at 999 myreverse_2(range(999))
    print


    print myreverse_3(range(10))
    myreverse_3(range(0))
    myreverse_3(range(1995))
    # stack exceeded exception at 999 myreverse_3(range(1996))
