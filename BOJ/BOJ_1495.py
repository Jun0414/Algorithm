
# 핵심 동적 프로그래밍
# 문제 1495번 기타리스트
# DP(다이나믹 프로그래밍)


import sys
r = sys.stdin.readline


n, s, m = map(int, r().split())
volume = list(map(int, r().split()))

# n * m 데이터 공간 확보
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1

# 출력 가능한 부분만 1로 저장
for i in range(1, n + 1):
  for j in range(m + 1):
    if dp[i - 1][j] == 1:
      if j + volume[i - 1] <= m:
        dp[i][j + volume[i - 1]] = 1
      if j - volume[i - 1] >= 0:
        dp[i][j - volume[i - 1]] = 1

# 마지막의 가장 큰 수 찾기
result = -1
for i in range(m, -1, -1):
  if dp[n][i] == 1:
    result = i
    break
print(result)





# # 시간 초과
# def music(start, index, maximum):
#   global max_volume, cnt

#   if index == n:
#     max_volume = max(max_volume, start)
#     cnt += 1
#     return
#   if start - volume[index] >= 0:
#     music(start - volume[index], index + 1, maximum)
#   if start + volume[index] <= maximum:
#     music(start + volume[index], index + 1, maximum)


# n, s, m = map(int, r().split())
# volume = list(map(int, r().split()))

# i = 0
# cnt = 0
# max_volume = s
# music(s, i, m)
# if cnt != 0:
#   print(max_volume)
# else:
#   print(-1)





# 입력 예시
# 3 5 10
# 5 3 7

# 출력 예시
# 10