
# 문제 1978번 소수 찾기
# math(수학), Prime Number(소수), sieve(에라토스테네스의 체)

import sys
r = sys.stdin.readline

n = int(r())
num = list(map(int, r().split()))

prime_num_cnt = 0
for i in num:
  check = 1
  # 2부터 나눠지는지 반복
  for j in range(2, i + 1):
    if check > 2:
      break
    if i % j == 0:
      check += 1
  
  if check == 2:
    prime_num_cnt += 1

print(prime_num_cnt)






# 입력 예시
# 4
# 1 3 5 7

# 출력 예시
# 3