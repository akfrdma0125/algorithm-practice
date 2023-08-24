from sys import stdin


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if apt[x][y] == 1:
        apt[x][y] = 0
        global count
        count += 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n = int(stdin.readline().rstrip())
apt = []
for _ in range(n):
    apt.append(list(map(int,stdin.readline().rstrip())))

result = 0
apt_num = []
count = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            apt_num.append(count)
            result += 1
            count = 0

print(result)
apt_num.sort()
for i in apt_num:
    print(i)