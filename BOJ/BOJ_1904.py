
# 기초 동적 프로그래밍
# 문제 1904번 01타일
# DP(다이나믹 프로그래밍)


import sys
r = sys.stdin.readline


def fibo(n):
  for i in range(2, n + 1):
    tile[i] = (tile[i - 1] + tile[i - 2]) % 15746
  
  return tile[n]


n = int(r())

tile = [0] * (n + 1)
tile[0] = 1
tile[1] = 1

print(fibo(n))




# 입력 예시
# 4

# 출력 예시
# 5