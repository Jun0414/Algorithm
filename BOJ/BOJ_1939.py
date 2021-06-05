
# 핵심 기본 탐색
# 문제 1939번 중량제한
# Graph Search(그래프 탐색, BFS), Binary Search(이진 탐색)

# 이중 배열로 시작,끝,값 설정하는 것 보다는
# 단일 배열에 시작 인덱스에 튜플로 끝, 값 설정하는 것이 관리 편함


from collections import deque
import sys
r = sys.stdin.readline

# 경로 존재 여부 판단
def bfs(c):
  # 리스트로 추가해야 while문 돌릴 수 있다(iterable)
  queue = deque([s_island])
  visited = [0] * (n + 1)
  visited[s_island] = 1

  while queue:
    start = queue.popleft()
    if start == e_island:
      return 1

    for end, weight in adj[start]:
      if not visited[end] and weight >= c:
        visited[end] = 1
        queue.append(end)

  return 0

n, m = map(int, r().split())
adj = [[] for _ in range(n + 1)]

min_w = 1_000_000_000
max_w = 1
for _ in range(m):
  s, e, w = map(int, r().split())
  adj[s].append((e, w))
  adj[e].append((s, w))
  min_w = min(min_w, w)
  max_w = max(max_w, w)

s_island, e_island = map(int, r().split())

result = min_w
# 큰 중량으로 갱신하며 이진탐색으로 중량 선택
while min_w <= max_w:
  # 중량 선택
  mid = (min_w + max_w) // 2

  # 경로 존재하므로 저장 및 더 큰 중량 경로 설정
  if bfs(mid):
    result = mid
    min_w = mid + 1
  # 경로 존재하지 않으므로 더 낮은 중량 경로 설정
  else:
    max_w = mid - 1

print(result)





# 입력 예시
# 3 3
# 1 2 2
# 3 1 3
# 2 3 2
# 1 3

# 출력 예시
# 3