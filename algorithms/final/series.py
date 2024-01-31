def main():
    n, a = list(map(int, input().split()))
    if a != 1:
        return (n * pow(a, n + 2) - (n + 1) * pow(a, n + 1) + a) // pow(a - 1, 2)
    return n * (n + 1) // 2


if __name__ == '__main__':
    print(main())
