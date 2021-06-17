
# 문제 2231번 분해합
# Bruteforcing(브루트포스)


import sys
r = sys.stdin.readline


n = int(r())

num = 1
while num < n:
  i = num
  sum = 0

  while i != 0:
    sum += i % 10
    i //= 10
  sum += num

  if sum == n:
    print(num)
    break
  
  num += 1
  
if num == n:
  print(0)







# 입력 예시
# 216

# 출력 예시
# 198