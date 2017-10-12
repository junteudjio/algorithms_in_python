from array_stack import ArrayStack

__author__ = 'Junior Teudjio'

def is_valid_html(raw_html):
    """
    Return True if the each opening html tag in the raw_html string has and associated closing html tag.
    Parameters
    ----------
    raw_html: str or unicode
        The raw html string we need to check for validity
    Returns
    -------
        Boolean
    """
    def is_opening_tag(tag):
        return not tag.startswith('/')

    stack = ArrayStack()
    opening_idx = raw_html.find('<')
    while opening_idx != - 1:
        closing_idx = raw_html.find('>', opening_idx+1)
        if closing_idx == - 1:
            return False
        tag = raw_html[opening_idx+1:closing_idx]

        if is_opening_tag(tag):
            stack.push(tag)
        else:
            if stack.is_empty() or stack.top() != tag[1:]:
                return False
            else:
                stack.pop()
        opening_idx = raw_html.find('<', closing_idx+1)

    return stack.is_empty()


if __name__ == '__main__':
    bad_html_file_path = '../data/bad.html'
    good_html_file_path = '../data/good.html'

    with open(bad_html_file_path, 'r') as f:
        raw_html = f.read()
        print is_valid_html(raw_html)


    with open(good_html_file_path, 'r') as f:
        raw_html = f.read()
        print is_valid_html(raw_html)