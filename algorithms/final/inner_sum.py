def sum_in_arr(arr, _sum):
    s = set()
    for el in arr:
        if _sum - el in s:
            return True
        s.add(el)
    return False


def main():
    N = int(input())
    arr = list(map(int, input().split()))
    counter = 0
    for i, el in enumerate(arr):
        if sum_in_arr(arr[:i] + arr[i + 1:], el):
            counter += 1
    print(counter)


if __name__ == '__main__':
    main()
