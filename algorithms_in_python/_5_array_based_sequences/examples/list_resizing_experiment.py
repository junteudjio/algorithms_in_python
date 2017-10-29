import sys
__author__ = 'Junior Teudjio'


if __name__ == '__main__':
    data = []
    for i in range(50):
        print "array of length = %d  ---> memory usage = %d "%(len(data), sys.getsizeof(data))
        data.append(None)