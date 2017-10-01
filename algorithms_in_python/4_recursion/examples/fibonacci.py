from algorithms_in_python.helpers import timer
__author__ = 'Junior Teudjio'

@timer
def bad_fibonacci(n):
    def helper(n):
        if n <= 1:
            return 1
        return helper(n - 1) + helper(n - 2)

    return helper(n)


@timer
def good_fibonacci(n):
    memo = dict()

    def helper(n):
        if n <= 1:
            return 1

        if n in memo:
            return memo[n]
        else:
            result = helper(n-1) + helper(n-2)
            memo[n] = result
            return result
    return helper(n)


if __name__ == '__main__':
    print good_fibonacci(30)
    print bad_fibonacci(30)
