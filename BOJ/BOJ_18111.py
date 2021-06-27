
# 문제 18111번 마인크래프트
# Bruteforcing(브루투포스 알고리즘)


import sys
from collections import Counter
r = sys.stdin.readline


n, m, b = map(int, r().split())

arr = []
for _ in range(n):
  arr += map(int, r().split())

# 현재 블럭 개수
sum_blocks = sum(arr)
# 면적
square_blocks = n * m
# 높이와 시간 초기화
height, min_time = 0, 1e9

# 같은 층 개수 세기
arr = dict(Counter(arr))
print(arr)

for i in range(257):
  # 기준 i 층 보다 블럭이 많은 경우
  if square_blocks * i <= sum_blocks + b:
    time = 0
    # 땅 다지기 걸리는 시간
    for key in arr:
      if key < i:
        time += (i - key) * arr[key]
      elif key > i:
        time += (key - i) * 2 * arr[key]
    # 최소 시간 갱신
    if min_time >= time:
      min_time = time
      height = i

print(min_time, height)


# # 시간초과
# n, m, b = map(int, r().split())

# arr = [list(map(int, r().split())) for _ in range(n)]
# max_height = 0
# for i in arr:
#   max_height = max(max_height, max(i))

# min_time = 1e11
# height_idx = max_height
# for i in range(max_height):
#   have = 0
#   need = 0
#   for j in range(n):
#     for k in range(m):
#       # 기준 i 보다 현재 낮은 경우
#       if arr[j][k] < i:
#         need += (i - arr[j][k])
#       # 기준 i 보다 현재 높은 경우
#       else:
#         have += (arr[j][k] - i)
#   got_blocks = have + b
#   # 가진 블럭으로 만들 수 없는 경우
#   if got_blocks < need:
#     continue
#   # 가진 블럭으로 만들 수 있는 경우
#   time = (2 * have) + need
#   # 최소시간 갱신
#   if time <= min_time:
#     min_time = time
#     height_idx = i
# print(min_time, height_idx)




# # 시간초과
# n, m, b = map(int, r().split())

# arr = []
# blocks = 0

# for _ in range(n):
#   a = list(map(int, r().split()))
#   for i in range(m):
#     arr.append(a[i])
#     blocks += a[i]

# min_time = 1e9
# max_height = max(arr)
# for i in range(max(arr), -1, -1):
#   std_blocks = i * n * m
#   sum_blocks = b + blocks
#   time = 0

#   if std_blocks <= sum_blocks:
#     for j in arr:
#       if i > j:
#         time += (i - j)
#       else:
#         time += (j - i) * 2
#     if min_time > time:
#       min_time = time
#       max_height = i

# print(min_time, max_height)








# 입력 예시
# 3 4 99
# 0 0 0 0
# 0 0 0 0
# 0 0 0 1

# 3 4 1
# 64 64 64 64
# 64 64 64 64
# 64 64 64 63

# 3 4 0
# 64 64 64 64
# 64 64 64 64
# 64 64 64 63

# 3 4 0
# 5 2 1 0
# 3 4 7 1
# 4 2 5 6

# 출력 예시
# 2 0

# 1 64

# 22 63

# 35 3