inf = (2 << 63) - 1


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


def dijkstra(G, N, s):
    heap = []
    d = [inf] * N
    p = [-1] * N
    v = -1
    S = {-1}
    d[s] = 0
    heappush(heap, (d[s], s))
    while heap:
        while v in S and heap:
            v = heappop(heap)[1]
        if v not in S:
            S.add(v)
            for u in G[v]:
                new_d = d[v] + G[v][u]
                if new_d < d[u]:
                    heappush(heap, (new_d, u))
                    d[u] = new_d
                    p[u] = v
    return d, p


def main():
    N, M = list(map(int, input().split()))
    s, h = list(map(int, input().split()))
    G = [{} for i in range(N)]
    for _ in range(M):
        u, v, w = list(map(int, input().split()))
        G[u][v] = w
        G[v][u] = w
    d, p = dijkstra(G, N, s)
    if d[h] == inf:
        return [], -1
    path = []
    v = h
    while v != -1:
        path.append(v)
        v = p[v]
    return path[::-1], d[h]


if __name__ == '__main__':
    path, w = main()
    print(w)
    if path:
        print(len(path))
        print(' '.join(map(str, path)))
