
# 핵심 동적 프로그래밍
# 문제 9251번 LCS
# DP(다이나믹 프로그래밍), LCS(가장 긴 공통 부분 수열)


import sys
r = sys.stdin.readline


word1 = r().strip()
word2 = r().strip()

dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

for i in range(1, len(word2) + 1):
  for j in range(1, len(word1) + 1):
    if word2[i - 1] == word1[j - 1]:
      dp[i][j] = dp[i - 1][j - 1] + 1
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(word2)][len(word1)])





# 입력 예시
# ACAYKP
# CAPCAK

# 출력 예시
# 4