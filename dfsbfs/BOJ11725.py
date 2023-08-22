from collections import deque
import sys

def write(*args):
    for arg in args:
        sys.stdout.write(str(arg))


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                result[i] = v


def get_graph(node, pair):
    graph = [[] for _ in range(node + 1)]
    for i in range(pair):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[x].append(y)
        graph[y].append(x)
    for i in graph:
        i.sort()
    return graph


node = int(sys.stdin.readline().rstrip())
graph = get_graph(node, node - 1)
result = [0] * len(graph)
visited = [False]*len(graph)
bfs(1)
write('\n'.join(map(str, result[2:])))