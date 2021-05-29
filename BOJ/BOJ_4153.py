
# 문제 4153번 직각삼각형
# Geometry(기하학), Math(수학)


import sys
r = sys.stdin.readline

while True:
  num = list(map(int, r().split()))
  if num[0] == 0 and num[1] == 0 and num[2] == 0:
    break

  num.sort()
  if pow(num[0], 2) + pow(num[1], 2) == pow(num[2], 2):
    print('right')
  else:
    print('wrong')






# 입력 예시
# 6 8 10
# 25 52 60
# 5 12 13
# 0 0 0

# 출력 예시
# right
# wrong
# right