
# 문제 17626번 Four Squares
# DP(다이나믹 프로그래밍), Bruteforcing(브루트포스)


import sys
import math
r = sys.stdin.readline


n = int(r())

dp = [0, 1]

for i in range(2, n + 1):
  min_val = 4
  j = 1

  while math.pow(j, 2) <= i:
    # i보다 작은 j의 제곱수를 뺀 값이 가장 작은 것
    min_val = min(min_val, dp[int(i - math.pow(j, 2))])
    j += 1

  # 최소한 제곱수라서 min_val이 dp[0]으로 설정되더라도
  # 한번의 연산을 거친 것이므로 모든 경우에서 1번의 연산은 필수로 사용
  dp.append(min_val + 1)

print(dp[n])






# 입력 예시
# 25

# 26

# 11339

# 34567

# 출력 예시
# 1

# 2

# 3

# 4