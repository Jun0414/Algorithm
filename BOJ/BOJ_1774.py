
# 문제 1774번 우주신과의 교감
# Graph(그래프), MST(최소 신장 트리), Kruskal(크루스칼 알고리즘), Union-find(유니온-파인드 알고리즘)


import sys
from math import sqrt
r = sys.stdin.readline


def get_distance(v1, v2):
  d1 = abs(v1[0] - v2[0])
  d2 = abs(v1[1] - v2[1])
  return sqrt((d1 * d1) + (d2 * d2))


def find(v):
  # 현재 v가 root가 아닌 경우
  if parent[v] != v:
  # 현재 v가 root일때 까지 재귀로 찾아서 반환
    parent[v] = find(parent[v])
  
  return parent[v]


def union(v1, v2):
  root1 = find(v1)
  root2 = find(v2)

  # 같은 트리인 경우
  if root1 == root2:
    return
  # root1의 깊이가 더 깊은 경우
  if rank[root1] > rank[root2]:
    parent[root2] = root1
  # root2의 깊이가 더 깊거나 동일한 경우
  else:
    parent[root1] = root2
    # 깊이가 동일하면(root1의 부모를 root2로 설정 했으므로)
    if rank[root1] == rank[root2]:
      rank[root2] += 1


# 크루스칼 알고리즘
def kruskal(edges):
  # 비용 낮은 순으로 정렬
  edges.sort(key=lambda x: x[2])
  total = 0
  for v1, v2, cost in edges:
    # 서로 다른 집합인 경우
    if find(v1) != find(v2):
      union(v1, v2)
      total += cost

  return total


n, m = map(int, r().split())

# 깊이와 부모노드 초기화
rank = {v: 0 for v in range(1, n + 1)}
parent = {v: v for v in range(1, n + 1)}

locations = dict()
for i in range(n):
  # 정점 좌표 저장
  x, y = map(int, r().split())
  locations[i + 1] = (x, y)

edges = []
for i in range(1, n):
  # 간선 추가
  for j in range(i + 1, n + 1):
    edges.append((i, j, get_distance(locations[i], locations[j])))

for i in range(m):
  # 주어진 간선 연결
  v1, v2 = map(int, r().split())
  union(v1, v2)

print("%.2f" %(kruskal(edges)))