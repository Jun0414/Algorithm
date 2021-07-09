
# 문제 10282번 해킹
# Graph(그래프), Dijkstra(다익스트라)


import sys, heapq
r = sys.stdin.readline


t = int(r())

def dijkstra(graph, start, n):
  # 컴퓨터 개수 만큼 생성
  distances = {node: float('inf') for node in range(1, n + 1)}
  distances[start] = 0

  queue = []
  heapq.heappush(queue, [distances[start], start])

  while queue:
    current_dis, current_node = heapq.heappop(queue)

    if distances[current_node] < current_dis:
      continue
    if current_node in graph:
      for adj, weight in graph[current_node].items():
        new_dis = weight + current_dis

        if distances[adj] > new_dis:
          distances[adj] = new_dis
          heapq.heappush(queue, [new_dis, adj])
  return distances


for _ in range(t):
  # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 개수
  n, d, c = map(int, r().split())

  graph = dict()
  for _ in range(d):
    # a 가 b를 의존, s초 뒤에 a 감염
    a, b, s = map(int, r().split())

    # b 키가 없다면 생성
    if b not in graph.keys():
      graph[b] = {a: s}
    # b 키가 있다면 추가
    else:
      graph[b].update({a: s})
    
  result = dijkstra(graph, c, n)

  cnt = 0
  max_dis = 0
  for key, value in result.items():
    if value != float('inf'):
      cnt += 1
      if max_dis < value:
        max_dis = value
  print(cnt, max_dis)






# 입력 예시
# 2
# 3 2 2
# 2 1 5
# 3 2 5
# 3 3 1
# 2 1 2
# 3 1 8
# 3 2 4

# 출력 예시
# 2 5
# 3 6