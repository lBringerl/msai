def same_type(c0, c1):
    if c0 in '[]' and c1 in '[]':
        return True
    if c0 in '()' and c1 in '()':
        return True
    if c0 in '{}' and c1 in '{}':
        return True


def check_rbs(seq):
    stack = []
    for c in seq:
        if c in '({[':
            stack.append(c)
            continue
        if len(stack) == 0:
            return 'no'
        if same_type(c, stack[-1]):
            stack.pop()
    if stack:
        return 'no'
    return 'yes'


if __name__ == '__main__':
    print(check_rbs(input()))
