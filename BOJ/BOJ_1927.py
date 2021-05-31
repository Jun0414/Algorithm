
# 핵심 고급 탐색
# 문제 1927번 최소 힙
# Priority Queue(우선순위 큐)
# heapq 라이브러리는 최소힙으로 구성한다


import sys
import heapq
r = sys.stdin.readline


n = int(r())

queue = []
for _ in range(n):
  num = int(r())

  if num == 0:
    if queue:
      print(heapq.heappop(queue))
    else:
      print(0)
  else:
    heapq.heappush(queue, num)




# 입력 예시
# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32

# 출력 예시
# 0
# 1
# 2
# 12345678
# 0