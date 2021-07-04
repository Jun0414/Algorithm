
# 문제 2012번 등수 매기기
# Greedy(그리디), Sorting(정렬)


import sys
r = sys.stdin.readline


n = int(r())

rank = [0]
for _ in range(n):
  rank.append(int(r()))
rank.sort()

cnt = 0
for i in range(1, n + 1):
  cnt += abs(i - rank[i])

print(cnt)






# 입력 예시
# 5
# 1
# 5
# 3
# 1
# 2

# 출력 예시
# 3