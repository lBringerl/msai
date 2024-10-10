def get_max_cost_table(ws, cs, w_max, n):
    d = [[0] * (w_max + 1) for _ in range(n + 1)]
    for i, (w_i, c_i) in enumerate(zip(ws, cs), 1):
        for w in range(1, w_max + 1):
            if w_i > w:
                d[i][w] = d[i - 1][w]
            else:
                d[i][w] = max(d[i - 1][w - w_i] + c_i, d[i - 1][w])
    return d


def restore(d, ws, w_max, n):
    w_rev = w_max
    i = n
    idxs = []
    while i > 0 and w_rev > 0:
        if d[i][w_rev] != d[i - 1][w_rev]:
            idxs.append(i)
            w_rev -= ws[i - 1]
        i -= 1
    return idxs[::-1]


if __name__ == '__main__':
    W, N = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    table = get_max_cost_table(weights, costs, W, N)
    idxs = restore(table, weights, W, N)
    print(table[-1][-1])
    print(len(idxs))
    print(' '.join(map(str, idxs)))
