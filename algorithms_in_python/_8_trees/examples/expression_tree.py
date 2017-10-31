from linked_binary_tree import LinkedBinaryTree

__author__ = 'Junior Teudjio'


class ExpressionTree(LinkedBinaryTree):

    def __init__(self, token, left_exp_tree=None, right_exp_tree=None):
        if not isinstance(token, str):
            raise TypeError('first argument ust be a string')

        super(ExpressionTree, self).__init__()
        self._add_root(token)

        if left_exp_tree is not None:
            if token not in '+-/*^':
                raise ValueError('Operand must be one of : + - * / ')

            self._attach(self.root(), left_exp_tree, right_exp_tree)


    def __str__(self):
        def _get_str(position, accumulator):
            if self.is_leaf(position):
                accumulator.append(str(position.element()))
            else:
                accumulator.append('(')
                _get_str(position=self.left(position), accumulator=accumulator)
                accumulator.append(str(position.element()))
                _get_str(position=self.right(position), accumulator=accumulator)
                accumulator.append(')')

        accumulator =[]
        _get_str(position=self.root(), accumulator=accumulator)
        return ''.join(accumulator)


    def evaluate(self):
        operand_dict = {
            '+': lambda a, b : a + b,
            '-': lambda a, b : a - b,
            '*': lambda a, b : a * b,
            '/': lambda a, b : a / b if b != 0 else None,
            '^': lambda a, b : pow(a,b)
        }
        def _evaluate(position):
            if self.is_leaf(position):
                return int(position.element())
            left_evaluation = _evaluate(self.left(position))
            right_evaluation = _evaluate(self.right(position))
            operand = operand_dict[position.element()]
            print 'left_evaluation {op} right_evaluation = {left} {op} {right}'.format(left=left_evaluation, op=position.element(), right=right_evaluation)
            return operand(left_evaluation, right_evaluation)

        return _evaluate(self.root())


def build_expression(tokens):
    stack = []

    for token in tokens:
        if token == '(':
            continue
        if token == ')':
            right = stack.pop()
            operator = stack.pop()
            left = stack.pop()
            #print 'operator, left, right = ', operator, left, right
            stack.append(ExpressionTree(operator, left, right))
        elif token in '+-*/^':
            stack.append(token)
        else:
            stack.append(ExpressionTree(token))

    return stack.pop()


if __name__ == '__main__':
    tokens = '( ( ( 3 + 1 ) * 4 ) / ( ( 9 - 5 ) + 2 ) )'.split(' ')
    print 'tokens = ', tokens
    expr_tree = build_expression(tokens)
    print 'exp_tree = ', str(expr_tree)
    print
    result = expr_tree.evaluate()
    print
    print 'result =', result