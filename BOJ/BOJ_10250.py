
# 문제 10250번 ACM 호텔
# Implementation(구현), Math(수학)


import sys
r = sys.stdin.readline

t = int(r())

for _ in range(t):
  h, w, n = map(int, r().split())
  
  cnt = 1
  for i in range(w):
    for j in range(h):
      if n == cnt:
        print('%d' % (j + 1), end='')
        print('%02d' % (i + 1))
      cnt += 1




# 입력 예시
# 2
# 6 12 10
# 30 50 72

# 출력 예시
# 402
# 1203