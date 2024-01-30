def is_sum(ws):
    N = len(ws)
    W = sum(ws)
    if W % 2 != 0:
        return False
    W = W // 2
    d = [[True] + [False] * W for _ in range(N + 1)]
    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if ws[i - 1] > w:
                d[i][w] = d[i - 1][w]
            else:
                d[i][w] = d[i - 1][w] or d[i - 1][w - ws[i - 1]]
    return d[N][W]


if __name__ == '__main__':
    N = int(input())
    costs = list(map(int, input().split()))
    if is_sum(costs):
        print('YES')
    else:
        print('NO')
