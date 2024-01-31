def main():
    N, M = list(map(int, input().split()))
    qs = sorted(list(map(int, input().split())))
    count = 0
    mins = 0
    for q in qs:
        mins += q
        if mins > M:
            break
        count += 1
    return count


if __name__ == '__main__':
    print(main())
