
# 문제 11050번 이항 계수 1
# Combinatorics(조합), Implementation(구현), Math(수학)
# 이항 계수
# (n)
# (m)  => n! / M!(n-m)!


import sys
r = sys.stdin.readline

def factorial(num):
  if num == 0:
    return 1
  return num * factorial(num - 1)

n, k = map(int, r().split())

result = factorial(n) // (factorial(k) * factorial(n - k))
print(result)






# 입력 예시
# 5 2

# 출력 예시
# 10