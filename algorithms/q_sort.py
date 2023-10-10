import random


def partition(x, l, r, pivot, key):
    """
    :param x: Source array (list)
    :param l: left border of partitioning range (int)
    :param r: right border (not included) of partitioning range (int)
    :param pivot: pivot element to divide array (any item from x[l, r)).
    :return: il, ir -- desired partition
    This function should reorder elements of x within [l, r) region
    in the way, these conditions are true:
    x[l:il] < pivot
    x[il:ir] == pivot
    x[ir:r] > pivot
    """
    for i, el in enumerate(x[l:r], l):
        if el == pivot:
            il = ir = i
            break
    r -= 1
    while l < il and r > ir:
        while l < il and x[l] <= pivot:
            if key(x[l]) == pivot:
                x[il - 1], x[l] = x[l], x[il - 1]
                il -= 1
                continue
            l += 1
        while r > ir and key(x[r]) >= pivot:
            if key(x[r]) == pivot:
                x[ir + 1], x[r] = x[r], x[ir + 1]
                ir += 1
                continue
            r -= 1
        if l < il and r > ir:
            x[l], x[r] = x[r], x[l]
    while l < il:
        if key(x[l]) > pivot:
            x[ir], x[l] = x[l], x[ir]
            x[l], x[il - 1] = x[il - 1], x[l]
            ir, il = ir - 1, il - 1
        elif key(x[l]) == pivot:
            x[l], x[il - 1] = x[il - 1], x[l]
            il -= 1
        else:
            l += 1
    while r > ir:
        if key(x[r]) < pivot:
            x[il], x[r] = x[r], x[il]
            x[r], x[ir + 1] = x[ir + 1], x[r]
            ir, il = ir + 1, il + 1
        elif key(x[r]) == pivot:
            x[r], x[ir + 1] = x[ir + 1], x[r]
            ir += 1
        else:
            r -= 1
    return il, ir


def qsort(x, l=0, r=None, key=lambda x: x):
    if r is None:
        r = len(x)
    if (r - l) > 1:
        pivot = key(x[random.randint(l, r - 1)])
        il, ir = partition(x, l, r, pivot, key)
        qsort(x, l, il, key)
        qsort(x, ir, r, key)


if __name__ == '__main__':
    # N = int(input())
    # x = list(map(int, input().split()))
    lst = [random.randint(-10000, 10000) for num in range(100000)]
    cmp = sorted(lst)
    x = lst
    qsort(x)
    str1 = ' '.join(map(str, x))
    str2 = ' '.join(map(str, cmp))
    assert str1 == str2


