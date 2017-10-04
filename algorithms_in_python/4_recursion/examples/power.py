from algorithms_in_python.helpers import timer
__author__ = 'Junior Teudjio'



def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

#reduce the problem by half each call --> O(lg n)
def power_fast(x, n):
    if n == 0:
        return 1
    else:
        half = n // 2
        result_squared =  power_fast(x, half)
        if n % 2 == 0:
            return result_squared * result_squared
        else:
            return x * result_squared * result_squared


if __name__ == '__main__':
    print timer(power)(2, 900)
    print timer(power_fast)(2, 900)