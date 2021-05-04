
# 기초 기본 탐색
# 문제 1568번 새
# Implementation(구현)


import sys
r = sys.stdin.readline

n = int(r())

time = 0
num = 1
while n > 0:
  if n < num:
    num = 1

  n -= num
  time += 1
  num += 1

print(time)





# 입력 예시
# 14

# 출력 예시
# 7