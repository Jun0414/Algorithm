
# 기초 고급 탐색
# 문제 1991번 트리 순회
# Tree(트리), Recursion(재귀)
# 전위 순회 : 루트 - 왼쪽 - 오른쪽
# 중위 순회 : 왼쪽 - 루트 - 오른쪽
# 후위 순회 : 왼쪽 - 오른쪽 - 루트
# 클래스 사용 예시


import sys
r = sys.stdin.readline


def pre_order(start):
  left = tree[start][0]
  right = tree[start][1]

  print(start, end='')

  if left != '.':
    pre_order(left)
  if right != '.':
    pre_order(right)


def in_order(start):
  left = tree[start][0]
  right = tree[start][1]

  if left != '.':
    in_order(left)
  
  print(start, end='')
  
  if right != '.':
    in_order(right)


def post_order(start):
  left = tree[start][0]
  right = tree[start][1]

  if left != '.':
    post_order(left)
  if right != '.':
    post_order(right)

  print(start, end='')

n = int(r())

tree = dict()
for _ in range(n):
  node, left, right = r().split()
  tree[node] = (left, right)

pre_order('A')
print()
in_order('A')
print()
post_order('A')



# # 클래스 사용 예시
# class Node:
#   def __init__(self, data, left, right):
#     self.data = data
#     self.left = left
#     self.right = right

# def pre_order(node):
#   print(node.data, end='')
#   if node.left != '.':
#     pre_order(tree[node.left])
#   if node.right != '.':
#     pre_order(tree[node.right])

# for _ in range(n):
#   data, left, right = r().split()
#   tree[data] = Node(data, left, right)

# pre_order(tree['A'])





# 입력 예시
# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .

# 출력 예시
# ABDCEFG
# DBAECFG
# DBEGFCA