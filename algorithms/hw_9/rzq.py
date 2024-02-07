class RSQFenwick:
    def __init__(self, N):
        self.N = N
        self.f = [0] * self.N

    def query(self, i):
        res = 0
        while i >= 0:
            res += self.f[i]
            i -= ~i & (i + 1)
        return res

    def update(self, i, delta):
        while i < self.N:
            self.f[i] += delta
            i += ~i & (i + 1)

    def rsq(self, left, right):
        return self.query(right - 1) - self.query(left - 1)


if __name__ == '__main__':
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    f = RSQFenwick(N)
    for i, v in enumerate(a):
        if v == 0:
            f.update(i, 1)
    for i in range(M):
        c, l, r = input().split()
        l = int(l)
        r = int(r)
        if c == '?':
            print(f.rsq(l, r))
        else:
            delta = (a[l] + r == 0) - (a[l] == 0)
            a[l] += r
            if delta:
                f.update(l, delta)
