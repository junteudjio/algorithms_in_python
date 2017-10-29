from array_stack import ArrayStack

__author__ = 'Junior Teudjio'

def reverse_file(file_path):
    stack = ArrayStack()
    with open(file_path, 'r') as f:
        for line in f:
            stack.push(line.rstrip('\n'))

    with open(file_path, 'w') as f:
        while not stack.is_empty():
            f.write(''.join([stack.pop(), '\n']))


if __name__ == '__main__':
    file_path = '../data/file_to_reverse.txt'

    with open(file_path, 'r') as f:
        print 'original first line :\n', f.readline()

    reverse_file(file_path)

    with open(file_path, 'r') as f:
        print 'first line after reverse:\n', f.readline()