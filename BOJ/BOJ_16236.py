
# 문제 16236번 아기 상어
# Graph(그래프), BFS(너비 우선 탐색)


import sys, heapq
r = sys.stdin.readline


def bfs(s_x, s_y):
  q = []
  heapq.heappush(q, (0, s_x, s_y))
  near = []
  visited = set()
  visited.add((s_x, s_y))

  # 움직일 방향
  directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

  while q:
    cnt, x, y = heapq.heappop(q)

    for dx, dy in directions:
      nx, ny = (x + dx), (y + dy)
      # 새로운 위치가 범위 안
      if nx >= 0 and ny >= 0 and nx < n and ny < n:
        # 상어보다 크면
        if arr[nx][ny] > shark_size:
          continue
        # 방문한 적은 없으나 상어와 크기가 동일하거나 물고기가 없는 칸
        elif (arr[nx][ny] == shark_size or arr[nx][ny] == 0) and (nx, ny) not in visited:
          heapq.heappush(q, (cnt + 1, nx, ny))
          visited.add((nx, ny))
        # 방문한적 없고 상어보다 작은 물고기 칸
        elif arr[nx][ny] < shark_size and (nx, ny) not in visited:
          heapq.heappush(near, (cnt + 1, nx, ny))
          visited.add((nx, ny))
  
  # 가장 가까운 물고기 반환
  if near:
    return heapq.heappop(near)
  # 물고기가 없는 경우
  else:
    return (-1, -1, -1)


n = int(r())

# 상어 및 물고기 위치 파악
shark = ()
arr = [list(map(int, r().split())) for _ in range(n)]
for i in range(n):
  for j in range(n):
    if arr[i][j] == 9:
      shark = (i, j)
      arr[i][j] = 0
      break

shark_size = 2
eat_cnt = 0
total_dis = 0

while True:
  fish = bfs(shark[0], shark[1])
  # 먹은 물고기가 없는 경우
  if fish[0] == -1:
    break

  # 잡은 물고기 상태 변경
  arr[fish[1]][fish[2]] = 0
  # 상어 위치 갱신
  shark = (fish[1], fish[2])
  # 움직인 거리 계산
  total_dis += fish[0]

  eat_cnt += 1
  # 상어 사이즈 조정
  if eat_cnt == shark_size:
    shark_size += 1
    eat_cnt = 0

print(total_dis)





# 입력 예시
# 3
# 0 0 0
# 0 0 0
# 0 9 0

# 3
# 0 0 1
# 0 0 0
# 0 9 0

# 4
# 4 3 2 1
# 0 0 0 0
# 0 0 9 0
# 1 2 3 4

# 6
# 5 4 3 2 3 4
# 4 3 2 3 4 5
# 3 2 9 5 6 6
# 2 1 2 3 4 5
# 3 2 1 6 5 4
# 6 6 6 6 6 6

# 6
# 6 0 6 0 6 1
# 0 0 0 0 0 2
# 2 3 4 5 6 6
# 0 0 0 0 0 2
# 0 2 0 0 0 0
# 3 9 3 0 0 1

# 6
# 1 1 1 1 1 1
# 2 2 6 2 2 3
# 2 2 5 2 2 3
# 2 2 2 4 6 3
# 0 0 0 0 0 6
# 0 0 0 0 0 9

# 출력 예시
# 0

# 3

# 14

# 60

# 48

# 39