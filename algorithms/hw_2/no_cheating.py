def l_binary_search(coords, m):
    l = -1
    r = coords[-1]
    while r - l > 1:
        dist = (r + l) // 2
        if can_place(coords, dist, m):
            l = dist
        else:
            r = dist
    return l


def can_place(coords, dist, m):
    n = 1
    last_seat = coords[0]
    for coord in coords[1:]:
        if coord - last_seat < dist:
            continue
        n += 1
        last_seat = coord
    if n >= m:
        return True
    return False


def main():
    _, M = map(int, input().split())
    coords = list(map(int, input().split()))
    coords.sort()
    dist = l_binary_search(coords, M)
    print(dist)



if __name__ == '__main__':
    main()
