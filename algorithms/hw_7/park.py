from collections import deque


def bfs(park_map, waves_map, s):
    vertex_stack = deque([s])
    dir_y = [1, 0, -1, 0]
    dir_x = [0, 1, 0, -1]
    while vertex_stack:
        cur_y, cur_x = vertex_stack.popleft()
        waves_map[s[0]][s[1]] = 0
        length = waves_map[cur_y][cur_x]
        for x, y in zip(dir_y, dir_x):
            next_y = cur_y + y
            next_x = cur_x + x
            if next_y > len(park_map) - 1 or next_y < 0:
                continue
            if next_x > len(park_map[0]) - 1 or next_x < 0:
                continue
            if waves_map[next_y][next_x] != -1:
                continue
            if park_map[next_y][next_x] == '.':
                waves_map[next_y][next_x] = length + 1
                vertex_stack.append((next_y, next_x))
            elif park_map[next_y][next_x] == '#':
                continue
            elif park_map[next_y][next_x] == 'X':
                return length + 1
    return -1


def main():
    M, N = list(map(int, input().split()))
    park_map = []
    waves_map = []
    for i in range(M):
        inp_row = [c for c in input()]
        if 'E' in inp_row:
            s = (i, inp_row.index('E'))
        park_map.append(inp_row)
        waves_map.append([-1] * N)
    print(bfs(park_map, waves_map, s))


if __name__ == '__main__':
    main()
