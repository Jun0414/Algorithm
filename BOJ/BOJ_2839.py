
# 문제 2839번 설탕 배달
# DP(다이나믹 프로그래밍), Greedy(그리디)


import sys
r = sys.stdin.readline


def cnt_sugar(n):
  hi = 1

n = int(r())

sugar5 = n // 5
while sugar5 > -1:
  sugar3 = (n - 5 * sugar5) // 3

  if (n - 5 * sugar5) % 3 == 0:
    print(sugar5 + sugar3)
    break
  sugar5 -= 1

if sugar5 == -1 and n % 3 != 0:
  print(-1)






# 입력 예시
# 18

# 4

# 6

# 9

# 11

# 출력 예시
# 4

# -1

# 2

# 3

# 3