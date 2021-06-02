
# ***
# 문제 4195번 친구 네트워크
# Union-Find(유니온 파인드)

import sys
r = sys.stdin.readline


def find(name):
  # 재귀로 부모 노드 찾기
  if parent[name] != name:
    parent[name] = find(parent[name])
  
  return parent[name]

def union(name1, name2):
  # 부모 노드 찾기
  root1 = find(name1)
  root2 = find(name2)

  # root1이 더 많이 연결되어 있다면
  if cnt[root1] > cnt[root2]:
    parent[root2] = root1
    cnt[root1] += cnt[root2]
  # root2가 더 많이 연결되어 있다면
  elif cnt[root2] > cnt[root1]:
    parent[root1] = root2
    cnt[root2] += cnt[root1]
  # 연결된 수가 동일하다면
  else:
    cnt[root2] += cnt[root1]
    parent[root1] = root2

# 노드당 초기화
def make_set(name):
  parent[name] = name
  cnt[name] = 1


case = int(r())

for _ in range(case):
  f = int(r())

  parent = dict()
  cnt = dict()
  for _ in range(f):
    name1, name2 = r().strip().split(' ')

    # 저장 안한 이름만 초기화
    if name1 not in parent:
      make_set(name1)
    if name2 not in parent:
      make_set(name2)

    # 서로 다른 집합인 경우
    if find(name1) != find(name2):
      union(name1, name2)

    # 최종 부모에 연결된 수 출력
    print(max(cnt[parent[name1]], cnt[parent[name2]]))
    # print(cnt[parent[name1]])







# 입력 예시
# 2
# 3
# Fred Barney
# Barney Betty
# Betty Wilma
# 3
# Fred Barney
# Betty Wilma
# Barney Betty

# 출력 예시
# 2
# 3
# 4
# 2
# 2
# 4