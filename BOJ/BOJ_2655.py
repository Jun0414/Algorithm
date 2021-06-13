
# 핵심 동적 프로그래밍
# 문제 2655번 가장 높은 탑 쌓기
# DP(다이나믹 프로그래밍), Sorting(정렬)


import sys
import copy
r = sys.stdin.readline


n = int(r())

# 벽돌 번호, 넓이, 높이, 무게를 튜플로 리스트에 저장
bricks = []
for i in range(1, n + 1):
  width, height, weight = map(int, r().split())
  bricks.append((i, width, height, weight))

# 넓이를 기준으로 내림차순 정렬
bricks.sort(key=lambda x: -x[1])

# 쌓을 벽돌 번호 저장 공간
dp = [[] for _ in range(n)]
for i in range(n):
  dp[i].append(bricks[i][0])

# 최대 높이 저장 공간
dp_height = []
for i in range(n):
  dp_height.append(bricks[i][2])

for i in range(1, n):
  for j in range(i):
    # 무게가 내림차순이면
    if bricks[i][3] < bricks[j][3]:
      # 높이가 더 높아 졌다면
      if dp_height[i] < dp_height[j] + bricks[i][2]:
        dp_height[i] = dp_height[j] + bricks[i][2]
        # 벽돌 번호 저장
        if dp[i] < dp[i] + dp[j]:
          dp[i] = copy.deepcopy(dp[j] + [bricks[i][0]])

# 최대 높이 저장 공간 번호
max_index = dp_height.index(max(dp_height))

print(len(dp[max_index]))
# 역으로 출력
for i in range(len(dp[max_index]) - 1, -1, -1):
  print(dp[max_index][i])







# # 순서를 바꾸지 않고 쌓을때
# dp = [(0, 0, 0)]
# for _ in range(n):
#   width, height, weight = map(int, r().split())
#   dp.append((width, height, weight))

# cnt = [1] * (n + 1)
# dp_height = [0] * (n + 1)
# dp_height[1] = dp[1][1]

# dp_order = [[] for _ in range(n + 1)]
# dp_order[1].append(1)

# max_height = 0
# max_index = 0
# for i in range(1, n + 1):
#   for j in range(1, i):
#     if dp[j][0] > dp[i][0]:
#       if dp[j][2] > dp[i][2]:
#         if dp_height[i] < dp_height[j] + dp[i][1]:
#           dp_order[i] = copy.deepcopy(dp_order[j])
#           dp_order[i].append(i)
#           cnt[i] = cnt[j] + 1
#           dp_height[i] = dp_height[j] + dp[i][1]
#         if max_height < dp_height[i]:
#           max_index = i
#           max_height = dp_height[i]


# print(cnt[max_index])
# while dp_order[max_index]:
#   print(dp_order[max_index].pop())






# 입력 예시
# 5
# 25 3 4
# 4 4 6
# 9 2 3
# 16 2 5
# 1 5 2

# 출력 예시
# 3
# 5
# 3
# 1