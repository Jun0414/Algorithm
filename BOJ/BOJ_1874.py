
# 문제 1874번 스택 수열
# Stack(스택)

import sys
r = sys.stdin.readline

n = int(r())
stack = []
arr = []
start = 1

for _ in range(n):
  num = int(r())

  while start <= num:
    stack.append(start)
    arr.append('+')
    start += 1
    
  if stack[-1] == num:
    stack.pop()
    arr.append('-')
  else:
    arr.insert(0, 'NO')

if arr[0] == 'NO':
  print('NO')
else:
  # 배열 안의 내용을 줄바꿈 단위로 출력
  print('\n'.join(arr))





# 입력 예시
# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1

# 5
# 1
# 2
# 5
# 3
# 4

# 출력 예시
# +
# +
# +
# +
# -
# -
# +
# +
# -
# +
# +
# -
# -
# -
# -
# -

# NO