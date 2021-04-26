
# 문제 2798번 블랙잭
# Brute Force(브루트 포스 알고리즘, 완전 탐색)

import sys
r = sys.stdin.readline

n, m = map(int, r().split())
cards = list(map(int, r().split()))
biggest = 0

# 중복되지 않게 카드 3장의 합이 가장 큰 합 구하기
for i in range(n):
  for j in range(i + 1, n):
    for k in range(j + 1, n):
      sum3 = cards[i] + cards[j] + cards[k]

      if sum3 <= m:
        biggest = max(biggest, sum3)

print(biggest)


# 입력 예시
# 5 21
# 5 6 7 8 9

# 10 500
# 93 181 245 214 315 36 185 138 216 295

# 출력 예시
# 21

# 497