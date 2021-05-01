
# 핵심 재귀 호출
# 문제 2747번 피보나치 수
# 구현

import sys
r = sys.stdin.readline

# 재귀로 해결
n = int(r())

def fibo_func(num):
  if fibo[num] != -1:
    return fibo[num]
  return fibo_func(num - 1) + fibo_func(num - 2)

fibo = [-1] * (n + 1)
fibo[0], fibo[1] = 0, 1
print(fibo_func(n))


# # 반복문으로 해결
# n = int(r())

# fibo = [0] * (n + 1)
# fibo[1] = 1

# for i in range(2, n + 1):
#   fibo[i] = fibo[i - 1] + fibo[i - 2]

# print(fibo[-1])





# 입력 예시
# 10

# 출력 예시
# 55