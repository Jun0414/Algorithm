
# 문제 10473번 인간 대포
# Dijkstra(다익스트라), Graph(그래프)

import sys
import heapq
from math import sqrt
r = sys.stdin.readline
INF = 1e9


## 거리계산
def cal_dis(s_x, s_y, e_x, e_y):
  return sqrt(pow(s_x - e_x, 2) + pow(s_y - e_y, 2))

## 다익스트라
def dijkstra(graph, start):
  # 초기화
  distances = [INF] * len(graph)
  distances[start] = 0
  queue = []
  heapq.heappush(queue, [0, start])

  while queue:
    # 기준 설정
    curr_dis, curr_node = heapq.heappop(queue)

    # 현재거리보다 오래 걸리면 
    if distances[curr_node] < curr_dis:
      continue

    # 주변 거리 측정
    for adjacent, weight in graph[curr_node]:
      # 인접 대포 거리 측정
      new_dis = curr_dis + weight

      # 새로운 거리가 더 짧다면
      if new_dis < distances[adjacent]:
        distances[adjacent] = new_dis
        heapq.heappush(queue, [new_dis, adjacent])

  return distances


# 출발지, 목적지
start_x, start_y = map(float, r().split())
end_x, end_y = map(float, r().split())
n = int(r())

# 그래프 초기화
graph = [[] for _ in range(n + 2)]
spot = []
spot.append([start_x, start_y])

# 출발점에서 거리 계산
for i in range(1, n + 1):
  start, end = map(float, r().split())
  spot.append([start, end])
  graph[0].append([i, cal_dis(start_x, start_y, start, end) / 5])
spot.append([end_x, end_y])
graph[0].append([n + 1, cal_dis(start_x, start_y, end_x, end_y) / 5])

# 출발점과 도착점을 제외한 거리 계산
for i in range(1, n + 1):
  x1, y1 = spot[i]
  
  for j in range(1, n + 2):
    x2, y2 = spot[j]
    
    if i != j:
      with_cannon = 2 + abs(cal_dis(x1, y1, x2, y2) - 50) / 5
      without_cannon = cal_dis(x1, y1, x2, y2) / 5
      graph[i].append([j, min(with_cannon, without_cannon)])


total = dijkstra(graph, 0)
print(total[-1])





# 입력 예시
# 25.0 100.0
# 190.0 57.5
# 4
# 125.0 67.5
# 75.0 125.0
# 45.0 72.5
# 185.0 102.5

# 출력 예시
# 19.984901234215027