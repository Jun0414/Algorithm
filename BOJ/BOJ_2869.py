
# 문제 2869번 달팽이는 올라가고 싶다
# Math(수학)


import sys
r = sys.stdin.readline


a, b, v = map(int, r().split())

# 마지막날 올라간 거리 계산 위해
sub_oneday = v - a

if sub_oneday % (a - b) == 0:
  print(sub_oneday // (a - b) + 1)
else:
  print(sub_oneday // (a - b) + 2)






# 입력 예시
# 2 1 5

# 5 1 6

# 100 99 1000000000

# 출력 예시
# 4

# 2

# 999999901