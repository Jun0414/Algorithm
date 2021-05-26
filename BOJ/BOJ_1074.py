# ***
# 핵심 재귀 호출
# 문제 1074번 Z
# Divide And Conquer(분할 정복), Recursion(재귀)


import sys
r = sys.stdin.readline

cnt = 0
def z(n, row, col):
  global cnt

  if n == 1:
    if row == r and col == c:
      print(cnt)
      return
    cnt += 1
    if row == r and col + 1 == c:
      print(cnt)
      return
    cnt += 1
    if row + 1 == r and col == c:
      print(cnt)
      return
    cnt += 1
    if row + 1 == r and col + 1 == c:
      print(cnt)
      return
    cnt += 1
    return
  
  n -= 1
  # 4등분한 사각형의 한 변의 길이
  one_side = (2**n)

  # 1사분면에 위치하는 경우
  if row + one_side > r and col + one_side > c:
    # 각 사분면의 좌상단 좌표
    z(n, row, col)
  # 2사분면에 위치하는 경우
  elif row + one_side > r and col + one_side <= c:
    # 1사분면 카운트
    cnt += one_side * one_side
    # 각 사분면의 좌상단 좌표
    z(n, row, col + (2**n))
  # 3사분면에 위치하는 경우
  elif row + one_side <= r and col + one_side > c:
    # 1, 2사분면 카운트
    cnt += 2 * (one_side * one_side)
    # 각 사분면의 좌상단 좌표
    z(n, row + (2**n), col)
  # 4사분면에 위치하는 경우
  elif row + one_side <= r and col + one_side <= c:
    # 1, 2, 3사분면 카운트
    cnt += 3 * (one_side * one_side)
    # 각 사분면의 좌상단 좌표
    z(n, row + (2**n), col + (2**n))

n, r, c = map(int, r().split())
z(n, 0, 0)





# 입력 예시
# 2 3 1

# 3 7 7

# 출력 예시
# 11

# 63