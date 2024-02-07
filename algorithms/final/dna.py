def combine(n):
    d = [[0] * 3 for _ in range(n + 1)]
    d[0][0] = 1
    for i in range(1, n + 1):
        d[i][0] = 3 * (d[i - 1][0] + d[i - 1][1] + d[i - 1][2])
        d[i][1] = d[i - 1][0]
        d[i][2] = d[i - 1][1]
    return d[n][0] + d[n][1] + d[n][2]


def main():
    N = int(input())
    print(combine(N))


if __name__ == '__main__':
    main()
