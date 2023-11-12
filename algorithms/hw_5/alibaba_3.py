def get_max_cost(ws, cs, w):
    d = [[0] * w for _ in range(len(ws))]
    for i in range(1, len(ws)):
        for j, (w_j, c_j) in enumerate(zip(ws, cs), 1):
            if w_j > w:
                d[i][w_j] = d[i - 1][w_j]
            else:
                d[i][w_j] = max(d[i - 1][w - w_j] + c_j, d[i - 1][w_j])
    print(d)
    return d[len(ws) - 1][w - 1]


if __name__ == '__main__':
    W, N = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    print(get_max_cost(weights, costs, W))
