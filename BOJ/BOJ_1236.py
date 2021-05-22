
# 기초 기본 탐색
# 문제 1236번 성 지키기
# Implementation(구현)


import sys
r = sys.stdin.readline

n, m = map(int, r().split())
check = []
for _ in range(n):
  check.append(r())

row = [0] * n
col = [0] * m
# 이미 경비병이 있는 곳 체크
for i in range(n):
  for j in range(m):
    if check[i][j] == 'X':
      row[i] = 1
      col[j] = 1

# 경비병이 없는 행 카운트
row_cnt = 0
for i in range(n):
  if row[i] == 0:
    row_cnt += 1

# 경비병이 없는 열 카운트
col_cnt = 0
for i in range(m):
  if col[i] == 0:
    col_cnt += 1

print(max(row_cnt, col_cnt))





# 입력 예시
# 4 4
# ....
# ....
# ....
# ....

# 출력 예시
# 4