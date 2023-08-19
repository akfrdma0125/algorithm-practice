from sys import stdin


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def get_graph():
    node = int(stdin.readline().rstrip())
    pair = int(stdin.readline().rstrip())
    graph = [[] for _ in range(node + 1)]
    for i in range(pair):
        x, y = map(int, stdin.readline().rstrip().split())
        graph[x].append(y)
        graph[y].append(x)
    return graph


graph = get_graph()
visited = [False] * len(graph)
dfs(graph, 1, visited)
print(visited.count(True) - 1)
