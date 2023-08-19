from collections import deque
from sys import stdin


def dfs(v):
    visited[v] = True
    dfs_path.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        bfs_path.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def get_graph(node, pair):
    graph = [[] for _ in range(node + 1)]
    for i in range(pair):
        x, y = map(int, stdin.readline().rstrip().split())
        graph[x].append(y)
        graph[y].append(x)
    for i in graph:
        i.sort()
    return graph


node, pair, start = map(int, stdin.readline().rstrip().split())
graph = get_graph(node, pair)
dfs_path = []
visited = [False] * len(graph)
dfs(start)
bfs_path=[]
visited = [False] * len(graph)
bfs(start)
print(*dfs_path)
print(*bfs_path)
