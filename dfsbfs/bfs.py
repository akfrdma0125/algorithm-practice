from collections import deque


def bfs(graph, queue, visited):
    if len(queue) == 0:
        return
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True  # 큐에 추가 -> 방문
            queue.append(i)
    bfs(graph, queue, visited)


def bfs_while(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)

queue = deque()
queue.append(1)
visited[1] = True

bfs(graph, queue, visited)
