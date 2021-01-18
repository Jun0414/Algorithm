
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
