def get_max_cost_table(ws, cs, w_max, n):
    d = [[0] * (w_max + 1) for _ in range(n)]
    for i, (w_i, c_i) in enumerate(zip(ws, cs)):
        for w in range(1, w_max + 1):
            if w_i > w:
                d[i][w] = d[i - 1][w]
            else:
                d[i][w] = max(d[i - 1][w - w_i] + c_i, d[i - 1][w])
    return d


def restore(d, ws, w_max, n):
    w_rev = w_max
    idxs = []
    for i in range(n - 1, -1, -1):
        if d[i][w_rev] != d[i - 1][w_rev]:
            idxs.append(i)
            w_rev -= ws[i]
    return idxs[::-1]


if __name__ == '__main__':
    W, N = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    data = sorted(zip(weights, costs, range(N)), key=lambda t: (t[0], t[1]))
    weights_sorted = map(lambda t: t[0], data)
    cost_sorted = map(lambda t: t[1], data)
    table = get_max_cost_table(weights_sorted, cost_sorted, W, N)
    max_cost = table[N - 1][W]
    weights_sorted_lst = list(map(lambda t: t[0], data))
    idxs_sorted = restore(table, weights_sorted_lst, W, N)
    print(max_cost)
    print(len(idxs_sorted))
    for sorted_idx in idxs_sorted:
        print(f'{data[sorted_idx][2] + 1} ', end='')
