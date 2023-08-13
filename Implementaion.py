# 상하좌우 : 시뮬레이션
def get_destination():
    N = int(input())
    direction = [plan for plan in input().split()]

    x = y = 0

    # 동, 북, 서, 남
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    # 매핑
    movement = dict()
    movement['R'] = 0
    movement['U'] = 1
    movement['L'] = 2
    movement['D'] = 3

    for plan in direction:
        idx = movement.get(plan)
        nx = x + dx[idx]
        ny = y + dy[idx]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        x, y = nx, ny
    print(x, y)


# 시각: 문제 조건
# 모든 시간의 경우를 다 더해봐야 86400이므로 완전 탐색
def get_count_time():
    N = int(input())
    count = 0

    for i in range(N + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    print(count)


def get_location():
    temp = input()
    x = ord(temp[0]) - 96
    y = int(temp[1])

    # 완전 탐색
    # 북, 서, 남, 동
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    N = 8
    count = 0
    for i in range(4):
        tx = x + 2 * dx[i]
        ty = y + 2 * dy[i]
        print(f'tx: {tx}, ty: {ty}')
        if tx < 1 or ty < 1 or tx > N or ty > N:
            print("자격미달!!")
            continue
        for j in range(2):
            idx = (i + 1 + 2 * j) % 4
            nx = tx + dx[idx]
            ny = ty + dy[idx]
            if nx < 1 or ny < 1 or nx > N or ny > N:
                continue
            count += 1
            print(f'x: {nx} y:{ny}')
    print(count)


def get_location_solution():
    input_data = input()
    row = ord(input_data[0]) - int(ord('a')) + 1  # 아스키코드 검색(X), 변환(O)
    column = int(input_data[1])

    # 완전 탐색
    # 모든 경우가 겨우 8개 > 배열에 정의
    steps = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    ]
    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = row + step[1]
        if 1 <= next_row <= 8 and 1 <= next_column <= 8:
            result += 1

    print(result)


# K1KA5CB7
def resort_string():
    input_data = input()
    input_data = sorted(input_data)
    result = ""
    result_number = 0
    for i in input_data:
        if '0' <= i <= '9':
            result_number += int(i)
            continue
        result += i
    result += str(result_number)
    print(result)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

def play_game():
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    region = []

    # 육지: 0, 바다: 1, 방문: 2
    for i in range(n):
        region.append(input().split())

    # 북, 동, 남, 서
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    region[y][x] = '2'

    i = 1
    answer = 1
    while True:
        nd = (d - i) % 4
        if d == nd: #같다면?
            # 한 칸 뒤로!
            x = dx[nd - 2]
            y = dx[nd - 2]
            if region[x][y] == '1' or not( 0 <= nx < n and 0 <= ny < m):
                print(answer)
                return
        nx = x + dx[nd]
        ny = y + dy[nd]
        # 경계선이 아니거나, 바다가 아니거나, 방문한 곳이 아니거나!
        if 0 <= nx < m and 0 <= ny < n and region[ny][nx] == '0':
            x, y, d = nx, ny, nd
            region[ny][nx] = '2'
            answer += 1
            continue
        i += 1