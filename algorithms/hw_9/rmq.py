from math import ceil, sqrt, floor


inf = (2 << 63) - 1


class RMQSqrtDecomposition:
    def __init__(self, a):
        N = len(a)
        self.k = max(int(ceil(sqrt(N))), 1)
        self.a = list(a)
        self.b = [inf] * (self.k + 2)

        for i, v in enumerate(self.a):
            self.b[i // self.k] = min(self.b[i // self.k], v)

    def rmq(self, l, r):
        l_block = self.k * int(ceil(l / self.k))
        r_block = self.k * int(floor(r / self.k))
        if l_block > r_block:
            return min(self.a[l:r])
        return min(self.a[l:l_block]
                   + self.b[l_block // self.k:r_block // self.k]
                   + self.a[r_block:r])

    def update(self, i, v):
        self.a[i] = v
        bi = i // self.k
        l = bi * self.k
        r = min(l + self.k, len(self.a))
        self.b[bi] = min(self.a[l:r])


if __name__ == '__main__':
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    s = RMQSqrtDecomposition(a)
    for i in range(M):
        c, l, r = input().split()
        l, r = int(l), int(r)
        if c == '?':
            print(s.rmq(l, r))
        else:
            s.update(l, r)
