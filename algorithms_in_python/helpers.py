import time
__author__ = 'Junior Teudjio'


def timer(function):
    def wrapper(*pargs, **kargs):
        t0 = time.time()
        result = function(*pargs, **kargs)
        t1 = time.time()
        print function.__name__, ' took %s seconds'% (t1 - t0)
        return result

    return wrapper
