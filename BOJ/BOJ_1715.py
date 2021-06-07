
# 핵심 고급 탐색
# 문제 1715번 카드 정렬하기
# Greedy(그리디), Priority Queue(우선순위 큐)


import sys
import heapq
r = sys.stdin.readline


n = int(r())

arr = []
for _ in range(n):
  heapq.heappush(arr, int(r()))

result = 0
while len(arr) != 1:
  fi = heapq.heappop(arr)
  se = heapq.heappop(arr)
  result += fi + se
  heapq.heappush(arr, fi + se)

print(result)






# 입력 예시
# 3
# 10
# 20
# 40

# 출력 예시
# 100