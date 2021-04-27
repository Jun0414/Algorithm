
# 문제 2920번 음계

import sys
r = sys.stdin.readline

scale = list(map(int, r().split()))

ascending = True
descending = True

for i in range(7):
  # 오름차순이 아니면
  if scale[i] > scale[i + 1]:
    ascending = False
  # 내림차순이 아니면
  elif scale[i] < scale[i + 1]:
    descending = False

if ascending:
  print('ascending')
elif descending:
  print('descending')
else:
  print('mixed')





# 입력 예시
# 1 2 3 4 5 6 7 8

# 8 7 6 5 4 3 2 1

# 8 1 7 2 6 3 5 4

# 출력 예시
# ascending

# descending

# mixed