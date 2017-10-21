from array_stack import ArrayStack

__author__ = 'Junior Teudjio'


def is_matching(expr):
    """
    Return True if delimiters in expr match correctly, False otherwise
    Parameters
    ----------
    test_str: str or unicode
        expression to evaluate parameters correctness
    Returns
    -------
        Boolean
    """
    delimiters_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    stack = ArrayStack()

    for c in expr:
        if c in delimiters_map:
            stack.push(c)
        elif c in delimiters_map.itervalues():
            if stack.is_empty() or delimiters_map[stack.top()] != c:
                return False
            else:
                stack.pop()

    return stack.is_empty()


if __name__ == '__main__':
    expr1 = '(((dd)))ze{a-}{}[]'
    expr2 = '(((dd))ze{a-}{}[]'
    expr3 = '((({{{{{}}'
    expr4 = ']]]])))}'
    expr5 = '()()()()()()[][]'

    print is_matching(expr1)
    print is_matching(expr2)
    print is_matching(expr3)
    print is_matching(expr4)
    print is_matching(expr5)
