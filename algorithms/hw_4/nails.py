INF = 10**9


def find_min_length(coords):
    l = len(coords)
    d = [INF, coords[1] - coords[0]] + [INF] * (l - 2)
    for i in range(2, l):
        d[i] = coords[i] - coords[i - 1] + min(d[i - 1], d[i - 2])
    return d[l - 1]


if __name__ == '__main__':
    N = int(input())
    nails = sorted(list(map(int, input().split())))
    print(find_min_length(nails))
