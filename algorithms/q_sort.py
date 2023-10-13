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
    il = l - 1
    ir = l - 1
    for j in range(l, r):
        if x[j] == pivot:
            ir += 1
            x[j], x[ir] = x[ir], x[j]
        elif x[j] < pivot:
            ir += 1
            il += 1
            x[j], x[ir] = x[ir], x[j]
            x[ir], x[il] = x[il], x[ir]
    return il + 1, ir + 1


def qsort(x, l=0, r=None, key=lambda x: x):
    if r is None:
        r = len(x)
    if (r - l) > 1:
        pivot = key(x[random.randint(l, r - 1)])
        print(x, l, r, pivot)
        il, ir = partition(x, l, r, pivot, key)
        print(il, ir)
        qsort(x, l, il, key)
        qsort(x, ir, r, key)


if __name__ == '__main__':
    # N = int(input())
    # x = list(map(int, input().split()))

    for i in range(1000):
        lst = [random.randint(0, 10) for num in range(i)]
        cmp = sorted(lst)
        x = lst
        qsort(x)
        str1 = ' '.join(map(str, x))
        str2 = ' '.join(map(str, cmp))
        print(str1)
        print(str2)
        assert str1 == str2
    
    # lst = [10, 2]
    # # lst.extend([5] * 5)
    # print(lst)
    # print(partition(lst, 0, len(lst), 10, key=lambda x: x))
    # print(lst)

