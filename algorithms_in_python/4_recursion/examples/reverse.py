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

if __name__ == '__main__':
    print myreverse(range(10))
    print myreverse(range(0))


    print myreverse_2(range(10))
    print myreverse_2(range(0))
