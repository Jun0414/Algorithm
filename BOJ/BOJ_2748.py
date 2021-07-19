
# 문제 2748번 피보나치 수 2
# Dynamic Programming(다이나믹 프로그래밍)

import sys
r = sys.stdin.readline

n = int(r())

# 초기 0과 1을 세팅
fibo = [0] * (n + 1)
fibo[1] = 1
# 2부터 피보나치 적용
for i in range(2, n + 1):
  fibo[i] = fibo[i - 1] + fibo[i - 2]

print(fibo[-1])


# n = int(r())

# first = 0
# second = 1
# for i in range(2, n + 1):
#   fibo = first + second
#   first, second = second, fibo

# print(second)





# 입력 예시
# 10

# 출력 예시
# 55