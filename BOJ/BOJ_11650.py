
# 핵심 정렬
# 문제 11650번 좌표 정렬하기
# Sorting(정렬)

import sys
r = sys.stdin.readline

n = int(r())

data = []
for _ in range(n):
  x, y = map(int, r().split(' '))
  data.append((x, y))

# 기본 정렬함수는 차례대로 0,1,2, ... 인덱스순으로 넘어가며 자동으로 순차적으로 정렬한다
data = sorted(data)

for x, y in data:
  print(x, y)





# 입력 예시
# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3

# 출력 예시
# 1 -1
# 1 1
# 2 2
# 3 3
# 3 4