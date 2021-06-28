
# 기초 그래프 기본 탐색
# 문제 1260번 DFS와 BFS
# Graph Searching(그래프 탐색), DFS(깊이 우선 탐색), BFS(너비 우선 탐색)


import sys
from collections import deque
r = sys.stdin.readline


def dfs(start):
  print(start, end=' ')
  visited[start] = 1
  
  for i in graph[start]:
    if visited[i] == 0:
      dfs(i)


def bfs(start):
  bfs_heap = deque()
  bfs_heap.append(start)

  while bfs_heap:
    node = bfs_heap.popleft()
    
    if visited[node] == 0:
      visited[node] = 1
      print(node, end=' ')
      for i in graph[node]:
        if visited[i] == 0:
          bfs_heap.append(i)


n, m, v = map(int, r().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
  node1, node2 = map(int, r().split())
  graph[node1].append(node2)
  graph[node2].append(node1)

for e in graph:
  e.sort()

visited = [0] * (n + 1)
dfs(v)
print()
visited = [0] * (n + 1)
bfs(v)





# 입력 예시
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1

# 1000 1 1000
# 999 1000

# 출력 예시
# 1 2 4 3
# 1 2 3 4

# 3 1 2 5 4
# 3 1 4 2 5

# 1000 999
# 1000 999