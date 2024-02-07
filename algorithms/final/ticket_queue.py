import heapq


def main():
    N, K = map(int, input().split())
    delays = list(map(int, input().split()))
    if K >= N:
        return max(delays)
    if K == 1:
        return sum(delays)
    windows = delays[:K]
    heapq.heapify(windows)
    for t in delays[K:]:
        if t == 0:
            continue
        windows[0] += t
        if len(windows) == 2 and windows[0] > windows[1]:
            zero = heapq.heappop(windows)
            heapq.heappush(windows, zero)
        elif len(windows) > 2 and windows[0] > min(windows[1], windows[2]):
            zero = heapq.heappop(windows)
            heapq.heappush(windows, zero)
    return max(windows[K // 2:])


if __name__ == '__main__':
    print(main())
