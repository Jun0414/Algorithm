
# 예제 4-1 (상하좌우 p.110)

n = int(input())
x, y = 1, 1


# 내가 작성한 답안
data = list(map(str, input().split()))

for direct in data:
    if x == 1 and direct == 'U' or x == n and direct == 'D':
        continue
    if y == 1 and direct == 'L' or y == n and direct == 'R':
        continue

    if direct == 'U':
        x -= 1
    elif direct == 'D':
        x += 1
    elif direct == 'L':
        y -= 1
    else:   # (direct == 'R')
        y += 1


# 모범 답안
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)

# 입력 예시
# 5
# R R R U D D



#####################################################################
# 예제 4-2 (시각 p.113)

n = int(input())
cnt = 0


# 내가 작성한 답안
for hr in range(n + 1):
    if hr % 10 == 3:
        cnt += (60 * 60)
        continue
    for min in range(60):
        if min >= 30 and min < 40:
            cnt += 60
            continue
        if min % 10 == 3:
            cnt += 60
        for sec in range(60):
            if sec >= 30 and sec < 40:
                cnt += 1
                continue
            if sec % 10 == 3:
                cnt += 1

print(cnt)


# 모범 답안
cnt = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)

# 입력 예시
# 5



#####################################################################
# 실전문제 2 (왕실의 나이트 p.115)

point = input()


# 내가 작성한 답안
cnt = 0

row = int(point[1])
col = int(ord(point[0])) - int(ord('a')) + 1

if col - 2 > 0:
    if row - 1 > 0:
        cnt += 1
    if row + 1 < 9:
        cnt += 1
if col + 2 < 9:
    if row - 1 > 0:
        cnt += 1
    if row + 1 < 9:
        cnt += 1
if row - 2 > 0:
    if col - 1 > 0:
        cnt += 1
    if col + 1 < 9:
        cnt += 1
if row + 2 < 9:
    if col - 1 > 0:
        cnt += 1
    if col + 1 < 9:
        cnt += 1

print(cnt)


# 모범 답안
cnt = 0

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        cnt += 1

print(cnt)

# 입력 예시
# a1



#####################################################################
# 실전문제 3 (게임 개발 p.118)

n, m = map(int, input().split())


# 내가 작성한 답안

x, y, d = map(int, input().split())

# 방문자 체크
visit = [[0] * m for _ in range(n)]
visit[x][y] = 1

# n x m 행렬 만들기
data = [[int(x) for x in input().split()] for _ in range(n)]

# 방향 움직임 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1
turn_cnt = 0

while True:
    if d == 0:
        d = 3
    else:
        d -= 1
    nx = x + dx[d]
    ny = y + dy[d]

    if visit[nx][ny] == 0 and data[nx][ny] == 0:
        cnt += 1
        visit[nx][ny] = 1
        x = nx
        y = ny
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1

    if turn_cnt == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if visit[nx][ny] == 0 and data[nx][ny] == 0:
            x = nx
            y = ny
            turn_cnt = 0
        else:
            break

print(cnt)


# 모범 답안

d = [[0] * m for _ in range(n)]

x, y, direct = map(int, input().split())
d[x][y] = 1

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direct
    direct -= 1
    if direct == -1:
        direct = 3

cnt = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direct]
    ny = y + dy[direct]

    if d[nx][ny] == 0 and data[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direct]
        ny = y - dy[direct]

        if d[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)

# 입력 예시
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
