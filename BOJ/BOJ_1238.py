
# 문제 1238번 파티
# Dijkstra(다익스트라), Graph(그래프)

import sys
import heapq
r = sys.stdin.readline
INF = 1e9


# 방법1 (arr 를 이용)

# 다익스트라 함수
def dijkstra(start, graph):
  # 초기화
  distances = [INF] * len(graph)
  distances[start] = 0
  queue = []
  heapq.heappush(queue, [distances[start], start])

  while queue:
    # 큐에서 pop
    current_distance, current_node = heapq.heappop(queue)

    # 현재거리보다 오래 걸리면 
    if distances[current_node] < current_distance:
      continue

    # 현재 노드에서 인접한 노드 거리 계산
    for adjacent, weight in graph[current_node]:
      distance = current_distance + weight

      # 더 짧은 거리가 나오면 갱신
      if distance < distances[adjacent]:
        distances[adjacent] = distance
        heapq.heappush(queue, [distance, adjacent])

  return distances

n, m, x = map(int, r().split())
graph = [[] for _ in range(n + 1)]

# 정보 입력
for _ in range(m):
  start, end, weight = map(int, r().split())
  graph[start].append([end, weight])


result = []
# 오는 거리 계산을 위해
from_party = dijkstra(x, graph)

# 왕복 거리 저장
for num in range(1, n + 1):
  home = dijkstra(num, graph)
  result.append(home[x] + from_party[num])

print(max(result))


# 방법2 (dictionary 를 이용)

# def dijkstra(start, graph):
#   distances = {node: INF for node in graph}
#   distances[start] = 0
#   queue = []
#   heapq.heappush(queue, [distances[start], start])

#   while queue:
#     current_distance, current_node = heapq.heappop(queue)

#     if distances[current_node] < current_distance:
#       continue

#     for adjacent, weight in graph[current_node].items():
#       distance = current_distance + weight

#       if distance < distances[adjacent]:
#         distances[adjacent] = distance
#         heapq.heappush(queue, [distance, adjacent])

#   return distances



# # 마을: 가중치
# graph = {}

# n, m, x = map(int, r().split())

# # 이중 사전을 사용하기 위해 각 마을의 사전을 초기화
# for i in range(1, n + 1):
#   graph[i] = {}

# for i in range(m):
#   start, end, weight = map(int, r().split())
#   graph[start][end] = weight

# result = {}

# for home in range(1, n + 1):
#   result[home] = dijkstra(home, graph)

# longest = 0

# for num in range(1, n + 1):
#   total_dis = result[num][x] + result[x][num]

#   if longest < total_dis:
#     longest = total_dis

# print(longest)







# 입력 예시
# 4 8 2
# 1 2 4
# 1 3 2
# 1 4 7
# 2 1 1
# 2 3 5
# 3 1 2
# 3 4 4
# 4 2 3

# 출력 예시
# 10