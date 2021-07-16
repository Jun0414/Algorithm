
# 문제 11651번 좌표 정렬하기 2
# Sorting(정렬)


import sys
r = sys.stdin.readline


n = int(r())

xy = dict()
for i in range(n):
  x, y = map(int, r().split())
  xy[i] = (x, y)

xy = sorted(xy.items(), key= lambda x: (x[1][1], x[1][0]))

for i in range(n):
  print(xy[i][1][0], xy[i][1][1])





# 입력 예시
# 5
# 0 4
# 1 2
# 1 -1
# 2 2
# 3 3

# 출력 예시
# 1 -1
# 1 2
# 2 2
# 3 3
# 0 4