
# 문제 5719번 거의 최단 경로
# Graph(그래프), BFS(너비 우선 탐색), Dijkstra(다익스트라)


import sys, heapq
from collections import deque
r = sys.stdin.readline


def dijkstra():
  heap_data = []
  distances[s] = 0
  heapq.heappush(heap_data, (0, s))

  while heap_data:
    crr_dis, crr_node = heapq.heappop(heap_data)
    if distances[crr_node] < crr_dis:
      continue

    for adj in graph[crr_node]:
      new_dis = crr_dis + graph[crr_node][adj]
      if distances[adj] > new_dis:
        distances[adj] = new_dis
        heapq.heappush(heap_data, (new_dis, adj))


def bfs():
  # 도착점에서 부터 출발
  queue = deque([d])

  while queue:
    v = queue.popleft()
    if v == s:
      continue

    for prev, weight in re_graph[v]:
      # 현재 노드 거리 = 이전 노드 + 거리 (맞다면)
      if distances[v] == distances[prev] + weight:
        if (prev, v) not in remove_list:
          # 삭제 리스트에 추가
          remove_list.append((prev, v))
          queue.append(prev)


while True:
  n, m = map(int, r().split())
  if n == 0 and m == 0:
    break

  s, d = map(int, r().split())

  graph = [dict() for _ in range(n + 1)]
  re_graph = [[] for _ in range(n + 1)]

  for _ in range(m):
    u, v, p = map(int, r().split())

    graph[u][v] = p
    re_graph[v].append((u, p))
  
  remove_list = []
  distances = [float('inf') for _ in range(n + 1)]
  # 최단 거리 계산
  dijkstra()
  # 최단 거리로 갈 수 있는 노드 찾기
  bfs()
  # 최단 경로 제거
  for u, v in remove_list:
    del graph[u][v]

  distances = [float('inf') for _ in range(n + 1)]
  # 최단 거리로 가는 노드 제외하고 최단 거리 계산
  dijkstra()
  
  if distances[d] != float('inf'):
    print(distances[d])
  else:
    print(-1)







# def dijkstra(graph, s, d, flag):
#   heap_data = []
#   distances = [float('inf') for _ in range(len(graph))]
#   distances[s] = 0
#   heapq.heappush(heap_data, (distances[s], s))

#   while heap_data:
#     crr_dis, crr_node = heapq.heappop(heap_data)

#     if distances[crr_node] < crr_dis:
#       continue

#     for adj, weight in graph[crr_node]:
#       new_dis = weight + crr_dis

#       if distances[adj] >= new_dis:
#         if adj == d and flag != -1 and flag >= new_dis:
#           continue
#         distances[adj] = new_dis
#         heapq.heappush(heap_data, (new_dis, adj))
  
#   return distances[d]



# a = []
# while True:
#   n, m = map(int, r().split())
#   if n == 0 and m == 0:
#     break

#   s, d = map(int, r().split())

#   graph = [[] for _ in range(n + 1)]
#   re_graph = [[] for _ in range(n + 1)]
#   for _ in range(m):
#     u, v, p = map(int, r().split())

#     graph[u].append((v, p))
#     re_graph[v].append((u, p))

#   mst = dijkstra(graph, s, d, -1)
#   result = dijkstra(re_graph, d, s, mst)

#   if result != float('inf'):
#     # print(result)
#     a.append(result)
#   else:
#     # print(-1)
#     a.append(-1)

# print(a)








# 입력 예시
# 7 9
# 0 6
# 0 1 1
# 0 2 1
# 0 3 2
# 0 4 3
# 1 5 2
# 2 6 4
# 3 6 2
# 4 6 4
# 5 6 1
# 4 6
# 0 2
# 0 1 1
# 1 2 1
# 3 2 1
# 1 3 1
# 2 0 3
# 3 0 2
# 6 8
# 0 1
# 0 1 1
# 0 2 2
# 0 3 3
# 2 5 3
# 3 4 2
# 4 1 1
# 5 1 1
# 3 0 1
# 0 0

# 출력 예시
# 5
# -1
# 6