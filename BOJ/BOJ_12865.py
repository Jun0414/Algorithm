
# 기초 동적 프로그래밍
# 문제 12865번 평범한 배낭
# DP(다이나믹 프로그래밍)


import sys
r = sys.stdin.readline

n, k = map(int, r().split())

# 모든 값을 비교할 수 있는 2중 배열 생성
dp = [[0] * (k + 1) for _ in range(n + 1)]
# 물품 수 만큼 반복
for i in range(1, n + 1):
  weight, value = map(int, r().split())
  # 무게가 1 ~ k 까지 경우의 수 모두 계산하기 위해
  for j in range(1, k + 1):
    # 현재 입력 받은 무게보다 작은 경우 본인의 위 정보 그대로 받아오기
    if j < weight:
      dp[i][j] = dp[i - 1][j]
    # weight가 반복문 j보다 같거나 작은 경우
    # (동일한 무게면 이전 value와 입력받은 value 중 큰 값, j가 더 크면 조합해서 가능한 value와 입력받은 value 중 큰 값)
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])





# 입력 예시
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

# 출력 예시
# 14