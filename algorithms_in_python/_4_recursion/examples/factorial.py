__author__ = 'Junior Teudjio'

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


if __name__ == '__main__':
    print 'factorial of the the 10 first natural numbers\n'
    for i in xrange(1, 11,1):
        print 'factorial %d = %d'% (i, factorial(i))