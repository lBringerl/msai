from collections import defaultdict, deque


def dfs(g, s, visited):
    vertex_stack = deque([s])
    while vertex_stack:
        s = vertex_stack.pop()
        for v in g[s]:
            if not visited[v]:
                vertex_stack.append(v)


def main():
    N, M = list(map(int, input().split()))
    G = defaultdict(list)
    visited = defaultdict(bool)
    for _ in M:
        v1, v2 = list(map(int, input().split()))
        G[v1].append(v1)
        G[v2].append(v2)
    dfs(G, visited, )


if __name__ == '__main__':
    main()
