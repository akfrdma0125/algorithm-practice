from sys import stdin


# 재귀 구조가 스택이므로 이걸 이용하는 거 자체가 dfs
# 1. 일단 방문 처리를 하고
# 2. 스택 구조를 이용함

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == '0':
        graph[x][y] = '1'
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
graph = [list(stdin.readline().rstrip()) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
