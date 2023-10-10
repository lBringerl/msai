import random


def partition(x, l, r, pivot, key):
    for i, el in enumerate(x[l:r], l):
        if key(el) == pivot:
            il = ir = i
            break
    r -= 1
    while l < il and r > ir:
        while l < il and key(x[l]) <= pivot:
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


def main():
    N, W = map(int, input().split())
    capacity = W
    bunches = []
    total_cost = 0
    for i in range(N):
        c, w = map(int, input().split())
        if c == 0:
            continue
        if w == 0:
            total_cost += c
            continue
        bunches.append((W * c // w, c, w))
    if capacity == 0:
        print(total_cost)
        return
    qsort(bunches, key=lambda x: x[0])
    for i in range(len(bunches) - 1, -1, -1):
        c, w = bunches[i][1], bunches[i][2]
        if w > capacity:
            total_cost += c * capacity // w
            capacity = 0
            break
        total_cost += c
        capacity -= w
        if capacity == 0:
            break
    print(total_cost)


if __name__ == '__main__':
    main()
