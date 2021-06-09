
# 기초 그래프 기본 탐색
# 문제 1697번 숨바꼭질
# Graph Searching(그래프 탐색), BFS(너비 우선 탐색)


import sys
from collections import deque
r = sys.stdin.readline


def bfs(start):
  queue = deque()
  queue.append(start)
  visited[start] = 1

  while queue:
    node = queue.popleft()

    # k위치 찾았을 시
    if node == k:
      return cnt[node]
    # 다음 자식 노드 구하기
    for next in (node - 1, node + 1, node * 2):
      if 0 <= next <= 100000 and not visited[next]:
        # 이전 노드 깊이 + 1
        cnt[next] = cnt[node] + 1
        # 방문 처리
        if visited[next] == 0:
          visited[next] = 1
        # 큐에 삽입
        queue.append(next)


n, k = map(int, r().split())

visited = [0] * (100001)
cnt = [0] * (100001)

print(bfs(n))







# 입력 예시
# 5 17

# 출력 예시
# 4