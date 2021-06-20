
# 문제 2775번 부녀회장이 될테야
# Math(수학)


import sys
r = sys.stdin.readline

t = int(r())

dp = [[[] for _ in range(15)] for _ in range(15)]

for i in range(15):
  for j in range(1, 15):
    if i == 0:
      dp[i][j] = j
    elif j == 1:
      dp[i][j] = 1
    else:
      dp[i][j] = dp[i-1][j] + dp[i][j-1]

for _ in range(t):
  k = int(r())
  n = int(r())
  print(dp[k][n])







# 입력 예시
# 2
# 1
# 3
# 2
# 3

# 출력 예시
# 6
# 10