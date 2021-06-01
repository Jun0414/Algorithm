
# 문제 1929번 소수 구하기
# Sieve(에라토스테네스의 체), Primality Test(소수 판정)


import sys
import math
r = sys.stdin.readline


n, m = map(int, r().split())

arr = [x for x in range(m + 1)]
arr[1] = 0

for i in range(2, m + 1):
  if arr[i] == 0:
    continue
  for j in range(i * 2, m + 1, i):
    arr[j] = 0

for i in range(n, m + 1):
  if arr[i] != 0:
    print(i)




# # 시간 초과
# n, m = map(int, r().split())

# for i in range(n, m + 1):
#   cnt = 0
#   for j in range(2, i + 1):
#     if i % j == 0 and i != j:
#       break
#     elif i == j:
#       print(i, end=' ')






# 입력 예시
# 3 16

# 출력 예시
# 3
# 5
# 7
# 11
# 13