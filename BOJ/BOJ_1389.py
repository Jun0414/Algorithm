
# 문제 1389번 케빈 베이컨의 6단계 법칙
# Graph(그래프), dijkstra(다익스트라)


import sys, heapq
r = sys.stdin.readline


def dijkstra(graph, s):
  h_data = []
  distances = [1e9 for _ in range(len(graph))]
  distances[s] = 0
  heapq.heappush(h_data, (0, s))

  while h_data:
    curr_dis, curr_node = heapq.heappop(h_data)

    if distances[curr_node] < curr_dis:
      continue
    
    for adjacent in graph[curr_node]:
      new_dis = curr_dis + 1

      if distances[adjacent] > new_dis:
        distances[adjacent] = new_dis
        heapq.heappush(h_data, (new_dis, adjacent))
  
  return sum(distances[1:])


n, m = map(int, r().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  s, d = map(int, r().split())
  graph[s].append(d)
  graph[d].append(s)

result = [1e9]
for i in range(1, n + 1):
  result.append(dijkstra(graph, i))

print(result.index(min(result)))






# 입력 예시
# 5 5
# 1 3
# 1 4
# 4 5
# 4 3
# 3 2

# 출력 예시
# 3