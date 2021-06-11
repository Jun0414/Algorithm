
# 문제 10773번 제로
# Implementation(구현), String(문자열), Stack(스택)


import sys
r = sys.stdin.readline


k = int(r())

nums = [int(r()) for _ in range(k)]
stack = []
for num in nums:
  if num != 0:
    stack.append(num)
  elif num == 0 and len(stack) != 0:
    stack.pop()

if len(stack) == 0:
  print(0)
else:
  print(sum(stack))







# 입력 예시
# 4
# 3
# 0
# 4
# 0

# 10
# 1
# 3
# 5
# 4
# 0
# 0
# 7
# 0
# 0
# 6

# 출력 예시
# 0

# 7