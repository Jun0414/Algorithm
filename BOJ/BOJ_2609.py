
# 문제 2609번 최대공약수와 최소 공배수
# Euclidean(유클리드 호제법), Math(수학)
# 유클리드 호제법
# 최대 공약수 = 큰 수에서 작은 수를 나눈 나머지 값(다시 나눈 값에서 나머지로 나눈 나머지 값) 반복하며 나머지 값이 0이 될때 나눈 수
# 최소 공배수 = 두 숫자의 곱을 최대 공약수로 나눈 값

import sys
r = sys.stdin.readline

def gcd(num1, num2):
  while num2 > 0:
    num1, num2 = num2, num1 % num2

  return num1

def lcm(num1, num2):
  return num1 * num2 // gcd(num1, num2)

num1, num2 = map(int, r().split())

print(gcd(min(num1, num2), max(num1, num2)))
print(lcm(min(num1, num2), max(num1, num2)))





# 입력 예시
# 24 18

# 출력 예시
# 6
# 72