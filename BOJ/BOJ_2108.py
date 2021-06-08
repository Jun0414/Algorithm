
# 문제 2108번 통계학
# Implementation(구현), Sorting(정렬)


import sys
from collections import Counter
r = sys.stdin.readline


n = int(r())

numbers = []
for _ in range(n):
  numbers.append(int(r().strip()))
numbers.sort()

san = round(sum(numbers) / n)
print(san)
center = numbers[(n // 2)]
print(center)

# 숫자 카운트
cnt = dict(Counter(numbers))
# 튜플로 만들기(오름 차순)
cnt = sorted(cnt.items())
# 개수 내림차순 정렬 후, 숫자 오름차순으로 정렬
cnt = sorted(cnt, key= lambda x: (-x[1], x[0]))

# 비교 개수가 2개 미만인 경우와 개수가 동일한 숫자가 없는 경우
if len(cnt) < 2 or cnt[0][1] != cnt[1][1]:
  print(cnt[0][0])
# 개수가 동일한 숫자가 있는 경우
else:
  print(cnt[1][0])

sub = numbers[-1] - numbers[0]
print(sub)





# 입력 예시
# 5
# 1
# 3
# 8
# -2
# 2

# 1
# 4000

# 5
# -1
# -2
# -3
# -1
# -2

# 출력 예시
# 2
# 2
# 1
# 10

# 4000
# 4000
# 4000
# 0

# -2
# -2
# -1
# 2