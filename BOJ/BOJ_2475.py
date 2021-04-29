
# 문제 2475번 검증수
# 구현

import sys
r = sys.stdin.readline

# arr = list(map(int, r().split()))
arr = [int(x) for x in r().split()]

sum = 0
for num in arr:
  sum += (num)**2

print(sum % 10)





# 입력 예시
# 0 4 2 5 6

# 출력 예시
# 1