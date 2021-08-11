
# 문제 10026번 적록색약
# Graph(그래프), bfs(너비 우선 탐색)


import sys
from collections import deque
r = sys.stdin.readline


directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = 1

  while q:
    v = q.popleft()

    for dx, dy in directions:
      nx, ny = (dx + v[0]), (dy + v[1])
      if nx >= 0 and ny >= 0 and nx < n and ny < n and visited[nx][ny] == 0 and arr[v[0]][v[1]] == arr[nx][ny]:
        q.append((nx, ny))
        visited[nx][ny] = 1


n = int(r())
arr = [list(map(str, r())) for _ in range(n)]

normal = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      bfs(i, j)
      normal += 1
    if arr[i][j] == 'R':
      arr[i][j] = 'G'

amnormal = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      bfs(i, j)
      amnormal += 1

print(normal, amnormal)