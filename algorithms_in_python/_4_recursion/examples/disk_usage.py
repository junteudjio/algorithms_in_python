import os
__author__ = 'Junior Teudjio'


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        children = [ os.path.join(path, child) for child in os.listdir(path)]
        for child_path in children:
            total += disk_usage(child_path)
    return total


if __name__ == '__main__':
    print disk_usage('../../../')