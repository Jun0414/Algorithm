
# 기초 동적 프로그래밍
# 문제 11053번 가장 긴 증가하는 부분 수열
# DP(다이나믹 프로그래밍), LIS(최장 증가 수열)


import sys
r = sys.stdin.readline


n = int(r())
arr = list(map(int, r().split()))
dp = [1] * n

for i in range(1, n):
  for j in range(i):
    # 기준 i 보다 작은 경우
    if arr[j] < arr[i]:
      # 최장 증가 수열이 긴 것을 채택(+1은 이전 최장 증가 수열에 본인을 포함하게 되므로)
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))





# 입력 예시
# 6
# 10 20 10 30 20 50

# 출력 예시
# 4