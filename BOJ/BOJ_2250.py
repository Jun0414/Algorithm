
# 기초 고급 탐색
# 문제 2250번 트리의 높이와 너비
# Tree(트리), Graph Traversal(그래프 탐색)


import sys
r = sys.stdin.readline


class Node:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right
    self.parent = 0
    self.index = 0
    self.depth = 1

inc = 1
max_depth = 1
# 중위 순회로 index 부여
def in_order(node):
  global inc, max_depth
  
  # 자식으로 넘어갈 때 마다 깊이 증가
  if node.left != -1:
    tree[node.left].depth = node.depth + 1
    in_order(tree[node.left])
  
  node.index = inc
  inc += 1
  # 같은 깊이에서 인덱스 가장 큰 것과 가장 작은 것 찾기
  max_val[node.depth] = max(max_val[node.depth], node.index)
  min_val[node.depth] = min(min_val[node.depth], node.index)
  # 최대 깊이 갱신
  max_depth = max(max_depth, node.depth)
  
  # 자식으로 넘어갈 때 마다 깊이 증가
  if node.right != -1:
    tree[node.right].depth = node.depth + 1
    in_order(tree[node.right])



n = int(r())

min_val = [n]
max_val = [0]

tree = dict()
# 트리 구성 및 깊이마다 최대 최소 저장 공간 초기화
for i in range(1, n + 1):
  tree[i] = Node(i, -1, -1)
  min_val.append(n)
  max_val.append(0)

# 트리 내용 저장
for _ in range(n):
  data, left, right = map(int, r().split())
  tree[data].left = left
  tree[data].right = right

  if left != -1:
    tree[left].parent = data
  if right != -1:
    tree[right].parent = data

# root 노드 찾기
for child in range(1, n + 1):
  if tree[child].parent == 0:
    root = child

in_order(tree[root])

max_gap = 0
gap_indx = 1
# 각 깊이마다 (최대 - 최소 + 1) 의 값이 가장 큰 것 찾기
for num in range(1, max_depth + 1):
  if max_gap < max_val[num] - min_val[num] + 1:
    max_gap = max_val[num] - min_val[num] + 1
    gap_indx = num

print(gap_indx, max_gap)






# 입력 예시
# 19
# 1 2 3
# 2 4 5
# 3 6 7
# 4 8 -1
# 5 9 10
# 6 11 12
# 7 13 -1
# 8 -1 -1
# 9 14 15
# 10 -1 -1
# 11 16 -1
# 12 -1 -1
# 13 17 -1
# 14 -1 -1
# 15 18 -1
# 16 -1 -1
# 17 -1 19
# 18 -1 -1
# 19 -1 -1

# 출력 예시
# 3 18