import random


def partition(x, l, r, pivot):
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


def qsort(x, l=0, r=None):
    if r is None:
        r = len(x)
    if (r - l) > 1:
        pivot = x[random.randint(l, r - 1)]
        il, ir = partition(x, l, r, pivot)
        qsort(x, l, il)
        qsort(x, ir, r)


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
    qsort(bunches)
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
