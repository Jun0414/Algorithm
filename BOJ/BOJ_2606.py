
# 문제 2606번 바이러스
# Graph(그래프), BFS(너비 우선 탐색), DFS(깊이 우선 탐색)


import sys
from collections import deque
r = sys.stdin.readline


n = int(r())
m = int(r())

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = 1

  while queue:
    v = queue.popleft()

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = 1


graph = [[] for _ in range(n + 1)]
for _ in range(m):
  s, e = map(int, r().split())
  graph[s].append(e)
  graph[e].append(s)

visited = [0 for _ in range(n + 1)]
bfs(graph, 1, visited)

print(visited.count(1) - 1)







# 입력 예시
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

# 출력 예시
# 4