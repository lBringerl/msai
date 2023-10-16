def r_binary_search(lst, el):
    l = -1
    r = len(lst)
    while r - l > 1:
        m = (r + l) // 2
        if lst[m] <= el:
            l = m
        else:
            r = m
    return r


def l_binary_search(lst, el):
    l = -1
    r = len(lst)
    while r - l > 1:
        m = (r + l) // 2
        if lst[m] < el:
            l = m
        else:
            r = m
    return r


def main():
    N, M = map(int, input().split())
    scores = sorted(list(map(int, input().split())))
    for _ in range(M):
        l, r = map(int, input().split())
        l_res, r_res = l_binary_search(scores, l), r_binary_search(scores, r)
        print(r_res - l_res)


if __name__ == '__main__':
    main()
