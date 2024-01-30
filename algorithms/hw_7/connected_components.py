from collections import defaultdict


def dfs(g, s, visited, color=1):
    vertex_stack = [s]
    while vertex_stack:
        v = vertex_stack.pop()
        if visited[v] == 0:
            visited[v] = color
            for u in g[v]:
                if visited[u] == 0:
                    vertex_stack.append(u)


def reverse_dct(dct):
    res_dct = defaultdict(list)
    for k, v in dct.items():
        res_dct[v].append(k)
    return res_dct


def main():
    N, M = list(map(int, input().split()))
    G = defaultdict(list)
    visited = defaultdict(int)
    for _ in range(M):
        v1, v2 = list(map(int, input().split()))
        G[v1].append(v2)
        G[v2].append(v1)
        visited[v1] = 0
        visited[v2] = 0
    count = 1
    dfs(G, 0, visited, color=count)
    for i in range(N):
        if not visited[i]:
            count += 1
            dfs(G, i, visited, color=count)
    rev_visited = reverse_dct(visited)
    print(len(rev_visited.keys()))
    for v in rev_visited.values():
        print(len(v))
        print(' '.join(map(str, v)))


if __name__ == '__main__':
    main()
