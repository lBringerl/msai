from bisect import bisect_left


INF = 10001


def LIS(seq):
    d = [-1] + [INF] * len(seq)
    for x in seq:
        l = bisect_left(d, x)
        d[l] = x
    return bisect_left(d, INF) - 1


if __name__ == '__main__':
    N = int(input())
    X = list(map(int, input().split()))
    print(LIS(X))
