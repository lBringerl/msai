def pascal_triangle():
    prev_row = [1]
    yield 1
    while 1:
        new_row = [1]
        yield 1
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i] + prev_row[i - 1])
            yield new_row[-1]
        new_row.append(1)
        yield 1
        prev_row = new_row


if __name__ == '__main__':
    p_gen = pascal_triangle()
    for i in range(50):
        print(next(p_gen))
