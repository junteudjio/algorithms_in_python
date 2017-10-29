__author__ = 'Junior Teudjio'

def mysum(data):
    def helper(index):
        if len(data) == 0:
            return 0
        if index == len(data) - 1:
            return data[index]
        else:
            return data[index] + helper(index+1)
    return helper(0)


if __name__ == '__main__':
    print mysum(range(100))
    print mysum([])
    print mysum([1])