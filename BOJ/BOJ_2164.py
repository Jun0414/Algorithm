
# 문제 2164번 카드2
# Queue(큐)
# 짝수만 남게된다. 결과값을 나열해 보면 2의 제곱승 수 단위로 반복된다.

import sys, math
r = sys.stdin.readline

n = int(r())

x = int(math.log(n, 2))
pow_two = 2**x
if n == pow_two:
  print(n)
else: # (n > pow_two)
  print(2 * (n - pow_two))




# 입력 예시
# 6

# 출력 예시
# 4