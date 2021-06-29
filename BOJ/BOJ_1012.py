
# 문제 1012번 유기농 배추
# Graph(그래프), BFS(너비 우선 탐색), DFS(깊이 우선 탐색)


import sys
from collections import deque
r = sys.stdin.readline


t = int(r())

def bfs(graph, x, y, visited):
  queue = deque([(x, y)])

  visited[x][y] = 1
  # 상하좌우 탐색 위해
  directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

  while queue:
    vx, vy = queue.popleft()

    for dx, dy in directions:
      # 상하좌우 좌표
      nx, ny = (dx + vx), (dy + vy)

      # 최대, 최소 범위 밖인 경우
      if nx < 0 or nx >= m or ny < 0 or ny >= n:
        continue
      # 범위 안인 경우
      if not visited[nx][ny] and graph[nx][ny] == 1:
        queue.append((nx, ny))
        visited[nx][ny] = 1

for _ in range(t):
  m, n, k = map(int, r().split())

  # 필요한 벌레 수
  cnt = 0
  # 배추 심은 위치 저장
  xy = []
  arr = [[0 for _ in range(n)] for _ in range(m)]
  visited = [[0 for _ in range(n)] for _ in range(m)]
  for _ in range(k):
    x, y = map(int, r().split())
    arr[x][y] = 1
    xy.append((x, y))

  # 모여있는 배추 찾기
  for xx, yy in xy:
    if visited[xx][yy] != 1:
      bfs(arr, xx, yy, visited)
      cnt += 1
  print(cnt)








# 입력 예시
# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5

# 1
# 5 3 6
# 0 2
# 1 2
# 2 2
# 3 2
# 4 2
# 4 0

# 출력 예시

# 5
# 1

# 2