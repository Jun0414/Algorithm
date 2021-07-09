
# 문제 1325번 효율적인 해킹
# Graph(그래프), BFS(너비 우선 탐색), DFS(깊이 우선 탐색)
# PyPy3 제출


import sys
from collections import deque
r = sys.stdin.readline
# sys.setrecursionlimit(100000)


n, m = map(int, r().split())

graph = [[] for _ in range(n + 1)]
def bfs(start):
  visited = [0 for _ in range(n + 1)]
  visited[start] = 1
  queue = deque([start])
  cnt = 0

  while queue:
    v = queue.popleft()

    # 방문 노드 카운트
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = 1
        cnt += 1
  return cnt

for _ in range(m):
  a, b = map(int, r().split())
  graph[b].append(a)

result = []
max_hack = 0
for i in range(1, n + 1):
  hack = bfs(i)
  # 새로운 개수가 더 큰 경우
  if hack > max_hack:
    result = [i]
    max_hack = hack
  # 동일한 경우
  elif hack == max_hack:
    result.append(i)

# 최대 해킹 가능 컴퓨터 번호들
for i in result:
  print(i, end=' ')





# # dfs는 scc 알고리즘을 활용해야 풀이 가능(아래 코드는 맞는 것 같지만 오답처리...)
# n, m = map(int, r().split())

# def dfs(graph, visited, v):
#   visited[v] = 1

#   for i in graph[v]:
#     if visited[i] != 1:
#       return 1 + dfs(graph, visited, i)
#   return 1

# graph = [[] for _ in range(n + 1)]
# cnt = [0 for _ in range(n + 1)]
# for _ in range(m):
#   a, b = map(int, r().split())
#   graph[b].append(a)

# for i in range(1, n + 1):
#   visited = [0 for _ in range(n + 1)]
#   cnt[i] = dfs(graph, visited, i)

# max_hack = max(cnt)

# for i in range(1, n + 1):
#   if cnt[i] == max_hack:
#     print(i, end=' ')








# 입력 예시
# 5 4
# 3 1
# 3 2
# 4 3
# 5 3

# 6 5
# 3 1
# 3 2
# 4 3
# 5 3
# 1 6

# 12 11
# 2 1
# 3 2
# 4 2
# 5 1
# 2 5
# 6 7
# 7 8
# 8 9
# 9 10
# 10 11
# 11 12

# 출력 예시
# 1 2

# 6

# 12