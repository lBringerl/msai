def sift_up(data, i):
    if i == 0:
        return
    parent = (i - 1) // 2
    if data[parent] > data[i]:
        data[parent], data[i] = data[i], data[parent]
        sift_up(data, parent)


def sift_down(data, i):
    child1 = i * 2 + 1
    child2 = i * 2 + 2
    if child1 >= len(data):
        return
    if child2 >= len(data):
        child_min = child1
    else:
        child_min = child1 if data[child2] > data[child1] else child2
    if data[child_min] < data[i]:
        data[child_min], data[i] = data[i], data[child_min]
        sift_down(data, child_min)


def heapify(data):
    for i in range(len(data) - 1, -1, -1):
        sift_down(data, i)


def heappush(data, x):
    data.append(x)
    sift_up(data, len(data) - 1)


def heappop(data, i=0):
    data[i], data[-1] = data[-1], data[i]
    res = data.pop()
    sift_up(data, i)
    sift_down(data, i)
    return res


if __name__ == '__main__':
    N = int(input())
    data = []
    for _ in range(N):
        _inp = input().split()
        if len(_inp) == 1:
            print(heappop(data)[1])
        else:
            n, v = int(_inp[1]), int(_inp[2])
            heappush(data, (-v, n))
