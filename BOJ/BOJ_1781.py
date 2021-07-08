
# 문제 1781번 컵라면
# Greedy(그리디), Priority Queue(우선순위 큐)


import sys, heapq
r = sys.stdin.readline


n = int(r())

cups = []
q = []
for _ in range(n):
  dead, cup = map(int, r().split())
  cups.append((dead, cup))
cups.sort()

for i in cups:
  heapq.heappush(q, i[1])
  # 데드라인 안에 다 못 푸는 경우
  if i[0] < len(q):
    # 풀 문제 중 컵라면 개수가 가장 적은 것 빼기
    heapq.heappop(q)
print(sum(q))





# 입력 예시
# 7
# 1 6
# 1 7
# 3 2
# 3 1
# 2 4
# 2 5
# 6 1

# 출력 예시
# 15